# Money Snowball ❄️

A playful, single-page dashboard that teaches children the **power of compounding** —
built to teach my own two kids (7 and 11) and shareable with friends to teach theirs.
One link, works on any phone.

Live URL (once deployed): `https://phuazz.github.io/money-snowball/`

## The idea

The teaching engine is **predict-then-reveal shock**: make the child *guess*, then show
a number far bigger than they imagined. A child who is told a fact forgets it; a child
who is **wrong** remembers. Every major concept is built as a guess followed by a
reveal, in **kid money** (pocket money, birthday money, "how many ice creams").

An age toggle (**Younger ≈7 / Older ≈11**) adjusts vocabulary, number sizes, and
whether the Rule-of-72 formula and the grown-up calculator are shown. One page serves a
range of ages.

### Design principle: every quantity must be one a child can feel

The examples are chosen so that **both sides of every comparison are comprehensible**.
A 7-year-old cannot distinguish $1,000,000 from $5,000,000 — both are "infinity
dollars" — so a hook built on that comparison surprises nobody. $10 a day is a number
they can feel; $300 is a fortune. That is why the hook races pocket money against the
doubling coin rather than a million dollars.

## What it teaches (the journey)

0. **Would You Rather?** — $10 a day for a month ($300) vs a 1-cent coin that doubles
   daily ($5,368,709). Run as an animated **race**: the coin *loses for the first 14
   days* and only takes the lead on day 15. That is the real lesson — compounding looks
   like a failure right until it does not, which is exactly when people quit.
1. **The Snowball** — two kids, both $100 at 20%. The squirrel keeps the profit and
   reaches $891 in 12 years; the ice-cream kid eats it and is on $100 for ever. Raced
   side by side so the gap is watched, not read.
2. **The Doubling Machine (Rule of 72)** — 72 ÷ growth rate ≈ years to double. Plus the
   reframe that makes it feel achievable: only **20** doublings turn 1 into a million,
   30 into a billion. Older mode gets the paper-folding experiment (42 folds passes the
   Moon; nobody manages more than ~7).
3. **Grow Your Money** — a kid calculator: save $X/week, pick a growth rate (piggy bank
   0% / bank 2% / index fund 10% / super-investor 20%), guess, then reveal. Splits the
   result into "you put in" vs "your snowball made", and answers the question that makes
   it tangible: to reach the same total in a piggy bank you would need to save ~40× more
   each week. **The guess adapts to age**: Younger taps one of four options (no keyboard,
   nothing to freeze at — a blank box gets skipped, and a skipped guess kills the reveal);
   Older types a number, which is a firmer commitment than picking from a list.
4. **Early Bird vs Late Bird** — Amy saves from 8 to 18 then stops; Ben saves from 25 to
   60. Amy ends with **$249,619** against Ben's **$77,513**, having put in 3.5× less.
   Starting early beats saving more.
5. **Where does ~10% come from?** — a gentle, honest intro to owning pieces of great
   companies, including the part where markets fall by half and it feels horrible.
6. **The Sneaky Thief 🥷 (inflation)** — the answer to the obvious rebuttal Step 5 invites
   ("fine, I will keep it under my bed"). Prices the piggy bank in **ice creams**: $100
   still says $100, but buys **33 cones today and 18 in twenty years** — 45% of its power
   gone, with the lost cones greying out where they stood. The same $100 invested buys
   **124**. Punchline: your money did not shrink, the price grew — which is why nobody
   ever sends you a bill. Older mode lands the callback: at 3%, prices double every
   **72 ÷ 3 = 24 years**. The Rule of 72 also works *against* you.
7. **Grown-Up Mode + Parent Guide** — the same maths on a grown-up salary: income →
   net-worth model (milestone table + linear/log chart), plus discussion prompts for
   parents, including the sweets-on-the-table version that needs no screen and the
   "ask a grandparent what noodles cost" question.

## Status

- **2026-07-17** — Readability pass: chart text was rendering at ~4px on a phone (viewBox
  scaling) and is now sized from the measured scale; money inputs comma-grouped; kid-facing
  captions bumped off the 13px adult-dashboard size. 30 self-checks pass in-browser.
- **2026-07-17** — Guess input now age-appropriate: tap-one-of-four in Younger, typed
  number in Older.
- **2026-07-17** — Added Step 6 (inflation, priced in ice creams): the cost of *not*
  investing. 8 steps. Mobile clean.
