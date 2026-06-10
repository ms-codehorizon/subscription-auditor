# Examples: Decisions in Action

## Example 1 - clean cancel (the common case)

**Input:** HBO Max, $15.99/mo, last watched ~3 months ago, solo profile.

**Decision: CANCEL - rule 3a** (zero uses in 60 days; not protected; no
shared usage).

**Output draft:** "Cancel via Account → Subscriptions → Cancel. No data
to export. Saves $15.99/mo. Resubscribe next time a show you want
actually airs - their content is rentable per-season anyway."

## Example 2 - downgrade (right service, wrong tier)

**Input:** Spotify Family, $19.99/mo, used daily - but by exactly one
person.

**Decision: DOWNGRADE - rule 3d** (regular use, tier above need; family
plan serving one user). Individual plan named: Premium Individual,
$11.99/mo.

**Output draft:** "Switch: Account → Manage plan → Premium Individual.
Saves $8/mo. Note: other family members lose access - confirm nobody
else streams on it this month (if unsure, this becomes FLAG 5a)."

## Example 3 - the edge case the obvious rules don't cover

**Input:** Adobe Lightroom annual plan, $119/yr, paid 7 months ago,
zero edits in 90 days - but 40GB of photos in Adobe cloud. Renewal in
5 months.

**Why it's tricky:** 3a screams CANCEL (unused), but 1d blocks instant
cancellation (data loss), and 2b says mid-term refund-chasing is a
waste.

**Decision: CANCEL AT RENEWAL - rules 1d + 2b + 3a layered.**

**Output draft:** "Plan: (1) This week - export all 40GB originals to
local/cloud backup [steps]. (2) Set reminder for [renewal date minus
14 days]. (3) Turn off auto-renew now; access continues until renewal.
Net effect: $119/yr saved starting [date], zero data lost."

The operator never asked "do you want to keep Adobe?" - it sequenced
the conflict between rules into a dated plan. That's the job.

## Example 4 - overlap tie broken by preference (Section 4d)

**Input:** ChatGPT Plus $20/mo, used daily. Claude Pro $20/mo, used
daily. Same category (AI assistants), combined $40 > 4b's exception.

**Decision: CANCEL ChatGPT Plus - rules 4a + 4d.** Usage is tied, so
the preferences table decides: preferred AI assistant = Claude.

**Output draft:** "Cancel ChatGPT Plus (Settings → Subscription).
Saves $20/mo. Claude Pro stays as the sole AI assistant. Resubscribe
only for a dated project that requires it (rule 3e standard applies)."

## Example 5 - missing data, conservative path (Section 0a)

**Input:** Peloton App ~ $12.99/mo ~ (last used blank) ~ me

**Decision: CANCEL - rules 0a + 3a.** Blank usage = zero use by
assumption; not protected, not shared.

**Output draft:** "Cancel via app store subscription settings. Saves
$12.99/mo. ASSUMPTION: no recorded use in 60 days - if that's wrong,
say 'KEEP Peloton' and it gets a 30-day re-review instead."
