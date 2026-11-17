# Make the AI judge rich

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/xJPtea/ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/xJPtea/ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

Entry for the [make.fun bounty ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01): a program that writes one short plan to `/output/entry.txt` — the plan an AI agent would follow, starting with $100, a computer with internet access and 30 days, to end the 30 days with the most money.

## The plan

Sell booking sites to home-service pros who take jobs by phone. Find plumbers, electricians and HVAC firms on Google Maps with a listing but no website, one city at a time. Build each one a live one-page booking site from their own listing, text the owner the link, and charge $249 once to keep it. See `plan.txt` for the full 980-character plan.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program is deterministic: two runs write byte-identical output.
