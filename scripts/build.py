# -*- coding: utf-8 -*-
"""Assemble translated/pNNN.html + assets/pages_jpg/pNNN.jpg into index.html (Phase 1: pages 1-60)."""
import base64
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
TRANSLATED = os.path.join(ROOT, "translated")
IMAGES = os.path.join(ROOT, "assets", "pages_jpg")
OUT = os.path.join(ROOT, "index.html")

TOTAL_PAGES = 122  # full book; phase 1 only renders pages START..END
START, END = 1, 60

SECTIONS = [
    ("front", "หน้าปกและเกริ่นนำ", 1, 8, None),
    ("ov", "1. ภาพรวม RS-232C Interface", 9, 13, None),
    ("cmdov", "2. ภาพรวมคำสั่ง RS-232C", 14, 16, None),
    ("ref", "3. รายการคำสั่ง RS-232C", 17, 55, None),
    ("compat", "4. ความเข้ากันได้กับ CF-4500", 56, 60, None),
]

CSS = r"""
:root {
  --bg:#f5f7fb; --card:#ffffff; --text:#172033; --muted:#667085; --line:#e4e7ec;
  --primary:#155eef; --primary-soft:#eef4ff; --danger:#d92d20; --danger-soft:#fff1f0;
  --success:#067647; --success-soft:#ecfdf3; --warning:#b54708; --warning-soft:#fffaeb;
  --teal:#0e7490; --teal-soft:#ecfeff;
  --shadow:0 8px 28px rgba(16,24,40,.08); --radius:18px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:"Prompt","Noto Sans Thai","Leelawadee UI",Tahoma,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.75}
a{color:inherit}
.header{background:linear-gradient(135deg,#0b3aa4,#155eef 60%,#3b82f6);color:#fff;padding:42px 22px 34px}
.header-inner{max-width:1280px;margin:auto}
.eyebrow{display:inline-block;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.24);padding:6px 12px;border-radius:999px;font-size:13px;margin-bottom:12px}
h1{margin:0;font-size:clamp(24px,4.4vw,40px);line-height:1.3;text-wrap:balance}
.subtitle{margin:12px 0 0;color:#e8efff;max-width:820px;text-wrap:pretty}
.actions{margin-top:20px;display:flex;gap:10px;flex-wrap:wrap}
.btn{border:0;border-radius:12px;padding:10px 16px;font-weight:700;cursor:pointer}
.btn-light{background:#fff;color:#174ea6}
.btn-ghost{background:rgba(255,255,255,.14);color:#fff;border:1px solid rgba(255,255,255,.25)}
.draft-banner{max-width:1280px;margin:16px auto 0;padding:0 18px}
.draft-banner .inner{background:var(--warning-soft);border:1px solid #fde3c0;color:#7a4a12;border-radius:14px;padding:14px 18px;font-size:14px}
.layout{max-width:1280px;margin:24px auto 60px;padding:0 18px;display:grid;grid-template-columns:280px minmax(0,1fr);gap:22px}
.sidebar{position:sticky;top:16px;height:max-content;max-height:calc(100vh - 32px);overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px;box-shadow:var(--shadow)}
.sidebar h3{margin:0 0 4px;font-size:15px}
.sidebar .pagecount{font-size:12px;color:var(--muted);margin:2px 0 12px}
.sidebar a{display:block;text-decoration:none;color:#475467;padding:7px 10px;border-radius:10px;font-size:13.5px}
.sidebar a:hover{background:var(--primary-soft);color:var(--primary)}
.content{min-width:0}
.section{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:26px;margin-bottom:20px;box-shadow:var(--shadow)}
.section h2{margin:0 0 6px;font-size:24px}
.section .rangehint{color:var(--muted);font-size:13px;margin-bottom:18px}
.section h3{margin:26px 0 10px;font-size:18px}
.section h3 .h3-num{color:var(--primary);margin-right:6px}
.subhead{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:700;color:#344054;margin:22px 0 10px}
.subhead .sq{width:9px;height:9px;background:var(--primary);display:inline-block;border-radius:2px;flex:0 0 auto}
.note,.warning,.success{border-radius:14px;padding:15px 17px;margin:16px 0}
.note{background:var(--primary-soft);border-left:5px solid var(--primary)}
.warning{background:var(--danger-soft);border-left:5px solid var(--danger)}
.success{background:var(--success-soft);border-left:5px solid var(--success)}
.warning strong{color:var(--danger)}
ul{padding-left:24px}
.kv{display:grid;grid-template-columns:200px 1fr;gap:8px 18px;margin-top:12px}
.kv div:nth-child(odd){font-weight:700;color:#344054}
.figure{margin:14px 0 4px;background:#f8fafc;border:1px solid var(--line);border-radius:14px;padding:16px;text-align:center;overflow:hidden}
.figure img{max-width:100%;height:auto;border-radius:8px;display:block;margin:auto}
.figure figcaption{font-size:13px;color:var(--muted);margin-top:8px;text-align:left}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.chip{display:inline-flex;align-items:center;border-radius:999px;padding:5px 10px;font-size:13px;background:#f2f4f7;color:#344054}
.chip.blue{background:var(--primary-soft);color:#1849a9}
.code{font-family:Consolas,monospace;background:#f2f4f7;border:1px solid #eaecf0;padding:2px 7px;border-radius:7px;white-space:nowrap}
.codeblock{font-family:Consolas,monospace;background:#0d1524;color:#d7e3ff;border-radius:14px;padding:16px 18px;overflow:auto;font-size:13.5px;line-height:1.7}
.codeblock .cm{color:#7d93c9}
.table-wrap{overflow:auto;border:1px solid var(--line);border-radius:14px}
table{width:100%;border-collapse:collapse;min-width:480px}
th,td{padding:12px 14px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:#f9fafb;font-size:13.5px}
tr:last-child td{border-bottom:0}
td.tabular,.tabular{font-variant-numeric:tabular-nums}
.footer{text-align:center;color:var(--muted);font-size:13px;margin-top:28px}
.small{font-size:13px;color:var(--muted)}

.type-badge{display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:700;padding:3px 9px;border-radius:999px;white-space:nowrap}
.type-badge .dot{width:6px;height:6px;border-radius:50%}
.type-1{background:#f2f4f7;color:#344054}.type-1 .dot{background:#98a2b3}
.type-2{background:var(--primary-soft);color:#1849a9}.type-2 .dot{background:var(--primary)}
.type-3{background:var(--success-soft);color:var(--success)}.type-3 .dot{background:var(--success)}
.type-4{background:var(--teal-soft);color:var(--teal)}.type-4 .dot{background:var(--teal)}
.type-legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px;margin:14px 0 6px}
.type-legend-item{border:1px solid var(--line);border-radius:12px;padding:10px 12px;background:#fbfcfe}
.type-legend-item p{margin:6px 0 0;font-size:13px;color:var(--muted)}

.cmd-group{margin-top:6px}
.cmd-card{border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:10px 0;background:#fff}
.cmd-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.cmd-code{font-family:Consolas,monospace;font-weight:700;font-size:15px;background:#f2f4f7;border:1px solid #eaecf0;border-radius:8px;padding:2px 9px}
.cmd-desc{flex:1;min-width:180px;font-size:14.5px;text-wrap:pretty}
.cmd-args{margin-top:10px;display:grid;grid-template-columns:130px 1fr;gap:6px 16px;font-size:13.5px}
.cmd-args .lbl{font-weight:700;color:#475467}
.cmd-args .val{color:var(--text);font-variant-numeric:tabular-nums}
.cmd-note{font-size:12.5px;color:var(--muted);margin-top:4px}

.api-card{border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:14px 0;background:#fff}
.api-sig{font-family:Consolas,monospace;font-size:14px;font-weight:700;color:#0b3aa4;background:var(--primary-soft);border-radius:10px;padding:8px 12px;overflow-x:auto;white-space:nowrap}
.api-card .kv{grid-template-columns:130px 1fr;margin-top:12px}

/* page card = one original page, mirrors the printed book 1:1 */
.pagecard{border:1px solid var(--line);border-radius:16px;padding:0;margin:0 0 22px;overflow:hidden;background:#fff}
.pagecard:last-child{margin-bottom:0}
.pagehead{display:flex;align-items:center;gap:10px;padding:12px 16px;background:#f8fafc;border-bottom:1px solid var(--line)}
.pagebadge{flex:0 0 auto;background:var(--primary);color:#fff;font-weight:800;font-size:12px;padding:4px 10px;border-radius:999px}
.pagetitle{font-weight:700;font-size:15px}
.pagebody{display:grid;grid-template-columns:300px minmax(0,1fr);gap:0}
.pageshot{position:relative;background:#f1f5f9;border-right:1px solid var(--line);display:flex;align-items:center;padding:10px}
.pageshot img{width:100%;border-radius:8px;display:block;cursor:zoom-in;transition:opacity .15s}
.pageshot img:hover{opacity:.88}
.zoomhint{position:absolute;right:16px;bottom:16px;background:rgba(17,24,39,.65);color:#fff;font-size:11px;padding:3px 8px;border-radius:999px;pointer-events:none}
.pagetext{padding:16px 18px;min-width:0}
.pagetext > *:first-child{margin-top:0}
.pagetext > *:last-child{margin-bottom:0}
.lightbox{position:fixed;inset:0;background:rgba(10,14,24,.86);display:none;align-items:center;justify-content:center;z-index:999;padding:28px;cursor:zoom-out}
.lightbox.open{display:flex}
.lightbox img{max-width:96vw;max-height:92vh;border-radius:10px;box-shadow:0 20px 60px rgba(0,0,0,.5)}
.lightbox .lbclose{position:fixed;top:18px;right:22px;color:#fff;font-size:32px;line-height:1;background:none;border:0;cursor:pointer;opacity:.85}
.lightbox .lbclose:hover{opacity:1}

@media (max-width:900px){.layout{grid-template-columns:1fr}.sidebar{position:relative;top:auto;max-height:none}.kv{grid-template-columns:1fr}.cmd-args{grid-template-columns:1fr}}
@media (max-width:760px){.pagebody{grid-template-columns:1fr}.pageshot{border-right:none;border-bottom:1px solid var(--line)}}
@media (max-width:560px){.header{padding:28px 16px}.layout{padding:0 10px}.section{padding:18px}}
"""

