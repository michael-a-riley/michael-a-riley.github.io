# Bab Touma Point website

Site for the Bab Touma Point visitor kiosk, Old City, Damascus. Plain HTML, no build step, works on GitHub Pages.

- `content.py`: all text, prices and partners in Arabic (light Shami) and English. Edit this.
- `build.py`: run `python3 build.py` to regenerate every page (Arabic at the root, English under `en/`).
- `style.css`: shared styles. `site.js` is generated.

Do not edit the generated `index.html` files by hand; they are overwritten on the next build.

## Before going live: edit one block

Open `content.py` and edit the `SITE` block at the top, then run `python3 build.py`:

| Setting | What to put |
| --- | --- |
| `whatsapp` | The kiosk's WhatsApp Business number, country code first, digits only (e.g. `9639XXXXXXXX`) |
| `lat`, `lon` | The kiosk's exact position (long-press it in Google Maps to copy the coordinates) |
| `mapsQuery` | Change to `Bab Touma Point` once the Google Maps listing is approved |

Prices on the site are mockup figures marked as indicative; replace them in `content.py` once partners confirm, and remove the `mock` notice in `build.py` when the site goes live.

## Publishing on GitHub Pages

- **Separate repo** (recommended, e.g. `bab-touma-point`): put these files at the repo root, then Settings → Pages → Deploy from branch `main`, folder `/ (root)`. The site appears at `https://michael-a-riley.github.io/bab-touma-point/`.
- **Inside `michael-a-riley.github.io`**: keep this folder as `bab-touma-point/`. Same address.

A custom domain (for example `babtoumapoint.com`) can be added later under Settings → Pages.

## Content rules

- The kiosk refers visitors to licensed partners; the site must not present it as a government office or as selling tours itself.
- Show prices only once partners have confirmed them; until then the site says "Ask for today's price".
- No em dashes in copy.
