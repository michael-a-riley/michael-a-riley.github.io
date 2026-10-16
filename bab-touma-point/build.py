# -*- coding: utf-8 -*-
"""Builds the static site from content.py. Run: python3 build.py
Outputs Arabic pages at the root and English pages under en/."""
import os, html, json
from content import *

ROOT = os.path.dirname(os.path.abspath(__file__))
ICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath d='M8 60V30a24 24 0 0 1 48 0v30z' fill='%23262422'/%3E%3Ccircle cx='32' cy='26' r='4' fill='%23E8892B'/%3E%3Crect x='29' y='34' width='6' height='18' rx='2' fill='%23E8892B'/%3E%3C/svg%3E"
WA_SVG = "<svg viewBox='0 0 24 24' aria-hidden='true'><path fill='currentColor' d='M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.2s1 2.6 1.1 2.7c.1.2 1.9 2.9 4.6 4 1.7.7 2.4.8 3.2.7.5-.1 1.5-.6 1.8-1.2.2-.6.2-1.1.1-1.2l-.4-.2z'/></svg>"
MARK = "<svg class='mark' viewBox='0 0 44 54' aria-hidden='true'><path d='M2 54V22a20 20 0 0 1 40 0v32' fill='none' stroke='#262422' stroke-width='3'/><circle cx='22' cy='20' r='3.5' fill='#E8892B'/><rect x='19.5' y='28' width='5' height='18' rx='2' fill='#E8892B'/></svg>"

def e(s): return html.escape(s, quote=True)

class Page:
    def __init__(self, lang, path):
        self.lang, self.path = lang, path          # path like "" or "walks/" or "walks/umayyad-classic/"
        self.depth = path.count("/") + (1 if lang == "en" else 0)
        self.rel = "../" * self.depth              # to site root
    def t(self, d): return d[self.lang]
    def url(self, path=""):                         # site-relative link to another page
        pre = "en/" if self.lang == "en" else ""
        return self.rel + pre + path
    def other(self):
        return (self.rel + self.path) if self.lang == "en" else (self.rel + "en/" + self.path)

def shell(p, title, desc, body, item=None):
    L = p.lang; T = p.t
    nav = "".join(f"<a href='{p.url(s + '/')}'{' aria-current=page' if p.path.startswith(s + '/') else ''}>{e(T(n))}</a>" for s, n in NAV)
    canonical_ar = SITE["base"] + p.path; canonical_en = SITE["base"] + "en/" + p.path
    ld = {"@context": "https://schema.org", "@type": "TouristInformationCenter", "name": T(SITE["name"]),
          "address": {"@type": "PostalAddress", "streetAddress": "Bab Touma Square", "addressLocality": "Damascus", "addressCountry": "SY"},
          "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lon"]},
          "telephone": "+" + SITE["whatsapp"], "openingHours": "Mo-Su 08:00-23:00"}
    book_text = json.dumps(T(UI["book"]))
    return f"""<!doctype html>
<html lang="{L}" dir="{'rtl' if L == 'ar' else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#262422">
<link rel="alternate" hreflang="ar" href="{canonical_ar}">
<link rel="alternate" hreflang="en" href="{canonical_en}">
<link rel="alternate" hreflang="x-default" href="{canonical_ar}">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600&family=Reem+Kufi:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p.rel}style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<div class="wrap topbar">
  <a class="wordmark" href="{p.url()}">{e(T(SITE['name']))}</a>
  <nav class="nav" aria-label="{'الأقسام' if L == 'ar' else 'Sections'}">{nav}</nav>
  <a class="lang" href="{p.other()}" hreflang="{'en' if L == 'ar' else 'ar'}" lang="{'en' if L == 'ar' else 'ar'}">{e(T(UI['other_lang']))}</a>
</div>
<p class="mock wrap">{e(T(UI['mock']))}</p>
{body}
<footer>
  <div class="wrap foot">
    <div>
      <p class="foot-name">{e(T(SITE['name']))}</p>
      <p>{e(T(UI['address']))}</p>
      <p>{e(T(UI['open']))}: {e(T(SITE['hours']))}</p>
      <p><a class="js-wa js-wa-text" href="#" target="_blank" rel="noopener"></a></p>
    </div>
    <div>
      <p>{e(T(UI['footer_note']))}</p>
      <p><a href="{p.url('about/')}">{e(T(ABOUT['title']))}</a> · <a href="{p.url('partners/')}">{e(T(PARTNERS['title']))}</a> · <a href="{p.url('book/')}">{e(T(UI['booking_title']))}</a></p>
    </div>
  </div>
</footer>
<a class="btn btn-primary float js-wa" href="#" target="_blank" rel="noopener">{WA_SVG} {e(T(UI['book']) if item else T(UI['ask']))}</a>
<script>window.BTP_ITEM={json.dumps(item, ensure_ascii=False) if item else 'null'};</script>
<script src="{p.rel}site.js"></script>
</body>
</html>
"""