- **2026-07-17** — Examples reworked so every quantity is one a child can feel (see the
  design principle above), and the page now stands on its own with no third-party
  credit. Mobile clean (no overflow, all tap targets ≥44px). Self-contained: no failed
  requests, no `data/`.
- **2026-07-16** — All seven steps built and verified. Deployed public + hub-listed.

## Concepts / maths

- Compounding: `FV = lump·(1+r)ⁿ + saving · ((1+r)ⁿ − 1)/r` (end-of-year annuity).
- Rule of 72 is taught honestly as an *estimate* (exact doubling = ln2 / ln(1+r); at
  20% the exact figure is ≈3.8 years, not 3.6).
- Penny doubling: day 30 = $0.01 × 2²⁹ = $5,368,709.12.
- The grown-up model is the standard growing-contribution one: income grows each year and
  the invested slice goes in at the **end** of each year, so `v = v·(1+r) + contribution`.
  Self-checks pin it to reference values for those inputs (start 35, income 84,000,
  +5%/yr, invest 20% → 0%: 16,800 then 34,440; 2%: 34,776; 20%: 37,800) and to milestone
  ages (start 21 at 10% → $1m at 44, $10m at 65, $100m at 88; at 20% → $1m at 37, $10m at
  49; start 35 at 20% → $1m at 48, $100m at 72). Do not "fix" the engine without re-running them.
- Step 0 race: the coin passes $10/day on **day 15** and finishes 17,896× ahead
  ($5,368,709 vs $300). The chart's y-axis deliberately rescales itself each frame — the
  rescaling is what conveys the explosion.
- Step 6 inflation: $3 cone at 3%/yr, invested at 10% (kept consistent with the ~10% rung
  in Step 5, so nominal is compared with nominal). After 20 years a cone is $5.42, so $100
  buys 18 cones against 33 at the start, while $100 invested buys 124. All pinned by
  self-checks.
- **Chart text is sized from the measured scale, not a declared px** (`paintChart`). SVG text
  inside a `viewBox` is in user units, so the container rescales it: a "9px" axis label rendered
  at **3.8px** on a phone (620-unit box at 264px = 0.425× scale), and the 10px label carrying the
  payoff number at 4.3px. Charts repaint on tab-show and debounced `resize` because a hidden tab
  measures `clientWidth === 0`. See `design.md`.
- **Money inputs are `type="text" inputmode="numeric"`, grouped on blur** — `type="number"` cannot
  hold a comma (the spec requires a valid float, so the browser discards it). Read them with
  `numOf()`; `+"42,000"` is `NaN`. See `design.md`.
- **Guess options (`kcOptionSet`) vary their decoy recipe with the inputs.** A fixed recipe
  puts the truth in the same slot every time, so "always pick the biggest" becomes a winning
  strategy and the child stops thinking. The recipe is seeded from the inputs — stable while
  a slider is dragged, different across setups — and a self-check asserts the biggest option
  is not always right.
- **Put `.younger-only` / `.older-only` on a WRAPPER, never on an element that has its own
  `display`.** `.guessrow{display:flex}` and `.older-only{display:none}` are both single-class
  (0,1,0), so the later rule in the sheet silently wins: the typing row showed in Younger mode
  *and* rendered as `block` instead of `flex` in Older. Neither was visible in the diff.
- **`selfTest()` must be called from init at the bottom, never as an IIFE at the top.** It
  references `const`s declared further down (`conePrice`, `grownUpSeries`); touching a
  `const` before its initialiser runs throws a TDZ `ReferenceError` that aborts the whole
  script and serves a blank page. This shipped-broken once and was caught only by driving
  the page, not by reading it.
- **Step 2 trap avoided:** the "$1 becomes…" figure uses real compounding, never
  `2^(rule-of-72 doublings)` — that shortcut overstates by 25% at 20% ($16,384 against a
  true $13,105) and understates at 10% ($128 against $142). Guarded by a self-check.
- The Step 5 market chart is a **stylised illustration, labelled as such** — not real
  index data. The only history claim ("roughly 10% a year over decades") is deliberately
  imprecise and flagged as history rather than a forecast: a borrowed decimal figure
  would imply a source the page no longer carries.

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

## On the material

Everything taught here is long-standing, universal finance pedagogy, independently
implemented: compound interest, the **Rule of 72** (in print since at least Pacioli,
1494), the **doubling-penny** choice, the **snowball** metaphor (Warren Buffett's own),
**early-bird vs late-bird**, and a plain growing-contribution savings model that any
planner would write the same way. No third party's proprietary material, personal
story, or track record appears on the page.

*Personal / educational project. Not investment advice.*
