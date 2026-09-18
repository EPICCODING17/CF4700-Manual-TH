# -*- coding: utf-8 -*-
"""Assemble translated/pNNN.html + assets/pages_jpg/pNNN.jpg into index.html.

Redesign v2 (2026-09): responsive shell, mobile TOC drawer, collapsible
original-page compare, dark mode, themed scrollbars. Confirmed with Pong
as the reference pattern for future manual-translation projects — see
memory `cf4700-manual-redesign-pattern`.
"""
import base64
import html
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
TRANSLATED = os.path.join(ROOT, "translated")
IMAGES = os.path.join(ROOT, "assets", "pages_jpg")
OUT = os.path.join(ROOT, "index.html")

TOTAL_PAGES = 122  # full book
START, END = 1, 122

SECTIONS = [
    ("front", "หน้าปกและเกริ่นนำ", 1, 8, None),
    ("ov", "1. ภาพรวม RS-232C Interface", 9, 13, None),
    ("cmdov", "2. ภาพรวมคำสั่ง RS-232C", 14, 16, None),
    ("ref", "3. รายการคำสั่ง RS-232C", 17, 55, None),
    ("compat", "4. ความเข้ากันได้กับ CF-4500", 56, 60, None),
    ("lanov", "Chapter 2 — 1. ภาพรวม LAN External Control", 61, 64, None),
    ("lanprep", "2. การเตรียมการใช้งาน LAN External Control", 65, 75, None),
    ("api", "3.1 CF9000Controller Class", 76, 79, None),
    ("setkey", "3.2 ตารางเทียบคำสั่งกับ Setting Key", 80, 94, None),
    ("dialog", "3.3 ตารางเทียบคำสั่งกับ Dialog Box", 95, 112, None),
    ("misc", "3.4-3.7 ตารางเทียบคำสั่งอื่นๆ", 113, 117, None),
    ("ref4", "4. ภาคผนวก (Network Terms)", 118, 118, None),
    ("index", "ดัชนีคำศัพท์ (Index)", 119, 121, None),
    ("back", "หน้าปกหลัง", 122, 122, None),
]

