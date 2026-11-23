# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/surab-max/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/surab-max/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

**Monday 23 November 2026 — the world in one day, in one image.** A newspaper front page drawn entirely in code: COP31 collapsing in Antalya without a major deal as the lead, Russian strikes killing 11 in the Kyiv region as a residential block collapses, suspected Ukrainian sea drones hitting a Russian warship at Benghazi, Democrats clinching at least 258 House seats — their largest majority since 1992 — and the search for 34 workers missing after an Indonesian candy-factory fire, with a Gaza aid-call brief (Australia, Canada, Italy and the UK urge Israel to open crossings as flooding worsens suffering) and a ticker carrying South Sudan, the Congo Ebola response, sliding Asia markets, the UK's 2035 Women's World Cup hosting and Liverpool's win over 10-man Manchester United. Every story is a verified event of 23 November 2026; `SOURCES.md` lists each one with the outlets that reported it. The image is a 1024×1024 PNG inside the competition's 1 MiB / 1024 px caps, and its masthead names the day it sums up.

**How it is built.** `tools/generate.py` renders the front page with Pillow (dated masthead, lead panel, four story panels, Gaza brief, ticker) and writes `entry.png`. The graded program, `main.py` (Python 3.13, standard library only), copies `entry.png` to `/output/entry.png`, verifying the PNG's dimensions against the competition caps and the copy's SHA-256 against the source, so both grader runs produce byte-identical output with no network.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# then view out/entry.png — the front page of 23 November 2026
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ys1ka8r4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