def hero(p, h1, lead, sub=None):
    T = p.t
    return f"""<header class="gate">
  <div class="arch">
    {MARK}
    <h1>{e(h1)}</h1>
    {f'<p class="other-name" aria-hidden="true">{e(sub)}</p>' if sub else ''}
    <p class="lead">{e(lead)}</p>
    <div class="actions">
      <a class="btn btn-primary js-wa" href="#" target="_blank" rel="noopener">{WA_SVG} {e(T(UI['wa_btn']))}</a>
      <a class="btn btn-secondary js-maps" href="#" target="_blank" rel="noopener">{e(T(UI['maps_btn']))}</a>
    </div>
  </div>
</header>
<div class="threshold" aria-hidden="true"></div>"""

def section_head(p, h1, intro):
    return f"<header class='page-head wrap'><h1>{e(h1)}</h1><p class='intro'>{e(intro)}</p></header>"

def price(p, item):
    T = p.t
    return f"<span class='price'>{e(T(UI['from']))} ${item['price']} <small>{e(T(UI[item['unit']]))}</small></span>"

def card_grid(p, items, base):
    T = p.t
    cards = ""
    for it in items:
        cards += f"""<li class="card">
  <a href="{p.url(base + it['slug'] + '/')}">
    <h3>{e(T(it['name']))}</h3>
    <p class="meta">{e(T(it['hours']))} · {e(T(it['times']))}</p>
    <p>{e(T(it['blurb']))}</p>
    {price(p, it)}
  </a>
</li>"""
    return f"<ul class='cards'>{cards}</ul>"

def list_page(p, data, base):
    T = p.t
    body = section_head(p, T(data["title"]), T(data["intro"])) + f"<div class='wrap'>{card_grid(p, data['items'], base)}<p class='fine'>{e(T(UI['indicative']))}</p></div>"
    return shell(p, f"{T(data['title'])} | {T(SITE['name'])}", T(data["intro"]), f"<main>{body}</main>")

def detail_page(p, data, it, base):
    T = p.t
    hl = "".join(f"<li>{e(x)}</li>" for x in T(it["highlights"]))
    body = f"""<main class="wrap detail">
<p class="crumbs"><a href="{p.url(base)}">{e(T(data['title']))}</a></p>
<h1>{e(T(it['name']))}</h1>
<p class="lead-l">{e(T(it['blurb']))}</p>
<div class="detail-grid">
  <div>
    <h2>{e(T(UI['highlights']))}</h2>
    <ol class="hl">{hl}</ol>
    <dl class="facts">
      <dt>{e(T(UI['includes']))}</dt><dd>{e(T(it['includes']))}</dd>
      <dt>{e(T(UI['bring']))}</dt><dd>{e(T(it['bring']))}</dd>
      <dt>{e(T(UI['good_for']))}</dt><dd>{e(T(it['good_for']))}</dd>
    </dl>
  </div>
  <aside class="book-box">
    {price(p, it)}
    <dl class="facts">
      <dt>{e(T(UI['duration']))}</dt><dd>{e(T(it['hours']))} · {e(T(it['times']))}</dd>
      <dt>{e(T(UI['meet']))}</dt><dd>{e(T(SITE['name']))}, {e(T(UI['address']).split('،')[0] if p.lang == 'ar' else 'Bab Touma Square')}</dd>
    </dl>
    <a class="btn btn-primary js-wa" href="#" target="_blank" rel="noopener">{WA_SVG} {e(T(UI['book']))}</a>
    <a class="btn btn-secondary" href="{p.url('book/')}?item={it['slug']}">{e(T(UI['booking_form']))}</a>
    <p class="fine">{e(T(UI['indicative']))}</p>
  </aside>
</div>
</main>"""
    return shell(p, f"{T(it['name'])} | {T(SITE['name'])}", T(it["blurb"]), body, item=T(it["name"]))

