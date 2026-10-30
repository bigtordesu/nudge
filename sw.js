// Nudge service worker: works offline, and picks up new versions when online.
const CACHE = 'nudge-v1';
const SHELL = ['./', './index.html', './manifest.webmanifest', './icon-180.png', './icon-192.png', './icon-512.png', './icon-maskable-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

const withTimeout = (p, ms) => new Promise((resolve, reject) => {
  const t = setTimeout(() => reject(new Error('timeout')), ms);
  p.then(v => { clearTimeout(t); resolve(v); }, err => { clearTimeout(t); reject(err); });
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // The page itself: try the network first so updates arrive, fall back to the cache offline.
  if (req.mode === 'navigate') {
    e.respondWith((async () => {
      const cache = await caches.open(CACHE);
      try {
        const res = await withTimeout(fetch(req), 4000);
        if (res && res.ok) cache.put('./index.html', res.clone());
        return res;
      } catch (err) {
        return (await cache.match('./index.html')) || (await cache.match('./')) || Response.error();
      }
    })());
    return;
  }

  // Icons, manifest and fonts: serve from cache, refresh in the background.
  const sameOrigin = url.origin === self.location.origin;
  const isFont = url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com';
  if (!sameOrigin && !isFont) return;
  const cacheP = caches.open(CACHE);
  const network = fetch(req).then(async res => {
    if (res && (res.ok || res.type === 'opaque')) (await cacheP).put(req, res.clone());
    return res;
  }).catch(() => null);
  e.waitUntil(network);
  e.respondWith(cacheP.then(c => c.match(req)).then(hit => hit || network.then(res => res || Response.error())));
});
