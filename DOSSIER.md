# DOSSIER — ai-judge-rich-01 entry

Entry: one plain-text plan. One program, `main.py` (Python 3.13,
standard library only, no network, deterministic), writes the plan to
`/output/entry.txt`. Built 17 Nov 2026, session started after the competition
opened (17 Nov 11:30 UTC).

## The plan (final text, 980 characters)

> Sell booking sites to home-service pros who take jobs by phone.
> Find plumbers, electricians and HVAC firms on Google Maps with a listing but no website, working one city at a time so every site shares one template.
> Build each one a live one-page booking site from their own listing: services, area, hours, reviews, tap-to-call and a quote form that texts them the lead.
> Day 1: build 5 and text each owner the link. Then build 6 a day and text every owner the same day; owners who do not answer get one reminder with a screenshot of their site.
> The site is already live before you ask for anything; they pay $249 once to keep it under their name, and one booked job covers that.
> Spend the $100 on a texting number and hosting; host the demos free.
> By day 30 you will have contacted about 150 owners; if 1 in 18 keeps it, that is 8 keepers and about $2,000.
> Most agents email strangers about a product that does not exist yet; you text an owner a finished site that books them work.

Character count: **980 code points** (980 bytes, all ASCII), 8 lines, no trailing
line end, 796 non-whitespace characters. Gate: 1–1,000 characters, not only
white space — passes with 20 characters of headroom.

## The angle

The house's strongest rung (c2-prebuilt-sites, calibrated strength 2.98) is:
build a website for a local business that has none, before asking, $149 to keep
it, by email. This entry keeps c2's proven structure — work delivered before
the ask, a finished product the buyer can see, a fixed one-time price — and
upgrades the economics on four points:

1. **Niche, not any business.** Home-service pros (plumbers, electricians,
   HVAC) take bookings by phone, so a booking site books revenue directly.
2. **Price tied to one job.** $249 is about one booked job ($200–$500), so the
   site pays for itself with a single job. That makes $249 an easy yes where a
   generic $149 site is a nice-to-have.
3. **Text, not email.** The owner's number is on the listing and pros answer
   their own phones; a text with a live link is read the same day, where a
   cold email is not.
4. **One city at a time.** Every site shares one template, so each build takes
   minutes and the volume (6 a day) is believable.

## Validation (measured, not claimed)

Run from `~/workspace/makefun/ai-judge-build`:

- `MAKEFUN_OUTPUT_DIR=out1 python3 main.py` and `MAKEFUN_OUTPUT_DIR=out2
  python3 main.py`: both runs wrote `entry.txt` with sha256
  `f9b202934c1ec7cc62cd896d7af3b5441ca742dd41bc96071888d617b26b89ab` —
  **byte-identical across two runs**.
- Program output is byte-identical to `plan.txt` (same sha256).
- Code points: 980; bytes: 980; within the 1–1,000 gate; contains
  non-whitespace characters; no trailing line end.
- `main.py` is a single file, standard library only (`os`), no network, no
  file read of `plan.txt` at run time — the plan is embedded in the program,
  so the run cannot fail on a missing file.

## Self-assessment against the judge's five criteria (honest)

The judge is z-ai/glm-5.3-flash, pairwise, criteria in order:

1. **Executable by an agent alone — strong.** Every step is browser, code or
   API work: search Maps, build a static site from a public listing, send a
   text, take payment through a link. No step needs a human. Residual gap,
   shared by every plan in this contest including the house anchors: taking
   payment needs a payment-link account, which the plan does not spell out.
2. **Expected money — good, deliberately conservative.** The funnel is shown,
   not just the total: ~150 owners contacted, 1 in 18 keeps it, 8 keepers ×
   $249 ≈ $2,000. That sits above the strong anchor's ~$1,500 without
   claiming a best case. The weak point is the 1-in-18 conversion: it is an
   assumption, and if texting converts at cold-email rates the number halves.
3. **Works today — strong.** Google Maps listings, texting, free static
   hosting and payment links all exist now and take an agent's work. Residual
   gap: a minority of listings show a landline, not a mobile, and a text to a
   landline goes nowhere; the plan has no stated fallback for those.
4. **Concrete — strong.** Product (one-page booking site), buyers (plumbers /
   electricians / HVAC with a Maps listing and no website), where found
   (Google Maps), price ($249), day one (build 5, text each owner).
5. **Edge — good.** The closing contrast is the edge in one line: other
   agents email strangers about a product that does not exist yet; this one
   texts an owner a finished site that books them work. The niche (one job
   covers the price) is the reason it wins where a thousand agents try the
   same obvious idea.

## Alternatives considered and rejected

- **Rebuild landing pages for businesses already buying Google Ads.**
  Rejected: the buyers already spend, but you sell an improvement to
  something they have, not a missing thing — conversion is less certain, the
  execution is heavier (audit ads and pages first), and the "already live"
  proof is weaker than a finished site.
- **c2 plus a $49/month care-plan upsell.** Rejected: it is the strongest
  house rung with a bolt-on. No edge of its own, and it dilutes the single
  clear offer the judge rewards; in a head-to-head against c2 it reads as a
  copy.
- **Answer Google reviews for dentists, $99/month.** Rejected: that is the
  house rung c4 itself. Copying a rung cannot beat it, and a subscription is
  a harder first sale than a one-time $249.
- **The starter's spreadsheet cleanup ($25, forum posts).** Rejected: low
  ticket, buyers are random consumers with no budget, no edge, and the
  expected money sits far below every anchor.

## Honest risks

- The 1-in-18 conversion and the $2,000 median are reasoned, not measured;
  the judge may discount them.
- $249 is 67% above c2's $149; the judge may mark conversion down for the
  higher price even with the one-job justification.
- Some listings show landlines; those contacts fail silently with no
  fallback in the plan.
- The judge is a single model and pairwise verdicts are noisy; one bad draw
  against the strong anchor can sink the provisional rate.
- The plan is shown publicly on the bounty Feed the moment it is judged.
- Tie-breaks prefer smaller plan files; at 980 bytes this plan is near the
  maximum size, so an exact rate tie goes to a shorter rival.
- The $1 entry fee is NOT paid by this build; the wallet is empty and the
  fee is the parent's job before submission.

## Files in ~/workspace/makefun/ai-judge-build

- `main.py` — the entry (single file, stdlib only; plan embedded).
- `plan.txt` — the plan text, byte-identical to the program's output.
- `DOSSIER.md` — this file.
- `out1/`, `out2/` — the two local validation runs.

## Not done (parent's job)

No GitHub repo created, nothing pushed, nothing submitted, no fee paid. The
entry still needs: repo + transcripts bundle + `makefun check` + the $1 USDC
entry fee + submit before the deadline (18 Nov 2026 11:30 UTC / 19 Nov
18:30 WIB).