def b64_image(n):
    path = os.path.join(IMAGES, f"p{n:03d}.jpg")
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def load_page(n):
    path = os.path.join(TRANSLATED, f"p{n:03d}.html")
    with open(path, encoding="utf-8") as f:
        content = f.read()
    m = re.match(r"<!--TITLE:(.*?)-->\s*\n(.*)", content, re.DOTALL)
    if not m:
        raise ValueError(f"page {n}: missing TITLE comment")
    title, body = m.group(1).strip(), m.group(2)
    return title, body

def pagecard(n):
    title, body = load_page(n)
    img_b64 = b64_image(n)
    return f"""
  <div class="pagecard" id="p{n}">
    <div class="pagehead"><span class="pagebadge">หน้า {n} / {TOTAL_PAGES}</span><span class="pagetitle">{title}</span></div>
    <div class="pagebody">
      <div class="pageshot"><img src="data:image/jpeg;base64,{img_b64}" alt="ต้นฉบับหน้า {n}" onclick="openLightbox(this.src)"><span class="zoomhint">&#128269; ดูรูปใหญ่</span></div>
      <div class="pagetext">
{body}
      </div>
    </div>
  </div>"""

def build():
    missing = [n for n in range(START, END + 1) if not os.path.exists(os.path.join(TRANSLATED, f"p{n:03d}.html"))]
    if missing:
        print("MISSING translated pages:", missing)
        return False

    sidebar_links = "\n".join(
        f'    <a href="#sec-{key}">{label} <span class="small">(หน้า {lo}-{hi})</span></a>'
        for key, label, lo, hi, _ in SECTIONS
    )

    sections_html = []
    for key, label, lo, hi, _ in SECTIONS:
        cards = "\n".join(pagecard(n) for n in range(lo, hi + 1))
        sections_html.append(f"""
<section class="section" id="sec-{key}">
  <h2>{label}</h2>
  <div class="rangehint">หน้า {lo}-{hi} จาก {TOTAL_PAGES}</div>
{cards}
</section>""")

    html = f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>คู่มืออ้างอิงการควบคุมภายนอก CF-4700 (ภาษาไทย)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="header">
  <div class="header-inner">
    <div class="eyebrow">CF-4700 FFT Comparator &bull; External Control Reference</div>
    <h1>คู่มืออ้างอิงการควบคุมภายนอก CF-4700 (RS-232C / LAN)</h1>
    <p class="subtitle">ฉบับแปลไทย เรียบเรียงจากคู่มือต้นฉบับ &ldquo;CF-4700 External Control Reference Guide&rdquo; (Ver. 1.6) &mdash; ครบทุกหน้า พร้อมภาพต้นฉบับคู่กับคำแปลไทย ทุกคำสั่งและ Class Reference สำหรับเขียนโปรแกรมควบคุม CF-4700 ผ่าน RS-232C และ LAN</p>
    <div class="actions"><button class="btn btn-light" onclick="window.print()">พิมพ์ / บันทึกเป็น PDF</button></div>
  </div>
