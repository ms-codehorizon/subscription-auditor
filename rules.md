# Rules: Decision Logic

Evaluate every subscription through these sections IN ORDER. First rule
that fires decides. Note the rule number in your output (e.g. "CANCEL - 3a").

## User preferences (overrides - edit these, they win ties)

| Category | Preferred tool | Note |
|---|---|---|
| AI assistants / coding AI | Claude | Cancel overlapping AI tools (ChatGPT, Cursor, etc.) unless a dated project requires them |

## Section 0 Assumptions & normalization (apply before everything)

- 0a. Blank or unknown "last used" → treat as zero use in 60 days,
      unless the item is protected (Section 1) or shared (then Section 5a FLAG).
      Every assumption must appear in the output's Why column.
- 0b. Normalize all prices to $/month equivalent (annual ÷ 12) before
      any comparison in Section 4 or Section 6. Report both figures for annual plans.
- 0c. Missing "who uses it" → assume solo user; state the assumption.

## Section 1 Protected list (check first - overrides everything)

Never CANCEL or DOWNGRADE, output is always KEEP (next review in 12 months):

- 1a. Password manager
- 1b. Cloud backup of irreplaceable data (photos, documents)
- 1c. Anything used by another household member within 30 days
      → if their usage is unknown, FLAG (see Section 5), don't guess
- 1d. Anything where cancelling loses data that can't be exported first
      → KEEP this cycle, output must include the export plan

## Section 2 Renewal urgency (process these first in the output)

- 2a. Annual renewal within 30 days → audit NOW at top of report; if the
      decision is CANCEL, the draft must say "turn off auto-renew today."
- 2b. Annual plan already paid with >60 days remaining → decision applies
      at renewal: output "CANCEL AT RENEWAL (date)" with a reminder line.
      Never refund-chase mid-term unless price rose mid-contract.

## Section 3 Usage (the workhorse)

- 3a. Zero uses in the last 60 days → CANCEL.
- 3b. Used 1-2 times in 60 days AND price > $10/month → CANCEL.
- 3c. Used 1-2 times in 60 days AND price ≤ $10/month → KEEP only if it
      survives Section 4 overlap; review again in 90 days.
- 3d. Regular use but on a tier above need (family plan / 1 user,
      pro plan / basic features) → DOWNGRADE to the named cheaper tier.
- 3e. "I might need it soon" is not usage. Future need without a dated,
      named project in the next 60 days → still CANCEL (note: resubscribe
      when the project starts).

## Section 4 Overlap (one job, one tool)

- 4a. Two+ services in the same category (two video streamers, two AI
      assistants, two note apps): rank by uses-per-month; KEEP the top
      one, CANCEL the rest.
- 4b. Exception: combined cost of the overlapping set ≤ $20/month AND
      each used weekly → both may stay (overlap is paid for by usage).
- 4c. A free tier covers the user's actual usage pattern → CANCEL the
      paid plan, note "move to free tier" in the draft.
- 4d. Usage tie within a category → the User preferences table (top of
      this file) decides. No preference listed → KEEP the cheaper one.
      Never resolve a tie arbitrarily.

## Section 5 FLAG - the narrow escalation lane

FLAG only when (max ~10% of any audit should land here):

- 5a. Shared household item with unknown usage by others (per 1c)
- 5b. Work-related and possibly reimbursable → draft the expense request
- 5c. Contract lock-in with early-termination fee > remaining cost

A FLAG output still does work: state what's unknown, who to ask, and
what the decision will be once answered ("If your partner hasn't used
it in 30 days → CANCEL per 3a").

## Section 6 Price & value modifiers

- 6a. Price increased >30% since signup with no usage increase → CANCEL,
      and the draft includes the retention-offer ask first
      (template: reference/cancellation-templates.md Section B).
- 6b. Entertainment cost-per-use > $10 (price ÷ uses last month) →
      DOWNGRADE if a tier exists, else CANCEL.
- 6c. Bundle math: if 2+ services are cheaper inside a bundle the user
      already qualifies for, recommend the bundle switch under KEEP.

## Tie-breaker

If after all sections two outcomes seem defensible: CANCEL beats KEEP,
DOWNGRADE beats both. Bias to saving money - reversing a cancellation
is cheap; forgotten auto-renew is not.