CSS = r"""
:root{
  --bg:#f6f4ee; --surface:#fffefb; --ink:#1c2230; --ink-soft:#4d5566; --muted:#8a8f9c;
  --line:#e4e0d4; --line-strong:#d5d0c1;
  --brand:#1f4fd6; --brand-ink:#13337e; --brand-soft:#e9eefb;
  --amber:#8a5a17; --amber-soft:#f7edd9;
  --teal:#0f6e63; --teal-soft:#e3f1ee;
  --radius:14px; --radius-lg:20px;
  --shadow:0 1px 2px rgba(28,34,48,.05), 0 10px 24px -12px rgba(28,34,48,.16);
  --header-h:64px;
  color-scheme: light;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#14171e; --surface:#1c2029; --ink:#eef0f4; --ink-soft:#b6bcc9; --muted:#7d8494;
    --line:#2b303c; --line-strong:#3a4152;
    --brand:#7fa2ff; --brand-ink:#dbe6ff; --brand-soft:#212b47;
    --amber:#e3ac5c; --amber-soft:#3a2f1c;
    --teal:#6fcabd; --teal-soft:#173330;
    --shadow:0 1px 2px rgba(0,0,0,.3), 0 10px 24px -12px rgba(0,0,0,.5);
    color-scheme: dark;
  }
}
:root[data-theme="dark"]{
  --bg:#14171e; --surface:#1c2029; --ink:#eef0f4; --ink-soft:#b6bcc9; --muted:#7d8494;
  --line:#2b303c; --line-strong:#3a4152;
  --brand:#7fa2ff; --brand-ink:#dbe6ff; --brand-soft:#212b47;
  --amber:#e3ac5c; --amber-soft:#3a2f1c;
  --teal:#6fcabd; --teal-soft:#173330;
  --shadow:0 1px 2px rgba(0,0,0,.3), 0 10px 24px -12px rgba(0,0,0,.5);
  color-scheme: dark;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:calc(var(--header-h) + 16px)}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Prompt","Noto Sans Thai",Tahoma,sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:inherit}
img{max-width:100%;display:block}
button{font:inherit}

/* themed scrollbar, used by .toc */
.scroll-thin{scrollbar-width:thin;scrollbar-color:var(--line-strong) transparent}
.scroll-thin::-webkit-scrollbar{width:6px}
.scroll-thin::-webkit-scrollbar-track{background:transparent;margin-block:2px}
.scroll-thin::-webkit-scrollbar-thumb{background:var(--line-strong);border-radius:999px;border:1px solid transparent;background-clip:padding-box}
.scroll-thin::-webkit-scrollbar-thumb:hover{background:var(--muted)}

.topbar{position:sticky;top:0;z-index:40;display:flex;align-items:center;gap:14px;height:var(--header-h);padding:0 18px;background:color-mix(in oklab,var(--surface) 92%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.toc-toggle{display:none;align-items:center;justify-content:center;width:40px;height:40px;border:1px solid var(--line);border-radius:10px;background:var(--surface);cursor:pointer;flex:0 0 auto}
.toc-toggle span{display:block;width:16px;height:2px;background:var(--ink);position:relative}
.toc-toggle span::before,.toc-toggle span::after{content:'';position:absolute;left:0;width:16px;height:2px;background:var(--ink)}
.toc-toggle span::before{top:-5px}
.toc-toggle span::after{top:5px}
.topbar-title{min-width:0}
.topbar-title .eyebrow{display:block;font-size:.68rem;font-weight:600;letter-spacing:.06em;color:var(--brand)}
.topbar-title h1{margin:1px 0 0;font-size:.95rem;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topbar-actions{margin-left:auto;display:flex;align-items:center;gap:8px}
.pagepill{font-size:.72rem;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}
.btn-print,.btn-search{display:inline-flex;align-items:center;gap:6px;height:38px;padding:0 14px;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink-soft);cursor:pointer;font-size:.82rem;font-weight:500}
.btn-print:hover,.btn-search:hover,.btn-search.active{border-color:var(--brand);color:var(--brand)}

/* search */
.search-panel{position:sticky;top:var(--header-h);z-index:39;max-height:0;overflow:hidden;background:var(--surface);border-bottom:1px solid var(--line);transition:max-height .22s cubic-bezier(.22,1,.36,1)}
.search-panel.open{max-height:min(70svh,640px)}
.search-inner{max-width:1280px;margin:0 auto;padding:16px 20px}
.search-row{display:flex;gap:8px}
.search-row input{flex:1;min-width:0;height:44px;padding:0 14px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);font-size:.9rem;outline:none}
.search-row input:focus{border-color:var(--brand)}
.search-row button{height:44px;padding:0 16px;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink-soft);cursor:pointer;font-size:.82rem}
.search-status{margin:10px 2px 0;font-size:.76rem;color:var(--muted)}
.search-results{margin-top:10px;max-height:46svh;overflow:auto;-webkit-overflow-scrolling:touch;display:grid;gap:4px}
.search-results button{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;align-items:baseline;width:100%;padding:10px 12px;border:0;border-radius:10px;background:transparent;color:var(--ink);text-align:left;cursor:pointer}
.search-results button:hover,.search-results button:focus-visible{background:var(--brand-soft)}
.search-results .sr-page{grid-row:1/3;color:var(--brand);font-size:.7rem;font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap}
.search-results .sr-title{font-size:.86rem;font-weight:500}
.search-results .sr-snippet{grid-column:2;font-size:.78rem;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.search-results mark{background:var(--amber-soft);color:var(--amber);border-radius:3px;padding:0 2px}

.shell{max-width:1280px;margin:0 auto;display:grid;grid-template-columns:264px minmax(0,1fr);gap:40px;padding:32px 20px 100px}
.toc{position:sticky;top:calc(var(--header-h) + 24px);align-self:start;max-height:calc(100svh - var(--header-h) - 48px);overflow:auto;-webkit-overflow-scrolling:touch}
.toc-heading{display:flex;justify-content:space-between;align-items:baseline;margin:0 0 14px;padding-bottom:10px;border-bottom:1px solid var(--ink);font-size:.78rem;font-weight:600}
.toc-heading span{color:var(--muted);font-size:.68rem;font-variant-numeric:tabular-nums}
.toc nav{display:flex;flex-direction:column}
.toc nav a{display:block;padding:9px 4px;border-radius:8px;color:var(--ink-soft);text-decoration:none;font-size:.84rem;line-height:1.4}
.toc nav a b{display:block;color:var(--ink);font-weight:500}
.toc nav a small{display:block;margin-top:1px;color:var(--muted);font-size:.72rem;font-variant-numeric:tabular-nums}
.toc nav a:hover{background:var(--brand-soft);color:var(--brand-ink)}
.toc nav a:hover b{color:var(--brand-ink)}
.toc-scrim{display:none}

.main{min-width:0}

.section{margin-bottom:64px}
.section:last-child{margin-bottom:0}
.section-head{display:flex;align-items:baseline;gap:16px;margin-bottom:6px}
.section-num{font-size:1.1rem;font-weight:600;color:var(--brand);font-variant-numeric:tabular-nums}
.section-head h2{margin:0;font-size:clamp(1.35rem,2.6vw,1.9rem);font-weight:600;letter-spacing:-.01em}
.section-range{margin:0 0 28px;color:var(--muted);font-size:.82rem}

.draft-banner{margin:0 0 28px;padding:14px 18px;border-radius:12px;background:var(--amber-soft);color:var(--amber);font-size:.88rem}

.pagecard{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow);overflow:hidden;margin-bottom:24px}
.pagecard:last-child{margin-bottom:0}
.pagecard-head{display:flex;align-items:center;gap:10px;padding:14px 20px;border-bottom:1px solid var(--line)}
.pagebadge{font-size:.72rem;font-weight:600;color:var(--brand);font-variant-numeric:tabular-nums}
.pagetitle{font-size:.86rem;font-weight:500;color:var(--ink-soft);min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pagebody{padding:26px 28px 30px}
.pagebody > *:first-child{margin-top:0}
.pagebody > *:last-child{margin-bottom:0}
.pagebody h3{margin:0 0 22px;font-size:1.2rem;font-weight:600;letter-spacing:-.005em}
.pagebody h3 .h3-num{color:var(--brand);margin-right:8px}
.pagebody p{max-width:74ch}

/* original-image compare: collapsible on mobile, open by default */
.compare{margin:0 0 26px;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.compare summary{display:flex;align-items:center;gap:8px;padding:11px 16px;background:var(--bg);cursor:pointer;font-size:.8rem;font-weight:500;color:var(--ink-soft);list-style:none}
.compare summary::-webkit-details-marker{display:none}
.compare summary::before{content:'\2295';color:var(--brand);font-size:.9rem}
.compare[open] summary::before{content:'\2296'}
.compare-shot{padding:16px;text-align:center;background:var(--bg)}
.compare-shot img{margin:0 auto;max-height:560px;width:auto;max-width:100%;border-radius:8px;cursor:zoom-in;border:1px solid var(--line-strong)}
.compare-hint{margin:8px 0 0;padding:0 16px 14px;font-size:.72rem;color:var(--muted)}

.subhead{display:flex;align-items:center;gap:8px;font-size:.92rem;font-weight:600;color:var(--ink);margin:26px 0 12px}
.subhead .sq{width:8px;height:8px;background:var(--brand);border-radius:2px;flex:0 0 auto}

ul{padding-left:24px}
.small{font-size:13px;color:var(--muted)}
.tabular{font-variant-numeric:tabular-nums}

.figure{margin:14px 0 4px;background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:16px;text-align:center;overflow:hidden}
.figure img{max-width:100%;height:auto;border-radius:8px;display:block;margin:auto}
.figure figcaption{font-size:13px;color:var(--muted);margin-top:8px;text-align:left}

.kv{display:grid;grid-template-columns:200px 1fr;gap:8px 18px;margin-top:12px}
.kv div:nth-child(odd){font-weight:700;color:var(--ink-soft)}

.code{font-family:"SFMono-Regular",Consolas,monospace;background:var(--bg);border:1px solid var(--line);padding:2px 7px;border-radius:6px;font-size:.88em}
.codeblock{font-family:"SFMono-Regular",Consolas,monospace;background:#0d1524;color:#d7e3ff;border-radius:14px;padding:16px 18px;overflow:auto;font-size:13.5px;line-height:1.7}
.codeblock .cm{color:#7d93c9}

.table-scroll{position:relative;margin:18px 0}
.table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:12px}
table{width:100%;border-collapse:collapse;min-width:440px}
th,td{padding:12px 16px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;font-size:.88rem}
th{background:var(--bg);font-size:.76rem;font-weight:600;color:var(--ink-soft);letter-spacing:.02em}
tr:last-child td{border-bottom:0}
.scroll-hint{display:none;margin:8px 2px 0;font-size:.72rem;color:var(--muted)}

.type-badge{display:inline-flex;align-items:center;gap:5px;font-size:.7rem;font-weight:600;padding:3px 9px;border-radius:999px;white-space:nowrap}
.type-badge .dot{width:6px;height:6px;border-radius:50%}
.type-1{background:var(--bg);color:var(--ink-soft)}.type-1 .dot{background:var(--muted)}
.type-2{background:var(--brand-soft);color:var(--brand-ink)}.type-2 .dot{background:var(--brand)}
.type-3{background:var(--teal-soft);color:var(--teal)}.type-3 .dot{background:var(--teal)}
.type-4{background:var(--amber-soft);color:var(--amber)}.type-4 .dot{background:var(--amber)}
.type-legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px;margin:14px 0 6px}
.type-legend-item{border:1px solid var(--line);border-radius:12px;padding:10px 12px;background:var(--surface)}
.type-legend-item p{margin:6px 0 0;font-size:13px;color:var(--muted)}

.cmd-group{margin-top:6px}
.cmd-card{border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:10px 0;background:var(--surface)}
.cmd-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.cmd-code{font-family:"SFMono-Regular",Consolas,monospace;font-weight:700;font-size:.92rem;background:var(--bg);border:1px solid var(--line);border-radius:7px;padding:2px 8px}
.cmd-desc{flex:1;min-width:180px;font-size:.9rem;text-wrap:pretty}
.cmd-args{margin-top:10px;display:grid;grid-template-columns:132px 1fr;gap:6px 16px;font-size:.84rem}
.cmd-args .lbl{font-weight:600;color:var(--ink-soft)}
.cmd-args .val{color:var(--ink);font-variant-numeric:tabular-nums}
.cmd-note{font-size:.78rem;color:var(--muted);margin-top:6px}

.api-card{border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:14px 0;background:var(--surface)}
.api-sig{font-family:"SFMono-Regular",Consolas,monospace;font-size:14px;font-weight:700;color:var(--brand-ink);background:var(--brand-soft);border-radius:10px;padding:8px 12px;overflow-x:auto;white-space:nowrap}
.api-card .kv{grid-template-columns:130px 1fr;margin-top:12px}

.step{border:1px solid var(--line);border-radius:16px;padding:18px;margin:16px 0;background:var(--surface)}
.step-head{display:flex;align-items:flex-start;gap:13px;margin-bottom:8px}
.step .num{flex:0 0 34px;height:34px;border-radius:50%;display:grid;place-items:center;background:var(--brand);color:#fff;font-weight:800}
.step-title{font-weight:800;font-size:16px;padding-top:4px}
.step p{margin:0 0 8px}
.step p:last-child{margin-bottom:0}

.note,.warning,.success{border-radius:12px;padding:14px 16px;margin:18px 0;font-size:.88rem}
.note{background:var(--brand-soft);color:var(--brand-ink)}
.warning{background:var(--amber-soft);color:var(--amber)}
.warning strong{color:var(--amber)}
.success{background:var(--teal-soft);color:var(--teal)}

.lightbox{position:fixed;inset:0;background:rgba(10,12,18,.92);display:none;align-items:center;justify-content:center;z-index:99;padding:24px;cursor:zoom-out}
.lightbox.open{display:flex}
.lightbox img{max-width:94vw;max-height:92vh;border-radius:8px;box-shadow:0 20px 60px rgba(0,0,0,.5)}
.lightbox .lbclose{position:fixed;top:16px;right:20px;background:none;border:0;color:#fff;font-size:32px;line-height:1;cursor:pointer;opacity:.85}
.lightbox .lbclose:hover{opacity:1}

.footer{text-align:center;color:var(--muted);font-size:13px;margin-top:28px}

@media (max-width:900px){
  .toc-toggle{display:inline-flex}
  .shell{grid-template-columns:1fr;gap:0;padding:20px 16px 90px}
  .toc{position:fixed;top:0;left:0;bottom:0;z-index:60;width:min(300px,84vw);max-height:none;background:var(--surface);border-right:1px solid var(--line);padding:20px 18px;transform:translateX(-100%);transition:transform .28s cubic-bezier(.22,1,.36,1);box-shadow:20px 0 40px rgba(20,24,34,.16)}
  .toc.open{transform:translateX(0)}
  .toc-scrim.open{display:block;position:fixed;inset:0;z-index:55;background:rgba(10,12,18,.45)}
  .kv{grid-template-columns:1fr}
}
@media (max-width:640px){
  .topbar{padding-inline:14px;gap:10px}
  .topbar-title h1{font-size:.84rem}
  .btn-print .lbl,.btn-search .lbl{display:none}
  .btn-print,.btn-search{width:38px;padding:0;justify-content:center}
  .pagebody{padding:20px 18px 24px}
  .pagebody h3{font-size:1.08rem}
  .cmd-args{grid-template-columns:1fr;gap:2px}
  .cmd-args .lbl{margin-top:6px}
  .compare-shot img{max-height:420px}
  .scroll-hint{display:block}
  .search-inner{padding:14px 16px}
  .search-row input,.search-row button{height:46px}
}
@media print{
  .topbar,.toc,.toc-scrim,.search-panel,.compare{display:none}
  .shell{grid-template-columns:1fr;padding:0}
}
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

EXTERNAL_IMAGES = False  # set True to reference pages/pNNN.jpg instead of embedding base64

TAG_RE = re.compile(r"<[^>]+>")

def plain_text(body_html):
    text = TAG_RE.sub(" ", body_html)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()

def pagecard(n):
    title, body = load_page(n)
    if EXTERNAL_IMAGES:
        img_src = f"pages/p{n:03d}.jpg"
    else:
        img_src = f"data:image/jpeg;base64,{b64_image(n)}"
    return f"""
  <div class="pagecard" id="p{n}">
    <div class="pagecard-head"><span class="pagebadge">หน้า {n} / {TOTAL_PAGES}</span><span class="pagetitle">{title}</span></div>
    <div class="pagebody">
      <details class="compare" open>
        <summary>เทียบกับต้นฉบับ (หน้า {n})</summary>
        <div class="compare-shot"><img src="{img_src}" alt="ต้นฉบับหน้า {n}" onclick="openLightbox(this.src)"></div>
        <p class="compare-hint">แตะภาพเพื่อดูขนาดเต็ม</p>
      </details>
{body}
    </div>
  </div>"""

def build():
    missing = [n for n in range(START, END + 1) if not os.path.exists(os.path.join(TRANSLATED, f"p{n:03d}.html"))]
    if missing:
        print("MISSING translated pages:", missing)
        return False

    if END >= TOTAL_PAGES:
        banner = ""
    else:
        banner = f'<div class="draft-banner"><strong>หน้า {START}-{END} จาก {TOTAL_PAGES}:</strong> ส่วนที่เหลือกำลังแปลต่อ</div>'

    toc_links = "\n".join(
        f'<a href="#sec-{key}"><b>{label}</b><small>หน้า {lo}-{hi}</small></a>'
        for key, label, lo, hi, _ in SECTIONS
    )

    sections_html = []
    search_index = []
    for key, label, lo, hi, _ in SECTIONS:
        cards = "\n".join(pagecard(n) for n in range(lo, hi + 1))
        sections_html.append(f"""
