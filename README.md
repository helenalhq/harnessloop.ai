# HarnessLoop

A bilingual, static business website. Chinese routes use `/`; English routes use `/en/`. The canonical production origin is **https://harnessloop.ai**. All demonstrations are synthetic, not customer results or live AI runs.

## Build and test

Requires Node.js and Python 3. No npm runtime packages or environment secrets are required.

```sh
npm run build             # local default: noindex preview
npm test                  # route, interaction, motion and release-policy tests
npm run build:production  # explicit local production build
```

`build.py`, `en_content.py`, `refine.py`, and `release.py` generate the HTML. CSS and browser JavaScript sources live in `dist/assets`; do not delete that directory before building. Serve `dist` with any static HTTP server, not `file://`.

### Indexing boundaries

- When `VERCEL_ENV` exists, it is authoritative. Only `VERCEL_ENV=production` enables indexing.
- Vercel Preview and Development builds stay `noindex,nofollow` with `robots.txt: Disallow: /`, even if `SITE_ENV=production` is set.
- Outside Vercel, default is private-preview indexing policy. `SITE_ENV=production` is an explicit local override.
- Committed `dist` is the preview build. Vercel must execute the configured build command; do not skip it and serve committed HTML directly.
- Production has canonical URLs, reciprocal Chinese/English hreflang, sitemap, Open Graph and Twitter summary metadata. A sitemap does not guarantee indexing.

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
- Language preference is the only application local-storage item.
- Motion has pause, manual steps, reduced-motion support and visibility suspension. The mobile menu closes with Escape or an outside click.
- A static explanatory fallback is supplied when JavaScript is unavailable.

## Release verification (2026-11-12)

Automated checks: 14 locale routes, local links/assets, bilingual content, safe plain-text brief generation, email parameter encoding, language choices, five-stage state machine, reduced motion, no native form fallback, four environment-policy combinations, canonical/hreflang/share metadata, 14 sitemap entries and 404. JavaScript syntax checks pass.

Not proven by local tests: Vercel's actual HTTP routing/build environment, production TLS, DNS propagation, final mobile rendering, browser console, screen-reader behavior, mail application behavior or receipt at `contact@harnessloop.ai`. Verify these against the deployed preview/production artifact before announcing the launch.

The privacy text describes the implemented website and user-initiated email flow. It does not invent a legal entity, a retention period or compliance certification. The operator must confirm any legally required identity/contact disclosures and actual business data-handling obligations before launch. Email MX records alone do not prove the specific mailbox exists or receives mail.

## SEO/GEO update (2026-11-15)
Stable language URLs, bilingual visible FAQ with matching JSON-LD, Organization/WebSite/WebPage entities and a local social preview image. No automatic locale redirection. No claims of guaranteed search ranking, AI citations or FAQ rich results.
