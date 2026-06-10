# Input Template

Paste subscriptions in this format - one line each, ~ separates the
four fields. Missing fields are fine: the auditor works with what it
gets and notes its assumptions (rules.md Section 0).

```
Name ~ price/cycle ~ last used ~ who uses it (+ any notes)
Netflix ~ $15.49/mo ~ yesterday ~ whole family
ChatGPT Plus ~ $20/mo ~ today ~ me, also have Claude Pro
Gym ~ $45/mo ~ 6 weeks ago ~ me, 12-mo contract ends Sept
iCloud+ ~ $2.99/mo ~ constant ~ me, photo backup
Adobe ~ $119.88/yr ~ 2 months ago ~ me, renews in 26 days
```

Extra context (renewal dates, contracts, overlaps, signup price) goes
at the end of the fourth field after a comma - the auditor reads the
whole line and uses everything it finds.

Minimum viable input: name + price. The auditor will mark
usage-unknown items and decide per the rules' conservative paths.
