# A working ai-judge-rich-01 entry (Python 3.13, standard library only): it writes one
# fixed plan, the plan an AI agent would follow to turn $100, a computer with internet
# access and 30 days into the most money, to /output/entry.txt. The plan is the entry:
# a booking-site service for home-service pros, built before asking and sold by text.
#
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white space, and
# the judge reads exactly the bytes written, line ends included, so write no line end
# you do not mean to show. This plan is 980 characters, no trailing line end. The
# program runs twice with no network, and both runs must write the same bytes.
#
# Start your agent's session at or after the contest opens and build the entry in it: a
# session begun before the opening cannot be entered (the transcript gate's
# thinking_in_window).
#
# To enter it, put this file at the root of your repository as main.py, with no main.ts
# beside it: a repository with both at its root is refused.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with nothing
# installed. -P keeps the script's own directory (/bot) off sys.path, so `import helpers`
# does NOT find a helpers.py beside main.py; -s keeps the user site-packages off it, so
# nothing pip installed is importable. Only the standard library imports. This file
# keeps everything in itself.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell booking sites to home-service pros who take jobs by phone.",
        "Find plumbers, electricians and HVAC firms on Google Maps with a listing but no website, working one city at a time so every site shares one template.",
        "Build each one a live one-page booking site from their own listing: services, area, hours, reviews, tap-to-call and a quote form that texts them the lead.",
        "Day 1: build 5 and text each owner the link. Then build 6 a day and text every owner the same day; owners who do not answer get one reminder with a screenshot of their site.",
        "The site is already live before you ask for anything; they pay $249 once to keep it under their name, and one booked job covers that.",
        "Spend the $100 on a texting number and hosting; host the demos free.",
        "By day 30 you will have contacted about 150 owners; if 1 in 18 keeps it, that is 8 keepers and about $2,000.",
        "Most agents email strangers about a product that does not exist yet; you text an owner a finished site that books them work.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
