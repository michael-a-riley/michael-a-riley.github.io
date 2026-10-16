/* ===== Edit these values; both the Arabic and English pages update ===== */
const CONFIG = {
  whatsapp: "963985390583",  // temporary: Michael's Syrian number; swap for the kiosk line (digits only)
  lat: 33.513502,            // kiosk position
  lon: 36.315654,
  mapsQuery: "Bab Touma Square, Damascus" // change to "Bab Touma Point" once the Google Maps listing is live
};
/* ====================================================================== */

(function () {
  const lang = document.documentElement.lang === "ar" ? "ar" : "en";
  const greet = {
    ar: "مرحبا نقطة باب توما، بدي مساعدة بـ: ",
    en: "Hello Bab Touma Point, I'd like help with: "
  };
  const wa = "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(greet[lang]);

  document.querySelectorAll(".js-wa").forEach(a => { a.href = wa; });
  document.querySelectorAll(".js-wa-text").forEach(a => {
    a.textContent = "+" + CONFIG.whatsapp;
    a.dir = "ltr";
  });
  document.querySelectorAll(".js-maps").forEach(a => {
    a.href = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(CONFIG.mapsQuery);
  });

  const d = 0.0035;
  const osm = document.querySelector(".js-osm");
  if (osm) {
    osm.src = "https://www.openstreetmap.org/export/embed.html?bbox=" +
      [CONFIG.lon - d, CONFIG.lat - d * 0.8, CONFIG.lon + d, CONFIG.lat + d * 0.8].join(",") +
      "&layer=mapnik&marker=" + CONFIG.lat + "," + CONFIG.lon;
  }
})();