def home_page(p):
    T = p.t
    tiles = "".join(f"<li class='tile'><a href='{p.url(s + '/')}'><h3>{e(T(n))}</h3><p>{e(T(d))}</p></a></li>" for s, n, d in HOME["tiles"])
    board = "".join(f"<tr><th>{e(T(a))}</th><td>{e(T(b))}</td></tr>" for a, b in WHATS_ON["board"][:4])
    body = hero(p, T(SITE["name"]), T(HOME["lead"]), SITE["name"]["en" if p.lang == "ar" else "ar"]) + f"""
<main>
<section><div class="wrap">
  <h2>{e(T(HOME['sections_title']))}</h2>
  <p class="intro">{e(T(HOME['sections_intro']))}</p>
  <ul class="tiles">{tiles}</ul>
</div></section>
<section><div class="wrap find">
  <div>
    <h2>{e(T(HOME['today_title']))}</h2>
    <table class="board">{board}</table>
    <p><a href="{p.url('whats-on/')}">{e(T(UI['see_all']))}</a></p>
  </div>
  <div>
    <h2>{e(T(UI['find_us']))}</h2>
    <dl class="facts">
      <dt>{e(T(UI['open']))}</dt><dd>{e(T(SITE['hours']))}</dd>
      <dt>{e(T(UI['langs']))}</dt><dd>{e(T(UI['langs_v']))}</dd>
      <dt>{e(T(UI['contact']))}</dt><dd><a class="js-wa js-wa-text" href="#" target="_blank" rel="noopener"></a> {e(T(UI['contact_v']))}</dd>
    </dl>
    <iframe class="map js-osm" title="{'خريطة ساحة باب توما' if p.lang == 'ar' else 'Map of Bab Touma Square'}" loading="lazy" referrerpolicy="no-referrer"></iframe>
  </div>
</div></section>
</main>"""
    return shell(p, f"{T(SITE['name'])} | {'قهوة ودليل الشام القديمة' if p.lang == 'ar' else 'Coffee and visitor help in Old Damascus'}", T(HOME["lead"]), body)

def transfers_page(p):
    T = p.t
    rows = "".join(f"<tr><td>{e(T(a))}</td><td class='num'>${b}</td><td>{e(T(c))}</td></tr>" for a, b, c in TRANSFERS["rows"])
    body = section_head(p, T(TRANSFERS["title"]), T(TRANSFERS["intro"])) + f"""<div class="wrap">
<table class="prices"><thead><tr><th>{'المشوار' if p.lang == 'ar' else 'Trip'}</th><th>{'السعر' if p.lang == 'ar' else 'Price'}</th><th>{'الوقت' if p.lang == 'ar' else 'Time'}</th></tr></thead><tbody>{rows}</tbody></table>
<p class="fine">{e(T(TRANSFERS['note']))} {e(T(UI['indicative']))}</p>
<p><a class="btn btn-primary js-wa" href="#" target="_blank" rel="noopener">{WA_SVG} {e(T(UI['book']))}</a></p>
</div>"""
    return shell(p, f"{T(TRANSFERS['title'])} | {T(SITE['name'])}", T(TRANSFERS["intro"]), f"<main>{body}</main>", item=T(TRANSFERS["title"]))

def simple_list_page(p, data, items, key):
    """Stays and Help: name, text, optional price."""
    T = p.t
    lis = ""
    for row in items:
        name, text = row[0], row[1]
        tag = f"<span class='price'>{e(T(row[2]))}</span>" if len(row) > 2 else ""
        lis += f"<li><h3>{e(T(name))}</h3>{tag}<p>{e(T(text))}</p></li>"
    body = section_head(p, T(data["title"]), T(data["intro"])) + f"<div class='wrap'><ul class='help'>{lis}</ul><p><a class='btn btn-primary js-wa' href='#' target='_blank' rel='noopener'>{WA_SVG} {e(T(UI['ask']))}</a></p></div>"
    return shell(p, f"{T(data['title'])} | {T(SITE['name'])}", T(data["intro"]), f"<main>{body}</main>")

