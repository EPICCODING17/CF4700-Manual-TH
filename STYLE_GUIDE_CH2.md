# CF-4700 Manual TH — Chapter 2 (LAN External Control) style guide

Read `STYLE_GUIDE.md` FIRST (the base rules: one page = one `translated/pNNN.html` file with a
`<!--TITLE:...-->` first line, mirror the book 1:1, never merge/skip pages, verbatim numbers/units,
Thai description + English name in parentheses on first mention, complete coverage of every row).
This file adds Chapter 2-specific content types that Chapter 1 didn't have.

Read `translated/p017.html` for the base command-card pattern (still used occasionally). Chapter 2
is mostly THREE new content shapes, described below. Most Chapter 2 pages are correspondence
tables (shape 3) — use it far more than the others.

## Shape 1 — numbered tutorial steps (`.step`)

Used for procedural walkthroughs (e.g. "Creating Control Programs" showing how to set up a VBA/C#
project). The source numbers each step ("1 Enable the Development tab...", "2 Create a command
button...").

```html
<div class="step">
  <div class="step-head"><div class="num">1</div><div class="step-title">Thai step title (สั้นๆ)</div></div>
  <p>Thai translation of the step's instructions, as prose.</p>
</div>
```

## Shape 2 — API method reference (`.api-card`)

Used for the CF9000Controller class method list (VBA and C# variants). One `.api-card` per method:

```html
<div class="api-card">
  <div class="api-sig">Execute (commandName As String) As String</div>
  <div class="kv">
    <div>คำอธิบาย</div><div>ส่งคำสั่ง (ไม่มีพารามิเตอร์)</div>
    <div>Argument 1</div><div>ชื่อคำสั่ง (Command name)</div>
    <div>ค่าที่คืนกลับ</div><div>กรณีคำสั่ง Get จะได้ค่าที่อ่าน / คำสั่งอื่นได้ 0 (สำเร็จ) หรือ &minus;1 (ล้มเหลว)</div>
  </div>
  <div class="api-example codeblock">cFController.Execute(<span class="cm">"KeySTART"</span>);</div>
</div>
```

- The `api-sig` line is the method signature verbatim from the source (do not translate code).
- `.kv` rows: label in Thai (คำอธิบาย, Argument 1/2/3..., ค่าที่คืนกลับ) — keep "Argument N" labels
  in English/numeral form like the source (that's a technical label, not prose), only the VALUES
  next to them are Thai.
- Include the `.api-example` codeblock only if the source shows one.
- The VBA section and the C# section are separate groups of methods with the same names/meaning
  but different signatures — translate both in full, do not skip the C# ones as "duplicate."
- Use `<div class="subhead"><span class="sq"></span>...</div>` for the group headers within 3.1
  (e.g. "การใช้งานด้วย VBA (Commands using VBA)", "การใช้งานด้วย C# (C#)", "วิธี GetData ทั้งบรรทัด
  (All-line data acquisition method)", "System methods").

## Shape 3 — correspondence tables (MOST of Chapter 2 uses this)

Sections 3.2 through 3.7 are large tables mapping a UI setting key / dialog box field / control
key to its LAN command name(s) and argument values. Render as a plain `.table-wrap > table`.
Mirror WHATEVER COLUMNS the source page actually shows for that page — do not force a fixed column
set. Common column sets you'll see: `Setting Key | Content | Command name | Arg1`, or
`Key | Content | Command | Arg1 | Arg2`, or `Item name | Content | Command | Arg1`, or
`Class | Key name | Command | Arg1`. Translate only the "Content"/"Outline" column (the plain-
language description) to Thai; keep the Key/Command-name column and all Arg value lists verbatim
in English/numeric form (these are literal API identifiers, e.g. `SetSampleClockFlag`).

Each source entry often has TWO command rows — a Set/action command and a paired Get command right
below it. Render this as two `<tr>`s: the first with the Key+Content text, the second with the
first two cells left empty (so the Get row visually nests under its Set row), e.g.:

```html
<div class="table-wrap"><table>
<thead><tr><th>Setting Key</th><th>คำอธิบาย</th><th>ชื่อคำสั่ง</th><th>Arg1</th></tr></thead>
<tbody>
<tr><td><strong>Sample Clock</strong></td><td>เลือกชนิดของ FFT Sample</td><td><span class="code">SetSampleClockFlag</span></td><td>0: Internal &nbsp;1: External</td></tr>
<tr><td></td><td></td><td><span class="code">GetSampleClockFlag</span></td><td>&mdash;</td></tr>
</tbody>
</table></div>
```

Use `<span class="code">...</span>` around every command name. A cell whose source value is a bare
`-` becomes `&mdash;`. Start a NEW `.table-wrap` table (don't continue the previous one) whenever
the source shows a new "■ ... Correspondences"/"■ ... Commands" subhead — precede the new table with
a `.subhead` matching that bullet heading (Thai + English in parentheses), same as Chapter 1.

## Chapter/section divider pages (e.g. p061, mirrors p009 from Chapter 1)

A page that's just a mini table-of-contents for the chapter/section — render as a `.table-wrap`
table of `เลขข้อ | หัวข้อ | หน้า`, same pattern as `translated/p009.html` if you want to check it for
reference.

## Judgement calls

If a page's raw text is ambiguous or looks like an OCR/authoring glitch in the source itself (this
happened a couple of times in Chapter 1, e.g. p042 GON command), translate as faithfully as
possible to what's printed and flag it in your final summary — do not silently "fix" or guess past
it.
