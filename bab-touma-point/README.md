# Bab Touma Point website

One-page bilingual (English / Arabic) site for the Bab Touma Point visitor kiosk, Old City, Damascus. Plain HTML, no build step, works on GitHub Pages.

## Before going live: edit one block

Open `index.html` and find `const CONFIG` near the bottom:

| Setting | What to put |
| --- | --- |
| `whatsapp` | The kiosk's WhatsApp Business number, country code first, digits only (e.g. `9639XXXXXXXX`) |
| `hours`, `hoursAr` | Opening hours in English and Arabic |
| `lat`, `lon` | The kiosk's exact position (long-press it in Google Maps to copy the coordinates) |
| `mapsQuery` | Change to `Bab Touma Point` once the Google Maps listing is approved |

Also replace `+963000000000` and the coordinates in the `application/ld+json` block in the page head so search engines get the same details.

## Publishing on GitHub Pages

- **Separate repo** (recommended, e.g. `bab-touma-point`): put these files at the repo root, then Settings → Pages → Deploy from branch `main`, folder `/ (root)`. The site appears at `https://michael-a-riley.github.io/bab-touma-point/`.
- **Inside `michael-a-riley.github.io`**: keep this folder as `bab-touma-point/`. Same address.

A custom domain (for example `babtoumapoint.com`) can be added later under Settings → Pages.

## Content rules

- The kiosk refers visitors to licensed partners; the site must not present it as a government office or as selling tours itself.
- Show prices only once partners have confirmed them; until then the site says "Ask for today's price".
- No em dashes in copy.
