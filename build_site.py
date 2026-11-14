# Builds docs/index.html (whenyoutap.com) from cheatsheet/races.json, in the Kage ink style of the reels.
# Clean layout: one idea per section, the card shows only what you need to choose (the matchup and each round's winner);
# numbers, the rule and the interview question sit behind "Details". Run from the repo root: python3 build_site.py
import html, json

R = sorted(json.load(open("cheatsheet/races.json")), key=lambda r: -r["no"])  # newest first
E = html.escape
KIND = {"counted": "Counted steps: you get exactly these numbers.", "timed": "Timed on one laptop: your times will differ, the winner should not.", "counted + timed": "Counts match on any machine; times differ."}


def vs(title):
    a, b = title.split(" vs ")
    return f'<span class="pill y">{E(a)}</span> <span class="vs">vs</span> <span class="pill m">{E(b)}</span>'


cards = []
for r in R:
    watch = f'<a class="ghost" href="{E(r["reel"])}">Watch</a>' if r.get("reel") else ""
    cards.append(f'''<article class="race" data-posted="{E(r.get("posted", ""))}">
  <a class="thumb" href="{E(r.get("reel") or "https://www.instagram.com/whenyoutap/")}"><img src="img/race-{r["no"]:02d}.webp" alt="Which Wins? No. {r["no"]}: {E(r["title"])}" loading="lazy" width="120" height="213"></a>
  <div class="body">
    <p class="meta"><span class="no">#{r["no"]}</span><span class="new" hidden>NEW</span></p>
    <h3>{vs(r["title"])}</h3>
    <ol class="rounds"><li data-w="{r["r1w_side"]}" data-x="{r["r1x"]}"><span>{E(r["r1s"])}</span><b>{E(r["r1sw"])}</b><i class="lanes"><i class="ln a"></i><i class="ln b"></i></i></li><li data-w="{r["r2w_side"]}" data-x="{r["r2x"]}"><span>{E(r["r2s"])}</span><b>{E(r["r2sw"])}</b><i class="lanes"><i class="ln a"></i><i class="ln b"></i></i></li></ol>
    <p class="act"><a class="run" href="https://github.com/whenyoutap/which-wins/tree/main/{E(r["folder"])}">▶ Run it</a>{watch}</p>
    <details><summary>Details</summary>
      <p><b>Round 1.</b> {E(r["r1"])}: {E(r["r1res"])}</p>
      <p><b>Round 2.</b> {E(r["r2"])}: {E(r["r2res"])}</p>
      <p class="rule">{E(r["rule"])}</p>
      <p><b>Interview:</b> {E(r["iq"])} {E(r["ia"])}</p>
      <p class="fine">{E(KIND[r.get("kind", "timed")])}</p>
    </details>
  </div>
</article>''')

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Which Wins? · whenyoutap</title>
<meta name="description" content="Kage races real code on a real laptop. Every result, and the code to run it yourself.">
<meta property="og:title" content="Which Wins? · whenyoutap"><meta property="og:description" content="Real code, raced on a real laptop. Run every race yourself."><meta property="og:image" content="https://whenyoutap.com/img/kage-avatar.jpg">
<link rel="icon" href="img/kage-avatar.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{{--paper:#F2ECDE;--ink:#16120F;--yel:#FFD23F;--mint:#3DF5C8;--grey:#6B625A;--card:#FBF7EE;--red:#C03A2B;--line:#E3DACA}}
*{{box-sizing:border-box}}
body{{margin:0;color:var(--ink);font:500 17px/1.5 "Space Grotesk",system-ui,sans-serif;background:var(--paper) url(img/paper.webp) center/1024px repeat}}
body::before{{content:"";position:fixed;inset:0;background:rgba(242,236,222,.72);pointer-events:none;z-index:-1}}
a{{color:var(--ink)}}
main{{max-width:1040px;margin:0 auto;padding:20px 16px 0}}
nav{{display:flex;justify-content:space-between;align-items:center}}
.brand{{display:flex;align-items:center;gap:10px;font:700 16px "JetBrains Mono",monospace;text-decoration:none}}
.brand img{{width:36px;height:36px;border-radius:50%;border:2px solid var(--ink)}}
nav a.ig{{font:700 14px "JetBrains Mono",monospace;text-decoration:none}}
.hero{{display:grid;grid-template-columns:1fr;align-items:center;gap:8px;padding:48px 0 56px}}
@media(min-width:760px){{.hero{{grid-template-columns:1.3fr 1fr}}}}
h1{{font-size:clamp(48px,11vw,96px);line-height:.95;margin:0 0 16px;letter-spacing:-.02em}}
.pill{{padding:0 .16em;border-radius:.14em}}.y{{background:var(--yel)}}.m{{background:var(--mint)}}
.lead{{font-size:clamp(19px,3.6vw,24px);margin:0 0 28px;max-width:28ch}}
.hero .kage{{justify-self:center;width:min(280px,62vw);filter:drop-shadow(0 14px 18px rgba(22,18,15,.18))}}
.btns{{display:flex;flex-wrap:wrap;gap:12px}}
.btn{{font:700 16px "JetBrains Mono",monospace;text-decoration:none;border:3px solid var(--ink);border-radius:14px;padding:12px 18px;background:var(--card);box-shadow:4px 4px 0 var(--ink);transition:transform .1s}}
.btn:hover{{transform:translate(-2px,-2px)}}.btn.y{{background:var(--yel)}}
h2{{font-size:clamp(26px,5vw,34px);margin:0 0 18px}}
.races{{display:grid;grid-template-columns:1fr;gap:18px}}
@media(min-width:820px){{.races{{grid-template-columns:1fr 1fr}}}}
.race{{display:grid;grid-template-columns:96px 1fr;gap:16px;background:var(--card);border:3px solid var(--ink);border-radius:18px;padding:14px;box-shadow:5px 5px 0 var(--ink);align-items:start}}
@media(min-width:480px){{.race{{grid-template-columns:120px 1fr}}}}
.thumb img{{width:100%;height:auto;border-radius:10px;border:2px solid var(--ink);display:block}}
.meta{{margin:0;display:flex;gap:8px;align-items:center}}
.no{{font:700 13px "JetBrains Mono",monospace;background:var(--ink);color:var(--yel);padding:2px 8px;border-radius:6px}}
.new{{font:700 12px "JetBrains Mono",monospace;background:var(--red);color:#fff;border-radius:6px;padding:2px 8px}}
.race h3{{font-size:clamp(20px,4.2vw,24px);line-height:1.25;margin:8px 0 10px}}.vs{{font-size:.8em;color:var(--grey)}}
.rounds{{list-style:none;margin:0 0 12px;padding:0;display:grid;gap:6px}}
.rounds li{{display:flex;flex-wrap:wrap;justify-content:space-between;gap:2px 10px;border-bottom:1px solid var(--line);padding-bottom:8px;font-size:15px}}
.lanes{{flex-basis:100%;display:grid;gap:3px;margin-top:4px}}.ln{{display:block;height:6px;border-radius:3px;background:#E6DDCB;position:relative;overflow:hidden}}.ln::after{{content:"";position:absolute;inset:0;width:calc(var(--p,0)*100%);border-radius:3px}}.ln.a::after{{background:#E8B400}}.ln.b::after{{background:#0FB58E}}.ln.done::after{{box-shadow:0 0 0 2px var(--ink) inset}}
.rounds span{{color:var(--grey)}}.rounds b{{text-align:right}}
.act{{display:flex;gap:10px;margin:0 0 6px}}
.run,.ghost{{font:700 14px "JetBrains Mono",monospace;text-decoration:none;border:2px solid var(--ink);border-radius:10px;padding:5px 12px}}.run{{background:var(--mint)}}
details summary{{cursor:pointer;font:700 13px "JetBrains Mono",monospace;color:var(--grey)}}
details p{{margin:8px 0 0;font-size:15px}}.rule{{font-weight:700}}.fine{{color:var(--grey);font-size:13px}}
.free{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:16px;background:var(--ink);color:var(--paper);border-radius:20px;padding:24px;margin:56px 0 0}}
.free h2{{margin:0;color:var(--yel)}}.free p{{margin:4px 0 0;color:#D9D0BF}}
footer{{margin-top:40px;padding:140px 16px 32px;text-align:center;color:var(--grey);font-size:14px;background:url(img/mountains.webp) center top/1600px auto no-repeat}}
footer img{{width:90px;display:block;margin:0 auto 8px}}footer a{{font-weight:700}}
@keyframes rise{{from{{opacity:0;transform:translateY(24px)}}to{{opacity:1;transform:none}}}}
@keyframes sweep{{from{{background-size:0% 100%}}to{{background-size:100% 100%}}}}
@keyframes float{{0%,100%{{transform:translateY(0) rotate(-1deg)}}50%{{transform:translateY(-12px) rotate(1deg)}}}}
@keyframes pop{{0%{{transform:scale(.3);opacity:0}}70%{{transform:scale(1.15)}}100%{{transform:scale(1);opacity:1}}}}
@keyframes pulse{{50%{{transform:scale(1.12)}}}}
nav{{animation:rise .6s both}}
h1{{animation:rise .7s .05s both}}h1 .y{{background:linear-gradient(var(--yel),var(--yel)) no-repeat left/0% 100%;animation:sweep .7s .55s cubic-bezier(.2,.8,.2,1) forwards}}
.lead{{animation:rise .7s .25s both}}.btns{{animation:rise .7s .4s both}}
.hero .kage{{animation:pop .8s .3s both,float 4.5s 1.2s ease-in-out infinite}}
.btn{{transition:transform .15s,box-shadow .15s}}.btn:hover{{transform:translate(-3px,-3px);box-shadow:7px 7px 0 var(--ink)}}.btn:active{{transform:translate(2px,2px);box-shadow:2px 2px 0 var(--ink)}}
.race{{opacity:0;transform:translateY(28px);transition:opacity .6s,transform .6s cubic-bezier(.2,.8,.2,1),box-shadow .2s}}.race.in{{opacity:1;transform:none}}.race:hover{{box-shadow:8px 8px 0 var(--ink)}}
.thumb img{{transition:transform .3s}}.race:hover .thumb img{{transform:rotate(-2deg) scale(1.04)}}
.new:not([hidden]){{display:inline-block;animation:pulse 1.4s ease-in-out infinite}}
.rounds b{{transition:opacity .4s}}.rounds li:not(.ran) b{{opacity:0}}
.run{{transition:transform .15s}}.run:hover{{transform:translateY(-2px)}}
footer img{{animation:float 5s ease-in-out infinite}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}.race{{opacity:1;transform:none}}.rounds li b{{opacity:1}}h1 .y{{background-size:100% 100%}}}}
@media(max-width:520px){{.hero{{padding:28px 0 36px}}.hero .kage{{display:none}}.rounds li{{flex-direction:column;gap:0}}.rounds b{{text-align:left}}}}
</style></head><body><main>
<nav><a class="brand" href="./"><img src="img/kage-avatar.jpg" alt="">whenyoutap</a><a class="ig" href="https://www.instagram.com/whenyoutap/">Instagram ↗</a></nav>
<section class="hero">
  <div>
    <h1>Which <span class="pill y">Wins?</span></h1>
    <p class="lead">Kage races real code on a real laptop. You can run every race yourself.</p>
    <div class="btns"><a class="btn y" href="https://github.com/whenyoutap/which-wins">▶ Run it yourself</a><a class="btn" href="which-wins-cheatsheet.pdf">Cheat sheet</a></div>
  </div>
  <img class="kage" src="img/kage-point.webp" alt="Kage, the ink ninja, pointing" width="280" height="358">
</section>
<h2>Races</h2>
<section class="races">
{chr(10).join(cards)}
</section>
<section class="free"><div><h2>Every race on one page</h2><p>Free cheat sheet, with the interview question each race answers.</p></div><a class="btn y" href="which-wins-cheatsheet.pdf">Download PDF</a></section>
</main>
<footer><img src="img/kage-bow.webp" alt="Kage bowing" width="90" height="119">New race every day on <a href="https://www.instagram.com/whenyoutap/">@whenyoutap</a> · <a href="https://github.com/whenyoutap/which-wins">GitHub</a></footer>
<script>
// Cards rise in as they scroll into view; then each round runs a tiny race: the winner's lane fills first, the loser's at its real speed ratio
// (capped so the page never waits more than about 3 s). Ties fill together; "none" never finishes; "wipe" fills, then empties (the RAM crash).
const ease = (u) => 1 - Math.pow(1 - Math.min(1, u), 3);
function race(li) {{
  const w = li.dataset.w, x = parseFloat(li.dataset.x) || 1, a = li.querySelector(".ln.a"), b = li.querySelector(".ln.b"), T = 700, t0 = performance.now();
  const lose = (k) => Math.min(1, k / Math.min(x, 4.5)), set = (el, v) => el.style.setProperty("--p", v.toFixed(3));
  (function step(now) {{ const k = (now - t0) / T; let pa, pb;
    if (w === "a") {{ pa = ease(k); pb = ease(lose(k)) * (x > 4.5 ? Math.min(1, 4.5 / x * 4) : 1); }}
    else if (w === "b") {{ pb = ease(k); pa = ease(lose(k)) * (x > 4.5 ? Math.min(1, 4.5 / x * 4) : 1); }}
    else if (w === "tie") {{ pa = pb = ease(k); }}
    else if (w === "none") {{ pa = ease(k); pb = Math.min(.04, k * .01); }}
    else {{ pa = k < 1.2 ? ease(k) : Math.max(0, 1 - (k - 1.2) * 2); pb = ease(k); }}
    set(a, pa); set(b, pb); if (k >= 1) {{ li.classList.add("ran"); (w === "a" ? a : w === "b" ? b : a).classList.add("done"); }}
    if (k < 4.6) requestAnimationFrame(step); }})(t0);
}}
const io = new IntersectionObserver((es) => es.forEach((e) => {{ if (!e.isIntersecting) return; const c = e.target; io.unobserve(c);
  setTimeout(() => {{ c.classList.add("in"); c.querySelectorAll(".rounds li").forEach((li, i) => setTimeout(() => race(li), 450 + i * 500)); }}, (c.dataset.i % 2) * 120); }}), {{ threshold: .25 }});
document.querySelectorAll(".race").forEach((c, i) => {{ c.dataset.i = i; io.observe(c); }});
if (matchMedia("(prefers-reduced-motion: reduce)").matches) document.querySelectorAll(".rounds li").forEach((li) => {{ li.classList.add("ran"); li.querySelectorAll(".ln").forEach((l) => l.style.setProperty("--p", 1)); }});
// "NEW" on races posted in the last 3 days (each card carries its posting date).
document.querySelectorAll(".race[data-posted]").forEach((c) => {{ const d = new Date(c.dataset.posted + "T00:00:00+05:30"); if (Date.now() - d < 3 * 864e5) c.querySelector(".new").hidden = false; }});
</script></body></html>
'''
open("docs/index.html", "w").write(page)
print("docs/index.html", len(page), "bytes,", len(R), "races")