def whats_on_page(p):
    T = p.t
    board = "".join(f"<tr><th>{e(T(a))}</th><td>{e(T(b))}</td></tr>" for a, b in WHATS_ON["board"])
    ev = "".join(f"<tr><th>{e(T(a))}</th><td>{e(T(b))}</td></tr>" for a, b in WHATS_ON["events"])
    body = section_head(p, T(WHATS_ON["title"]), T(WHATS_ON["intro"])) + f"""<div class="wrap find">
<div><table class="board">{board}</table></div>
<div><h2>{e(T(WHATS_ON['events_title']))}</h2><table class="board">{ev}</table><p>{e(T(WHATS_ON['channel']))}</p></div>
</div>"""
    return shell(p, f"{T(WHATS_ON['title'])} | {T(SITE['name'])}", T(WHATS_ON["intro"]), f"<main>{body}</main>")

def partners_page(p):
    T = p.t
    offers = "".join(f"<li><h3>{e(T(a))}</h3><span class='price'>{e(T(b))}</span><p>{e(T(c))}</p></li>" for a, b, c in PARTNERS["offers"])
    rules = "".join(f"<li>{e(x)}</li>" for x in T(PARTNERS["rules"]))
    body = section_head(p, T(PARTNERS["title"]), T(PARTNERS["intro"])) + f"""<div class="wrap">
<ul class="help">{offers}</ul>
<h2>{e(T(PARTNERS['rules_title']))}</h2><ol class="hl">{rules}</ol>
<p>{e(T(PARTNERS['cta']))}</p>
<p><a class="btn btn-primary js-wa" href="#" target="_blank" rel="noopener">{WA_SVG} {e(T(UI['ask']))}</a></p>
</div>"""
    return shell(p, f"{T(PARTNERS['title'])} | {T(SITE['name'])}", T(PARTNERS["intro"]), f"<main>{body}</main>")

def about_page(p):
    T = p.t
    paras = "".join(f"<p>{e(x)}</p>" for x in T(ABOUT["body"]))
    body = f"<main class='wrap detail'><h1>{e(T(ABOUT['title']))}</h1><div class='prose'>{paras}</div></main>"
    return shell(p, f"{T(ABOUT['title'])} | {T(SITE['name'])}", T(ABOUT["body"])[0], body)

def book_page(p):
    T = p.t; L = p.lang
    groups = [(WALKS, "walks"), (TRIPS, "trips"), (EXPERIENCES, "experiences")]
    opts = ""
    for data, base in groups:
        opts += f"<optgroup label='{e(T(data['title']))}'>" + "".join(f"<option value='{it['slug']}'>{e(T(it['name']))}</option>" for it in data["items"]) + "</optgroup>"
    opts += f"<optgroup label='{e(T(TRANSFERS['title']))}'>" + "".join(f"<option value='transfer-{i}'>{e(T(a))}</option>" for i, (a, b, c) in enumerate(TRANSFERS["rows"])) + "</optgroup>"
    langs = ["العربية", "English", "Français"] if L == "ar" else ["Arabic", "English", "French"]
    lang_opts = "".join(f"<option>{x}</option>" for x in langs)
    body = f"""<main class="wrap detail">
<h1>{e(T(UI['booking_title']))}</h1>
<p class="lead-l">{e(T(UI['booking_intro']))}</p>
<form class="book-form" id="bookform">
  <label>{e(T(UI['f_what']))}<select name="item" required>{opts}</select></label>
  <div class="two">
    <label>{e(T(UI['f_date']))}<input type="date" name="date" required></label>
    <label>{e(T(UI['f_people']))}<input type="number" name="people" min="1" max="20" value="2" required></label>
  </div>
  <label>{e(T(UI['f_lang']))}<select name="lang">{lang_opts}</select></label>
  <label>{e(T(UI['f_name']))}<input type="text" name="name" required></label>
  <label>{e(T(UI['f_notes']))}<textarea name="notes" rows="3"></textarea></label>
  <button class="btn btn-primary" type="submit">{WA_SVG} {e(T(UI['f_send']))}</button>
  <p class="fine">{e(T(UI['indicative']))}</p>
</form>
</main>"""
    return shell(p, f"{T(UI['booking_title'])} | {T(SITE['name'])}", T(UI["booking_intro"]), body)

