# Bab Touma Point website

Site for the Bab Touma Point visitor kiosk, Old City, Damascus. Plain HTML, no build step, works on GitHub Pages.

- `index.html`: Arabic (main page), written in a light Shami register any Arabic speaker can follow
- `en/index.html`: English
- `style.css`, `site.js`: shared by both pages

## Before going live: edit one block

Open `site.js` and edit `const CONFIG` at the top (both pages update):

| Setting | What to put |
| --- | --- |
| `whatsapp` | The kiosk's WhatsApp Business number, country code first, digits only (e.g. `9639XXXXXXXX`) |
| `lat`, `lon` | The kiosk's exact position (long-press it in Google Maps to copy the coordinates) |
| `mapsQuery` | Change to `Bab Touma Point` once the Google Maps listing is approved |

Opening hours are written in each page's text. If the phone number or hours change, also update the `application/ld+json` block in the head of both pages so search engines get the same details.

## Publishing on GitHub Pages

- **Separate repo** (recommended, e.g. `bab-touma-point`): put these files at the repo root, then Settings → Pages → Deploy from branch `main`, folder `/ (root)`. The site appears at `https://michael-a-riley.github.io/bab-touma-point/`.
- **Inside `michael-a-riley.github.io`**: keep this folder as `bab-touma-point/`. Same address.

A custom domain (for example `babtoumapoint.com`) can be added later under Settings → Pages.

## Content rules

- The kiosk refers visitors to licensed partners; the site must not present it as a government office or as selling tours itself.
- Show prices only once partners have confirmed them; until then the site says "Ask for today's price".
- No em dashes in copy.