<section class="section" id="sec-{key}">
  <div class="section-head"><h2>{label}</h2></div>
  <p class="section-range">หน้า {lo}-{hi} จาก {TOTAL_PAGES}</p>
{cards}
</section>""")
        for n in range(lo, hi + 1):
            title, body = load_page(n)
            search_index.append({"n": n, "t": title, "s": label, "x": plain_text(body)})

    search_index_json = json.dumps(search_index, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

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
<div class="toc-scrim" id="scrim" onclick="closeToc()"></div>
<div class="topbar">
  <button class="toc-toggle" id="tocToggle" aria-label="เปิดสารบัญ" onclick="openToc()"><span></span></button>
  <div class="topbar-title">
    <span class="eyebrow">CF-4700 FFT Comparator &middot; External Control Reference</span>
    <h1>คู่มืออ้างอิงการควบคุมภายนอก CF-4700</h1>
  </div>
  <div class="topbar-actions">
    <span class="pagepill">หน้า {START}&ndash;{END}</span>
    <button class="btn-search" id="searchToggle" aria-expanded="false" aria-controls="searchPanel">&#128269;<span class="lbl"> ค้นหา</span></button>
    <button class="btn-print" onclick="window.print()">&#128438;<span class="lbl"> พิมพ์ / PDF</span></button>
  </div>
</div>

<div class="search-panel" id="searchPanel">
  <div class="search-inner">
    <div class="search-row">
      <input id="searchInput" type="search" placeholder="ค้นหาทั้งเล่ม เช่น STE, LAN, Setting Key…" autocomplete="off">
      <button id="searchClose" type="button">ปิด</button>
    </div>
    <p class="search-status" id="searchStatus">พิมพ์คำเพื่อค้นหาทั้ง {TOTAL_PAGES} หน้า</p>
    <div class="search-results" id="searchResults"></div>
  </div>
</div>

<div class="shell">
  <aside class="toc scroll-thin" id="toc">
    <div class="toc-heading">สารบัญ<span>{TOTAL_PAGES} หน้า</span></div>
    <nav>{toc_links}</nav>
  </aside>
  <main class="main">
{banner}
{''.join(sections_html)}
<div class="footer">CF-4700 External Control Reference Guide &bull; ฉบับแปลไทยสำหรับใช้งานภายใน &bull; หน้า {START}-{END} / {TOTAL_PAGES}</div>
  </main>
</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <button class="lbclose" onclick="closeLightbox(event)">&times;</button>
  <img id="lightbox-img" src="" alt="ภาพขยาย">
</div>
<script>
function openToc(){{document.getElementById('toc').classList.add('open');document.getElementById('scrim').classList.add('open');}}
function closeToc(){{document.getElementById('toc').classList.remove('open');document.getElementById('scrim').classList.remove('open');}}
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
  if(e.key === 'Escape'){{ closeLightbox(); closeToc(); closeSearch(); }}
}});
document.querySelectorAll('.toc nav a').forEach(a => a.addEventListener('click', closeToc));

var SEARCH_INDEX = {search_index_json};
(function(){{
  var toggle = document.getElementById('searchToggle');
  var panel = document.getElementById('searchPanel');
  var input = document.getElementById('searchInput');
  var status = document.getElementById('searchStatus');
  var results = document.getElementById('searchResults');

  window.openSearch = function(){{
    panel.classList.add('open');
    toggle.classList.add('active');
    toggle.setAttribute('aria-expanded', 'true');
    setTimeout(function(){{ input.focus(); }}, 120);
  }};
  window.closeSearch = function(){{
    panel.classList.remove('open');
    toggle.classList.remove('active');
    toggle.setAttribute('aria-expanded', 'false');
  }};
  toggle.addEventListener('click', function(){{
    panel.classList.contains('open') ? closeSearch() : openSearch();
  }});
  document.getElementById('searchClose').addEventListener('click', closeSearch);

  function esc(s){{ return s.replace(/[&<>]/g, function(c){{ return {{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c]; }}); }}

  function snippet(text, q){{
    var i = text.toLowerCase().indexOf(q);
    if(i < 0) return esc(text.slice(0, 90));
    var start = Math.max(0, i - 30);
    var before = text.slice(start, i);
    var match = text.slice(i, i + q.length);
    var after = text.slice(i + q.length, i + q.length + 60);
    return (start > 0 ? '&hellip;' : '') + esc(before) + '<mark>' + esc(match) + '</mark>' + esc(after);
  }}

  input.addEventListener('input', function(){{
    var q = input.value.trim().toLowerCase();
    if(!q){{
      results.innerHTML = '';
      status.textContent = 'พิมพ์คำเพื่อค้นหาทั้ง {TOTAL_PAGES} หน้า';
      return;
    }}
    var hits = SEARCH_INDEX.filter(function(p){{
      return p.t.toLowerCase().indexOf(q) > -1 || p.x.toLowerCase().indexOf(q) > -1;
    }}).slice(0, 40);
    status.textContent = hits.length ? ('พบ ' + hits.length + ' หน้า') : 'ไม่พบผลลัพธ์';
    results.innerHTML = hits.map(function(p){{
      var body = p.t.toLowerCase().indexOf(q) > -1 ? esc(p.t) : snippet(p.x, q);
      return '<button data-n="' + p.n + '"><span class="sr-page">หน้า ' + p.n + '</span><span class="sr-title">' + esc(p.t) + '</span><span class="sr-snippet">' + body + '</span></button>';
    }}).join('');
  }});

  results.addEventListener('click', function(e){{
    var btn = e.target.closest('button[data-n]');
    if(!btn) return;
    location.hash = '#p' + btn.dataset.n;
    closeSearch();
  }});
}})();
</script>
</body>
</html>"""

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", OUT, len(html), "bytes")
    return True

if __name__ == "__main__":
    import sys
    if "--artifact" in sys.argv:
        EXTERNAL_IMAGES = True
        OUT = os.path.join(ROOT, "artifact_preview.html")
    build()
