"""
Subscription Auditor - local web app.

The md files remain the brain; this app is plumbing + UI:
loads operator files → assembles prompt → calls Claude → renders report
→ logs every audit to history.json.

"""

import json
import os
import time
from pathlib import Path

from anthropic import Anthropic
from flask import Flask, jsonify, request

ROOT = Path(__file__).resolve().parent.parent          # subscription-auditor/

# Load .env (no dependency needed) - checks interface/ then the folder root.
for env_file in (Path(__file__).resolve().parent / ".env", ROOT / ".env"):
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
        break
HISTORY = Path(__file__).resolve().parent / "history.json"
FILES = ["identity.md", "rules.md", "examples.md",
         "reference/input-template.md", "reference/cancellation-templates.md"]
MODEL = "claude-sonnet-4-6"

app = Flask(__name__)
client = Anthropic()


def build_prompt(subs: str) -> str:
    docs = "".join(f"\n\n===== FILE: {f} =====\n{(ROOT / f).read_text()}" for f in FILES)
    return (
        "You are the operator defined by the files below. Follow identity.md and "
        "apply rules.md IN ORDER, citing rule numbers. Produce the audit report "
        "exactly per reference/cancellation-templates.md section D, then an "
        "'Execute this week' list. Decide - do not ask questions; use Section 0 "
        "assumptions for missing data and mark them."
        f"{docs}\n\n===== MY SUBSCRIPTIONS =====\n{subs}\n\nRun the full audit now."
    )


@app.post("/audit")
def audit():
    try:
        subs = (request.get_json(silent=True) or {}).get("subscriptions", "").strip()
        if not subs:
            return jsonify(error="No subscriptions provided"), 400
        if not os.environ.get("ANTHROPIC_API_KEY"):
            return jsonify(error="ANTHROPIC_API_KEY not found - check your .env "
                                 "(expected line: ANTHROPIC_API_KEY=sk-ant-...)"), 500
        response = client.messages.create(
            model=MODEL, max_tokens=4096,
            messages=[{"role": "user", "content": build_prompt(subs)}],
        )
        report = "".join(b.text for b in response.content if b.type == "text")
        log = json.loads(HISTORY.read_text()) if HISTORY.exists() else []
        log.append({"ts": time.strftime("%Y-%m-%d %H:%M"), "input": subs, "report": report})
        HISTORY.write_text(json.dumps(log, indent=2))
        return jsonify(report=report)
    except Exception as e:                       # always answer in JSON
        return jsonify(error=f"{type(e).__name__}: {e}"), 500


@app.get("/history")
def history():
    return jsonify(json.loads(HISTORY.read_text()) if HISTORY.exists() else [])


PAGE = """<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Subscription Auditor</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.0/marked.min.js"></script>
<style>
:root{--bg:#0f1117;--panel:#181b24;--text:#e2e6ef;--muted:#9aa3b5;--accent:#5eb1ff;--green:#7ee0a3;--border:#2a3042;--code:#11141c}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
.wrap{max-width:860px;margin:0 auto;padding:36px 22px}
h1{font-size:24px}.sub{color:var(--muted);margin:4px 0 22px}
textarea{width:100%;min-height:170px;background:var(--code);color:var(--text);border:1px solid var(--border);border-radius:10px;padding:13px;font-family:Menlo,Consolas,monospace;font-size:13.5px}
button{background:var(--accent);color:#0b1220;border:none;border-radius:10px;padding:12px 22px;font-size:15px;font-weight:700;cursor:pointer;margin-top:14px}
button:disabled{opacity:.5}
#report{margin-top:28px;background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:22px;display:none}
#report table{border-collapse:collapse;width:100%;margin:12px 0;font-size:14px}
#report th,#report td{border-bottom:1px solid var(--border);padding:8px 10px;text-align:left}
#report h1,#report h2,#report h3{margin:14px 0 8px;color:var(--accent)}
.spin{color:var(--green);margin-left:12px}
</style></head><body><div class="wrap">
<h1>💸 Subscription Auditor</h1>
<p class="sub">Decisions by <code>rules.md</code> · engine: Claude · this app just carries the messages.</p>
<textarea id="subs" placeholder="Netflix ~ $15.49/mo ~ yesterday ~ whole family&#10;ChatGPT Plus ~ $20/mo ~ today ~ me"></textarea>
<button id="go">Run audit</button><span class="spin" id="spin"></span>
<div id="report"></div>
<script>
const go=document.getElementById('go'),spin=document.getElementById('spin'),rep=document.getElementById('report');
go.onclick=async()=>{
  go.disabled=true;spin.textContent='Auditing… (10–30s)';rep.style.display='none';
  try{
    const r=await fetch('/audit',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({subscriptions:document.getElementById('subs').value})});
    const raw=await r.text();
    let d; try{d=JSON.parse(raw);}catch(e){d={error:'Server said: '+raw.slice(0,300)};}
    rep.innerHTML=d.error?('<b>Error:</b> '+d.error):marked.parse(d.report);
    rep.style.display='block';
  }catch(e){rep.innerHTML='<b>Error:</b> '+e;rep.style.display='block';}
  go.disabled=false;spin.textContent='';
};
</script></div></body></html>"""


@app.get("/")
def index():
    return PAGE


if __name__ == "__main__":
    if os.environ.get("ANTHROPIC_API_KEY"):
        print("✓ API key loaded")
    else:
        print("✗ ANTHROPIC_API_KEY not found - put ANTHROPIC_API_KEY=sk-ant-... "
              "in subscription-auditor/.env or interface/.env")
    app.run(port=5050, debug=False)
