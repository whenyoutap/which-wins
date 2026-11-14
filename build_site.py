# Builds docs/index.html (whenyoutap.com) from cheatsheet/races.json, in the Kage ink style of the reels.
# Run from the repo root: python3 build_site.py
import html, json

R = json.load(open("cheatsheet/races.json"))
E = html.escape
POSES = ["cheer", "think", "smug", "point", "cheer", "think"]
KIND = {"counted": "counted steps, not timed", "timed": "timed on one laptop", "counted + timed": "counted, and timed"}


def vs(title):
    a, b = title.split(" vs ")
    return f'<span class="pill y">{E(a)}</span> vs <span class="pill m">{E(b)}</span>'


cards = []
for i, r in enumerate(sorted(R, key=lambda r: -r["no"])):  # newest first
    reel = f'<a href="{E(r["reel"])}">Watch the reel ↗</a>' if r.get("reel") else '<span class="soon">Reel coming soon</span>'
    cards.append(f'''<article class="race" data-posted="{E(r.get("posted", ""))}">
  <a class="thumb" href="{E(r["reel"] or "https://www.instagram.com/whenyoutap/")}"><img src="img/race-{r["no"]:02d}.webp" alt="Which Wins? No. {r["no"]}: {E(r["title"])}" loading="lazy" width="180" height="320"></a>
  <div class="body">
    <span class="chip">WHICH WINS? #{r["no"]}</span> <span class="new" hidden>NEW</span> <span class="kind">{E(KIND[r.get("kind", "timed")])}</span>
    <h3>{vs(r["title"])}</h3>
    <div class="round"><span class="rn r1">ROUND 1</span><b>{E(r["r1"])}</b><code>{E(r["r1res"])}</code><span class="win">Winner: {E(r["r1w"])}</span></div>
    <div class="round"><span class="rn r2">ROUND 2</span><b>{E(r["r2"])}</b><code>{E(r["r2res"])}</code><span class="win">Winner: {E(r["r2w"])}</span></div>
    <p class="rule">{E(r["rule"])}</p>
    <details><summary>Interview question</summary><p><b>{E(r["iq"])}</b><br>{E(r["ia"])}</p></details>
    <p class="links"><a class="run" href="https://github.com/whenyoutap/which-wins/tree/main/{E(r["folder"])}">▶ Run it yourself</a>{reel}</p>
  </div>
</article>''')

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Which Wins? · whenyoutap</title>
<meta name="description" content="Kage races real code on a real laptop. Every result, every rule, and the code to run it yourself.">
<meta property="og:title" content="Which Wins? · whenyoutap"><meta property="og:description" content="Real code, raced on a real laptop. Run every race yourself."><meta property="og:image" content="https://whenyoutap.com/img/kage-avatar.jpg">
<link rel="icon" href="img/kage-avatar.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{{--paper:#F2ECDE;--ink:#16120F;--yel:#FFD23F;--mint:#3DF5C8;--grey:#6B625A;--card:#FBF7EE;--red:#C03A2B;--green:#1AA583}}
*{{box-sizing:border-box}}
body{{margin:0;color:var(--ink);font:500 17px/1.5 "Space Grotesk",system-ui,sans-serif;background:var(--paper) url(img/paper.webp) center/1024px repeat}}
body::before{{content:"";position:fixed;inset:0;background:rgba(242,236,222,.7);pointer-events:none;z-index:-1}}
a{{color:var(--ink)}}
main{{max-width:960px;margin:0 auto;padding:24px 16px 0}}
.top{{display:flex;justify-content:space-between;align-items:center;gap:12px}}
.brand{{display:flex;align-items:center;gap:10px;font:700 16px "JetBrains Mono",monospace;text-decoration:none}}
.brand img{{width:40px;height:40px;border-radius:50%;border:2px solid var(--ink)}}
.chip{{display:inline-block;font:700 13px "JetBrains Mono",monospace;background:var(--ink);color:var(--yel);padding:4px 10px;border-radius:7px}}
.hero{{display:grid;grid-template-columns:1fr;gap:8px;align-items:end;margin:28px 0 8px}}
@media(min-width:760px){{.hero{{grid-template-columns:1.4fr 1fr}}}}
h1{{font-size:clamp(44px,10vw,88px);line-height:.98;margin:14px 0 10px;letter-spacing:-.02em}}
.pill{{padding:0 .18em;border-radius:.16em}}.y{{background:var(--yel)}}.m{{background:var(--mint)}}
.lead{{font-size:clamp(18px,3.4vw,22px);margin:0 0 6px}}.sub{{color:var(--grey);margin:0}}
.hero .kage{{justify-self:center;width:min(300px,70vw);filter:drop-shadow(0 14px 18px rgba(22,18,15,.18))}}
.stamp{{display:inline-block;margin:16px 0 0;transform:rotate(-4deg);border:4px solid var(--green);color:var(--green);font:700 16px "JetBrains Mono",monospace;padding:6px 12px;border-radius:10px;background:rgba(242,236,222,.9)}}
.cta{{display:flex;flex-wrap:wrap;gap:12px;margin:26px 0 8px}}
.btn{{font:700 16px "JetBrains Mono",monospace;text-decoration:none;border:3px solid var(--ink);border-radius:14px;padding:12px 16px;background:var(--card);box-shadow:4px 4px 0 var(--ink);transition:transform .1s}}
.btn:hover{{transform:translate(-2px,-2px)}}.btn.y{{background:var(--yel)}}.btn.dark{{background:var(--ink);color:var(--yel)}}
h2{{font-size:clamp(26px,5vw,36px);margin:42px 0 4px}}.how{{color:var(--grey);margin:0 0 18px}}
.races{{display:grid;gap:18px}}
.race{{display:grid;grid-template-columns:120px 1fr;gap:16px;background:var(--card);border:3px solid var(--ink);border-radius:20px;padding:14px;box-shadow:6px 6px 0 var(--ink)}}
@media(min-width:640px){{.race{{grid-template-columns:180px 1fr;padding:18px}}}}
.thumb img{{width:100%;height:auto;border-radius:12px;border:3px solid var(--ink);display:block}}
.race h3{{font-size:clamp(22px,4.6vw,30px);margin:8px 0 10px;line-height:1.15}}
.round{{display:grid;gap:2px;margin:0 0 10px}}.round b{{font-size:16px}}
.rn{{justify-self:start;font:700 12px "JetBrains Mono",monospace;color:var(--paper);padding:2px 8px;border-radius:6px}}.r1{{background:var(--ink)}}.r2{{background:var(--red)}}
.round code{{font:600 14px/1.4 "JetBrains Mono",monospace;background:#1C1815;color:#EDE6D6;padding:6px 10px;border-radius:8px;white-space:normal}}
.win{{font:700 13px "JetBrains Mono",monospace;color:var(--green)}}
.rule{{border-top:2px dashed #D9D0BF;padding-top:10px;margin:6px 0 8px;font-weight:700}}
details{{margin:0 0 10px}}summary{{cursor:pointer;font:700 14px "JetBrains Mono",monospace;color:var(--grey)}}details p{{margin:6px 0 0}}
.links{{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin:0}}.links a{{font-weight:700}}
.run{{font:700 14px "JetBrains Mono",monospace;background:var(--mint);border:2px solid var(--ink);border-radius:10px;padding:6px 10px;text-decoration:none}}
.soon{{color:var(--grey);font-size:14px}}
.new{{font:700 12px "JetBrains Mono",monospace;background:var(--red);color:#fff;border-radius:6px;padding:3px 8px;margin-left:4px;animation:pulse 1.6s ease-in-out infinite}}@keyframes pulse{{50%{{transform:scale(1.08)}}}}
.kind{{font:700 12px "JetBrains Mono",monospace;color:var(--grey);border:2px solid #D9D0BF;border-radius:6px;padding:2px 6px;margin-left:4px;white-space:nowrap}}
.free{{display:grid;grid-template-columns:1fr;gap:12px;align-items:center;background:var(--ink);color:var(--paper);border-radius:22px;padding:22px;margin:40px 0 0}}
@media(min-width:640px){{.free{{grid-template-columns:1fr auto}}}}.free h2{{margin:0;color:var(--yel)}}.free p{{margin:6px 0 0;color:#D9D0BF}}
.free img{{width:150px;justify-self:center}}
footer{{position:relative;margin-top:30px;padding:150px 16px 34px;text-align:center;color:var(--grey);font-size:14px;background:url(img/mountains.webp) center top/1600px auto no-repeat}}
footer img{{width:110px;display:block;margin:0 auto 8px}}footer a{{font-weight:700}}
</style></head><body><main>
<nav class="top"><a class="brand" href="./"><img src="img/kage-avatar.jpg" alt="">whenyoutap</a><a class="chip" href="https://www.instagram.com/whenyoutap/">@whenyoutap</a></nav>
<section class="hero">
  <div>
    <span class="chip">WHICH WINS?</span>
    <h1>Which <span class="pill y">Wins?</span></h1>
    <p class="lead">Kage races real code on a real laptop.</p>
    <p class="sub">Two rounds each. Every number comes from a real run, and you can run every race yourself.</p>
    <span class="stamp">KAGE CHECKED THE NUMBERS ✓</span>
    <div class="cta"><a class="btn y" href="https://github.com/whenyoutap/which-wins">▶ Run it yourself</a><a class="btn" href="which-wins-cheatsheet.pdf">Free cheat sheet (PDF)</a><a class="btn dark" href="https://www.instagram.com/whenyoutap/">Follow on Instagram</a></div>
  </div>
  <img class="kage" src="img/kage-point.webp" alt="Kage, the ink ninja, pointing" width="300" height="383">
</section>
<h2>Every race, newest first</h2>
<p class="how">Races 1 to 5 count steps, so you will get exactly our numbers. Races 6 to 12 are timed on one Intel Core i9-14900HX laptop: your times will differ, the winner of each round should not. No. 7 has both.</p>
<section class="races">
{chr(10).join(cards)}
</section>
<section class="free"><div><h2>The cheat sheet</h2><p>Every race on one page: both rounds, the winner, the rule to remember and the interview question it answers.</p><div class="cta"><a class="btn y" href="which-wins-cheatsheet.pdf">Download the PDF</a></div></div><img src="img/kage-cheer.webp" alt="Kage cheering" width="150" height="152"></section>
</main>
<footer><img src="img/kage-bow.webp" alt="Kage bowing" width="110" height="145">New race every day on <a href="https://www.instagram.com/whenyoutap/">Instagram @whenyoutap</a> · Code on <a href="https://github.com/whenyoutap/which-wins">GitHub</a><br>Want a race? Ask in the comments on any reel.</footer>
<script>
// "NEW" on races posted in the last 3 days (each card carries its posting date).
document.querySelectorAll(".race[data-posted]").forEach((c) => {{ const d = new Date(c.dataset.posted + "T00:00:00+05:30"); if (Date.now() - d < 3 * 864e5) c.querySelector(".new").hidden = false; }});
</script></body></html>
'''
open("docs/index.html", "w").write(page)
print("docs/index.html", len(page), "bytes,", len(R), "races")
