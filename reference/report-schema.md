# Report Schema (machine-readable output)

Used when an interface requests the audit as structured data instead of
the human-readable report (Section D of cancellation-templates.md).
The DECISIONS are identical either way - only the packaging differs.

## Output

Respond with ONLY a raw JSON object. No markdown fences, no commentary.

```
{
  "summary": { "total_mo": number, "savings_mo": number },
  "items": [
    {
      "name": string,
      "per_mo": number,            // normalized per rule 0b
      "decision": "KEEP" | "DOWNGRADE" | "CANCEL" | "CANCEL AT RENEWAL" | "FLAG",
      "rule": string,              // e.g. "4a+4d"
      "why": string,               // max 12 words, plain hyphens only
      "urgent": boolean,           // true only for Section 2 renewal urgency
      "draft": string | null
    }
  ],
  "execute_this_week": [ string ]  // one line each, next-7-days actions only
}
```

## Rules (same as Section D - if these two files disagree, fix it)

- Item order: urgent renewals first, then CANCELs, DOWNGRADEs, FLAGs, KEEPs.
- "draft" only for items needing a written artifact: retention ask (6a),
  reimbursement request (5b), data-export plan (1d). Null for everything else.
- Plain hyphens everywhere. Never em-dashes.
