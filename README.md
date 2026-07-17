# Money Snowball ❄️

A playful, single-page dashboard that teaches children the **power of compounding** —
built to teach my own two kids (7 and 11) and shareable with friends to teach theirs.
One link, works on any phone.

Live URL (once deployed): `https://phuazz.github.io/money-snowball/`

## The idea

Inspired by Adam Khoo's "Power of Compounding" video
(https://youtu.be/3qPLIYiejas). His real teaching engine is **predict-then-reveal
shock** — he made his daughters *guess*, then showed a number far bigger than they
imagined, and that surprise is what motivated them to start investing. Money Snowball
keeps that surprise as its spine and reframes his adult income → net-worth model into
**kid money** (pocket money, birthday money, "how many ice creams / Lego sets").

An age toggle (**Younger ≈7 / Older ≈11**) adjusts vocabulary, number sizes, and
whether the Rule-of-72 formula and the grown-up calculator are shown. One page serves a
range of ages.

## What it teaches (the journey)

0. **Would You Rather?** — $1,000,000 now vs a magic 1-cent coin that doubles every day
   for 30 days (reveal: the coin becomes $5,368,709). Doubling is magic.
1. **The Snowball** — you earn money on your money, then on *that* money too. Spend the
   profit and the snowball stops.
2. **The Doubling Machine (Rule of 72)** — 72 ÷ growth rate ≈ years to double.
3. **Grow Your Money** — a kid calculator: save $X/week, pick a growth rate (piggy bank
   0% / bank 2% / index fund 10% / super-investor 20%), guess, then reveal. Splits the
   result into "you put in" vs "your snowball made".
4. **Early Bird vs Late Bird** — Amy saves from 8 to 18 then stops; Ben saves from 25 to
   60. Amy ends with **$249,619** against Ben's **$77,513**, having put in 3.5× less.
   Starting early beats saving more.
5. **Where does ~10% come from?** — a gentle, honest intro to owning pieces of great
   companies, including the part where markets fall by half and it feels horrible.
6. **Grown-Up Mode + Parent Guide** — Adam's fuller income → net-worth model (milestone
   table + linear/log chart), plus discussion prompts for parents.

## Status

- **2026-07-16** — All seven steps built and verified in-browser. 20 self-checks pass,
  including 11 that pin the grown-up engine to Adam's published figures. Mobile clean
  (no overflow, all tap targets ≥44px). Self-contained: no failed requests, no `data/`.

## Concepts / maths

- Compounding: `FV = lump·(1+r)ⁿ + saving · ((1+r)ⁿ − 1)/r` (end-of-year annuity).
- Rule of 72 is taught honestly as an *estimate* (exact doubling = ln2 / ln(1+r); at
  20% the exact figure is ≈3.8 years, not 3.6).
- Penny doubling: day 30 = $0.01 × 2²⁹ = $5,368,709.12.
- The grown-up model follows Adam's spreadsheet exactly: income grows each year and the
  invested slice goes in at the **end** of each year, so `v = v·(1+r) + contribution`.
  It is pinned by self-checks reproducing his published cells (start 35, income 84,000,
  +5%/yr, invest 20% → 0%: 16,800 then 34,440; 2%: 34,776; 20%: 37,800) and every
  milestone he states (start 21 at 10% → $1m at 44, $10m at 65, $100m at 88; at 20% →
  $1m at 37, $10m at 49; start 35 at 20% → $1m at 48, $100m at 72).
- **Step 2 trap avoided:** the "$1 becomes…" figure uses real compounding, never
  `2^(rule-of-72 doublings)` — that shortcut overstates by 25% at 20% ($16,384 against a
  true $13,105) and understates at 10% ($128 against $142). Guarded by a self-check.
- The Step 5 market chart is a **stylised illustration, labelled as such** — not real
  index data. The only cited history (≈10.9%/yr) is attributed to Adam and flagged as
  history, not a forecast.

## Architecture

Pure client-side maths — **no `data/` directory**. Self-contained `template.html`
(emoji illustrations, CSS/SVG animations, no external image assets).

**Deviation from house style, on purpose:** every chart is hand-rolled SVG
(`drawChart()`, ~30 lines, log-scale capable) rather than Plotly. The plan called for
Plotly on the grown-up linear/log chart, but pulling a ~1MB CDN library onto a page
whose whole point is to open instantly on a friend's phone was the wrong trade — and it
would have been the page's only external dependency, costing offline capability. Styling
still follows `design.md` (tokens, type, semantic colours). Revisit if the charts ever
need real interactivity.

```
money-snowball/
├── template.html        # source (edit this)
├── scripts/pipeline.py  # copies template.html -> docs/index.html + build stamp
├── scripts/make_og.py   # builds docs/og.png + docs/icon-180.png (rarely needs re-running)
├── docs/index.html      # GitHub Pages output
├── docs/og.png          # 1200x630 link-preview card
├── docs/icon-180.png    # apple-touch-icon
└── README.md
```

Build: `python scripts/pipeline.py`. Local dev: `npx serve .` and open `template.html`.

### Sharing

The whole point is that a parent can send this to another parent, so the link has to look
like something worth opening:

- `og:*` / `twitter:*` tags give WhatsApp, Telegram and iMessage a real preview card.
  **`og:image` must be an absolute URL to a raster file** — crawlers do not resolve
  relative paths and will not render an SVG or a data URI.
- `docs/og.png` is generated by `scripts/make_og.py` (PIL, Georgia — the house serif
  fallback, colours from `design.md`). Re-run it only if the card design changes.
- The favicon is an inline SVG data URI (no file, no request); `icon-180.png` covers iOS
  home-screen saves.
- The parent section has a share button: native share sheet on phones via
  `navigator.share`, falling back to clipboard, falling back to selecting the URL.

Note: relative asset paths assume the page is served from a directory URL with a trailing
slash (as GitHub Pages does). Serving `docs` without the trailing slash locally will 404
the icon — harmless, and not how it is deployed.

## Credit

Concept and the original Excel model: **Adam Khoo**, "Power of Compounding"
(https://youtu.be/3qPLIYiejas). This is an independent educational reinterpretation for
children; no affiliation.

*Personal / educational project. Not investment advice.*