def write(p, html_text):
    d = os.path.join(ROOT, "en" if p.lang == "en" else "", p.path)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_text)

def build():
    n = 0
    for L in ("ar", "en"):
        write(Page(L, ""), home_page(Page(L, ""))); n += 1
        for data, base in ((WALKS, "walks/"), (TRIPS, "trips/"), (EXPERIENCES, "experiences/")):
            write(Page(L, base), list_page(Page(L, base), data, base)); n += 1
            for it in data["items"]:
                pth = base + it["slug"] + "/"
                write(Page(L, pth), detail_page(Page(L, pth), data, it, base)); n += 1
        write(Page(L, "transfers/"), transfers_page(Page(L, "transfers/"))); n += 1
        write(Page(L, "stays/"), simple_list_page(Page(L, "stays/"), STAYS, STAYS["items"], "stays")); n += 1
        write(Page(L, "help/"), simple_list_page(Page(L, "help/"), HELP, HELP["items"], "help")); n += 1
        write(Page(L, "whats-on/"), whats_on_page(Page(L, "whats-on/"))); n += 1
        write(Page(L, "partners/"), partners_page(Page(L, "partners/"))); n += 1
        write(Page(L, "about/"), about_page(Page(L, "about/"))); n += 1
        write(Page(L, "book/"), book_page(Page(L, "book/"))); n += 1
    # site.js config
    with open(os.path.join(ROOT, "site.js"), "w", encoding="utf-8") as f:
        f.write(SITE_JS.replace("__WA__", SITE["whatsapp"]).replace("__LAT__", str(SITE["lat"])).replace("__LON__", str(SITE["lon"])).replace("__Q__", SITE["maps_query"]))
    print(f"built {n} pages")

SITE_JS = r"""/* Generated by build.py from content.py SITE; edit there, then run build.py */
const CONFIG = { whatsapp: "__WA__", lat: __LAT__, lon: __LON__, mapsQuery: "__Q__" };
(function () {
  const lang = document.documentElement.lang === "ar" ? "ar" : "en";
  const item = window.BTP_ITEM;
  const greet = item
    ? (lang === "ar" ? "مرحبا نقطة باب توما، بدي احجز: " + item + " " : "Hello Bab Touma Point, I'd like to book: " + item + " ")
    : (lang === "ar" ? "مرحبا نقطة باب توما، بدي مساعدة بـ: " : "Hello Bab Touma Point, I'd like help with: ");
  const wa = "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(greet);
  document.querySelectorAll(".js-wa").forEach(a => { a.href = wa; });
  document.querySelectorAll(".js-wa-text").forEach(a => { a.textContent = "+" + CONFIG.whatsapp; a.dir = "ltr"; });
  document.querySelectorAll(".js-maps").forEach(a => { a.href = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(CONFIG.mapsQuery); });
  const d = 0.0035, osm = document.querySelector(".js-osm");
  if (osm) osm.src = "https://www.openstreetmap.org/export/embed.html?bbox=" + [CONFIG.lon - d, CONFIG.lat - d * 0.8, CONFIG.lon + d, CONFIG.lat + d * 0.8].join(",") + "&layer=mapnik&marker=" + CONFIG.lat + "," + CONFIG.lon;

  const form = document.getElementById("bookform");
  if (form) {
    const pre = new URLSearchParams(location.search).get("item");
    if (pre && form.item.querySelector("option[value='" + pre + "']")) form.item.value = pre;
    form.addEventListener("submit", ev => {
      ev.preventDefault();
      const f = new FormData(form), sel = form.item.selectedOptions[0].textContent;
      const msg = lang === "ar"
        ? `مرحبا نقطة باب توما، بدي احجز:\n${sel}\nالتاريخ: ${f.get("date")}\nعدد الأشخاص: ${f.get("people")}\nلغة الدليل: ${f.get("lang")}\nالاسم: ${f.get("name")}\n${f.get("notes") || ""}`
        : `Hello Bab Touma Point, I'd like to book:\n${sel}\nDate: ${f.get("date")}\nPeople: ${f.get("people")}\nGuide language: ${f.get("lang")}\nName: ${f.get("name")}\n${f.get("notes") || ""}`;
      window.open("https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(msg), "_blank", "noopener");
    });
  }
})();
"""

if __name__ == "__main__":
    build()
