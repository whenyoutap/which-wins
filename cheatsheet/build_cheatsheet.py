# Builds cheatsheet/cheatsheet.html from cheatsheet/races.json. Run from the repo root: python3 cheatsheet/build_cheatsheet.py
# Then make the PDF with headless Chrome (print to A4, backgrounds on).
import html, json
e = html.escape
R = json.load(open("cheatsheet/races.json"))
KIND = {"counted": "counted steps", "timed": "timed", "counted + timed": "counted + timed"}
cards = "".join(f"""<div class="c"><div class="h"><span class="no">No. {r['no']}</span><b>{e(r['title'])}</b><span class="k">{KIND[r.get('kind', 'timed')]}</span></div>
<div class="rd"><span class="t">R1</span><div><b>{e(r['r1'])}</b><i>{e(r['r1res'])}</i></div><span class="w">{e(r['r1w'])}</span></div>
<div class="rd"><span class="t t2">R2</span><div><b>{e(r['r2'])}</b><i>{e(r['r2res'])}</i></div><span class="w">{e(r['r2w'])}</span></div>
<p class="rule">{e(r['rule'])}</p><p class="iq"><b>Interview:</b> {e(r['iq'])} <span>{e(r['ia'])}</span></p></div>""" for r in R)
open("cheatsheet/cheatsheet.html", "w").write(f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<style>@page{{size:A4;margin:12mm}}body{{margin:0;background:#F2ECDE;color:#16120F;font:500 9.6pt/1.3 "Space Grotesk",sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
h1{{font-size:22pt;margin:0}}h1 em{{font-style:normal;background:#FFD23F;padding:0 6px;border-radius:6px}}.sub{{margin:2px 0 10px;color:#6B625A}}
.g{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}.c{{background:#FBF7EE;border:2px solid #16120F;border-radius:10px;padding:8px 10px;break-inside:avoid}}
.h{{display:flex;gap:8px;align-items:center;font-size:13pt}}.no{{font:700 8pt "JetBrains Mono";background:#16120F;color:#FFD23F;padding:2px 6px;border-radius:4px;white-space:nowrap;flex:none}}
.k{{margin-left:auto;font:700 7pt "JetBrains Mono";color:#6B625A;border:1.5px solid #CFC6B6;border-radius:4px;padding:1px 4px;white-space:nowrap}}
.rd{{display:grid;grid-template-columns:24px 1fr auto;gap:6px;align-items:start;margin:5px 0}}.rd b{{display:block;font-size:9pt}}.rd i{{font:500 8pt "JetBrains Mono";font-style:normal;color:#3d3833}}
.t{{font:700 8pt "JetBrains Mono";background:#16120F;color:#F2ECDE;border-radius:4px;text-align:center;padding:1px 0}}.t2{{background:#C03A2B}}.w{{font:700 8.5pt "JetBrains Mono";background:#3DF5C8;border:1.5px solid #16120F;border-radius:5px;padding:1px 5px;white-space:nowrap}}
.rule{{margin:6px 0 4px;padding-top:5px;border-top:1.5px dashed #CFC6B6;font-weight:700}}.iq{{margin:0;font-size:8.5pt}}.iq span{{color:#3d3833}}
.f{{margin-top:10px;font:700 9pt "JetBrains Mono";text-align:center}}.n{{margin-top:4px;text-align:center;color:#6B625A;font-size:8.5pt}}</style></head><body>
<h1>Which <em>Wins?</em> Cheat sheet</h1><p class="sub">Real code, raced on a real laptop. Two rounds each; the rule is what to remember.</p>
<div class="g">{cards}</div>
<div class="f">@whenyoutap · run every race yourself: github.com/whenyoutap</div><div class="n">Counted races (1 to 5, and No. 7's comparisons) give the same numbers on any machine. Timed races (6 to 16) are from one Intel Core i9-14900HX laptop: your times will differ, the winner of each round should not.</div>
</body></html>""")
print(len(R), "races")
