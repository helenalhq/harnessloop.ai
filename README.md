# HarnessLoop

A bilingual, static business website. Chinese lives at `/zh/` (home) with root-level subpages; English lives under `/en/`. In production the apex path `/` redirects to `/en/`; language switches use stable URLs, never browser sniffing. The canonical production origin is **https://harnessloop.ai**. All demonstrations are synthetic, not customer results or live AI runs.

## Build and test

Requires Node.js and Python 3. No npm runtime packages or environment secrets are required.

```sh
npm run build             # local default: noindex preview
npm test                  # routes, demo, motion, release policy, SEO and source registry
npm run build:production  # explicit local production build
```

`build.py` renders the shared template; `en_content.py` holds English copy. Pages are assembled in this order: `refine.py` (structure), `seo.py` (FAQ, metadata, structured data), `solutions.py` and `demo.py` (the examples and the interactive brief demo), `business.py` (home and contact bodies), `release.py` (privacy text, contact brief, indexing policy). There are 9 pages per language: home, demo, solutions, how-it-works, data-factory, research, contact, privacy and FAQ. CSS and browser JavaScript sources live in `dist/assets`; do not delete that directory before building. Serve `dist` with any static HTTP server, not `file://`.

### Indexing boundaries

- When `VERCEL_ENV` exists, it is authoritative. Only `VERCEL_ENV=production` enables indexing.
- Vercel Preview and Development builds stay `noindex,nofollow` with `robots.txt: Disallow: /`, even if `SITE_ENV=production` is set.
- Outside Vercel, default is private-preview indexing policy. `SITE_ENV=production` is an explicit local override.
- Committed `dist` is the preview build. Vercel must execute the configured build command; do not skip it and serve committed HTML directly.
- Production has canonical URLs, reciprocal Chinese/English hreflang, sitemap, Open Graph and Twitter summary metadata. A sitemap does not guarantee indexing.

### Figures and sources

`sources.py` is the only registry for regulatory figures and official links used on the site (ISF timing and penalty, FMC detention and demurrage billing, 19 U.S.C. § 1592, China customs late-declaration fee). Each entry records the issuing body, URL, figure, last verification date and the next quarterly review.

- A page may quote a figure only with its source link next to it.
- `source-tests.py` fails when a body contains an unregistered external link, a retired figure or a promotional pattern such as "guarantee compliance" or "up to N%".
- The test prints the next review date. When it is due, re-open each official page, update `checked`, and update or remove the figure if the text has changed. Some official sites block automated fetches; that re-check is a manual task.

## Deploy to Vercel

Import the repository with:

- Framework preset: **Other**
- Root directory: **repository root (`./`)**, not `harnessloop-web`
- Build command: **`npm run build`** (also declared in `vercel.json`)
- Output directory: **`dist`** (also declared in `vercel.json`)
- No application secrets or API credentials.

Vercel's build environment must provide Python 3. Verify the actual build log and fail rather than deploying stale generated files if the command fails. `vercel.json` provides a 308-style permanent host redirect from `www.harnessloop.ai` to the apex domain and conservative security headers. Configure both domains in Vercel and use the DNS targets shown by that specific project. Preserve mail MX and TXT records. No DNS change or deployment is performed by this repository.

## Privacy and interaction

- The brief tool is a non-submitting control group, not an HTML form. With JavaScript disabled, its input cannot become a native GET submission or URL query.
- JavaScript validates inputs and generates plain text locally; copy and mailto are user actions. Mailto opens a draft, never automatically sends it.
- CSP additionally disallows form submissions and network connections from scripts. There are no analytics, remote fonts, third-party browser scripts or uploads.
- The site stores nothing in browser storage: no cookies, no local storage. Language is chosen through stable URLs and the header link; in-site links keep the chosen language.
- The home-page walkthrough video (`demo-55s-en/zh.mp4`, release assets of the `helenalhq/media` repository) is not downloaded until the visitor presses play; a local poster shows first. With JavaScript the poster gets our own play button (`video.js`); without it the browser's controls remain. If GitHub does not answer, a line below the player links to the release. CSP `media-src` allows GitHub only for that element. The media repository and its `v1.0` release must stay public, and `source-tests.py` requires the release link to be registered in `sources.py`.
- Motion has pause, manual steps, reduced-motion support and visibility suspension. Cards fade in once on scroll (`motion.js`), only when the visitor has not asked for reduced motion; everything is visible without JavaScript and in print. The mobile menu closes with Escape or an outside click.
- Typography is self-hosted: Instrument Sans (SIL Open Font License, see `dist/assets/fonts/`).
- A static explanatory fallback is supplied when JavaScript is unavailable.

## Release verification (2026-11-26)

Automated checks: 18 locale routes, local links/assets, bilingual content, safe plain-text brief generation, email parameter encoding, language choices, five-stage state machine, reduced motion, no native form fallback, four environment-policy combinations, canonical/hreflang/share metadata with titles that match across tab, social preview and structured data, 18 sitemap entries (16 in preview), 404, and the source registry above. The demo's headline counts (6 items, 3 anomalies, 1 draft) are checked against its rows.

Not proven by local tests: Vercel's actual HTTP routing/build environment, production TLS, DNS propagation, final mobile rendering, browser console, screen-reader behavior, mail application behavior or receipt at `contact@harnessloop.ai`. Verify these against the deployed preview/production artifact before announcing the launch.

The privacy text describes the implemented website and user-initiated email flow. It does not invent a legal entity, a retention period or compliance certification. The operator must confirm any legally required identity/contact disclosures and actual business data-handling obligations before launch. Email MX records alone do not prove the specific mailbox exists or receives mail.

## SEO/GEO update (2026-11-15)
Stable language URLs, bilingual visible FAQ with matching JSON-LD, Organization/WebSite/WebPage entities and a local social preview image. No automatic locale redirection. No claims of guaranteed search ranking, AI citations or FAQ rich results.

## Review (2026-11-26)

Page titles name the page's subject rather than only its nav label. The demo states its counts consistently and no longer suggests that static rows expand. On narrow screens the audit table stacks into cards and the statistics row keeps three columns. Legacy home-page code was removed. Not done yet: a real lead-capture form (the brief is still generated locally and sent by the visitor) and A/B tests on the calls to action.