</header>

<div class="draft-banner"><div class="inner"><strong>Phase 1 &mdash; Chapter 1 เท่านั้น (หน้า 1-60 จาก {TOTAL_PAGES}):</strong> Chapter 2 (LAN External Control) จะทำต่อในเฟสถัดไป</div></div>

<div class="layout">
<aside class="sidebar">
  <h3>สารบัญ</h3>
  <div class="pagecount">หน้า {START}-{END} / {TOTAL_PAGES}</div>
  <nav>
{sidebar_links}
  </nav>
</aside>
<main class="content">
{''.join(sections_html)}
<div class="footer">CF-4700 External Control Reference Guide &bull; ฉบับแปลไทยสำหรับใช้งานภายใน &bull; Phase 1: หน้า {START}-{END} / {TOTAL_PAGES}</div>
</main>
</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <button class="lbclose" onclick="closeLightbox(event)">&times;</button>
  <img id="lightbox-img" src="" alt="ภาพขยาย">
</div>
<script>
function openLightbox(src){{
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox').classList.add('open');
}}
function closeLightbox(e){{
  if(e) e.stopPropagation();
  document.getElementById('lightbox').classList.remove('open');
  document.getElementById('lightbox-img').src = '';
}}
document.addEventListener('keydown', function(e){{
  if(e.key === 'Escape') closeLightbox();
}});
</script>
</body>
</html>"""

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", OUT, len(html), "bytes")
    return True

if __name__ == "__main__":
    build()
