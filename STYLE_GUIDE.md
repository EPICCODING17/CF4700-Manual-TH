# CF-4700 Manual TH — page translation style guide

You are translating individual PAGES of an English Onosokki CF-4700 technical manual (RS-232C /
LAN command reference) into Thai, for a web reference guide. Every physical page of the source
PDF becomes exactly one "page card" in the output — this mirrors the book 1:1, so do not merge,
reorder, or skip pages, and do not carry content from one page onto another even if a table or
command group is cut off mid-page in the original (that's expected — the original book does this
too).

## Your inputs

- `extract/pNNN.txt` — the raw extracted English text for page NNN (already provided per-page).
- `translated/p017.html` — a REAL, already-approved example of a finished page. Read it first.
  It shows the exact HTML you should produce for a command-reference page.

## Your output

For each page NNN you are assigned, write `translated/pNNN.html` with this exact shape:

```
<!--TITLE:สั้นๆ เป็นภาษาไทย ไม่เกินประมาณ 6-8 คำ-->
...HTML content (this becomes the "pagetext" column next to the original-page screenshot)...
```

The first line is a short Thai title used as a page badge caption (e.g. "3.1 คำสั่งตั้งค่า Input
— EU Setting", "3.10 คำสั่ง Comparator (ต่อ)"). Everything after it is the translated page body.
Do NOT include `<html>`, `<body>`, or a `<div class="pagetext">` wrapper — just the inner content
(the build script wraps it).

## Available CSS classes — use ONLY these, do not invent new ones

- `<h3><span class="h3-num">3.2</span>หัวข้อภาษาไทย (English Heading)</h3>` — ONLY when the raw
  page text contains a new top-level numbered section header line, e.g. a line by itself reading
  `3.2` immediately followed by `Display Setting Commands`. Most pages do NOT start a new section
  — in that case do not emit an `<h3>` at all, just continue straight into cards.
- `<div class="subhead"><span class="sq"></span>ชื่อกลุ่มย่อยภาษาไทย (English)</div>` — for a
  sub-group heading inside a section. In the raw text these appear as a line with just a small
  square/bullet glyph followed by the group name, e.g. "Analog Setting", "Sample Setting",
  "Tracking Analysis Setting". Always show both the Thai translation AND the original English
  name in parentheses, like the example page.
- `<div class="cmd-group"> ... </div>` — wraps a run of `.cmd-card` command entries under the
  same subhead (see p017.html for exact nesting).
- Command card (repeat this exact structure per command):
  ```html
  <div class="cmd-card">
    <div class="cmd-head"><span class="cmd-code">EUS</span><span class="type-badge type-2"><span class="dot"></span>Type 2</span><span class="cmd-desc">Thai description of what the command does</span></div>
    <div class="cmd-args">
      <div class="lbl">Argument 1</div><div class="val">0 fix [Ch1]</div>
      <div class="lbl">Argument 2</div><div class="val">0: OFF &nbsp; 1: ON</div>
    </div>
  </div>
  ```
  - `type-1` / `type-2` / `type-3` / `type-4` map exactly to the source's "Type 1/2/3/4" column —
    never guess or renumber, copy the number shown in the raw text.
  - If a command has no visible Type number in the raw text (rare, some very short entries), omit
    the badge rather than inventing a number.
  - `.cmd-args` rows: use the exact label from the source (`Argument 1`, `Argument 2`, `Argument
    3`, `Read value 1`, `Read value 2`, ...) — do not translate these labels, they are technical
    labels. If a command has NO arguments/read-values (some Type 1 commands are bare), omit the
    `.cmd-args` block entirely.
  - If the source has an extra explanatory bullet under the command (e.g. "Calculates the
    physical quantity conversion coefficient...") put it in `<div class="cmd-note">...</div>`
    between `.cmd-head` and `.cmd-args`, translated to Thai — see `YES`/`YEU` in the example.
- `<span class="code">XYZ</span>` — inline monospace for a standalone command name, unit
  abbreviation, or key name mentioned in prose (not inside a cmd-card).
- `<div class="codeblock">...</div>` — for a literal multi-command string example, e.g.
  `AMS2AND16AST + terminator`.
- `.table-wrap > table` (with `<thead>`/`<tbody>`) — for genuine tabular spec data that is NOT a
  command list (e.g. pin-out tables, communication spec tables). Most of your pages ARE command
  lists, so you'll mostly use `.cmd-card`, not raw tables.
- `<div class="note">...</div>` / `<div class="warning">...</div>` — for informational asides /
  cautions in the source (marked with a caution or "!" icon).
- Numbers, ranges, units (`dB`, `Hz`, `E-19f`, channel counts, etc.) are NEVER translated — copy
  them verbatim, including scientific notation and the minus sign style (`&minus;` entity, not a
  hyphen, matches the example).

## Translation conventions (match these words for consistency across the whole book)

- "Sets ..." → "ตั้งค่า..." (Type 2 commands)
- "Reads ..." / "Obtains ..." → "อ่าน..." (Type 3/4 commands)
- "Executes ..." → "สั่งให้..." or "อ่าน/ทำ..." matching the actual action (see `STE` in example)
- Keep the original English command/parameter/class name in parentheses after first mention in a
  heading, e.g. "การตั้งค่า EU (EU Setting)" — the example page does this throughout.
- Do not summarize or drop any command — every command row in the raw text must appear as its own
  `.cmd-card`. This is a reference manual; completeness matters more than brevity.
- Natural, plain technical Thai — same register as the example page. Not overly formal, not
  casual.

## Page numbers with no new content (rare)

If a page is essentially a continuation with no visible heading and just more `.cmd-card`s,
that's normal — just keep emitting cards, no `<h3>` needed.

## When you're done

List the page files you wrote. Do not touch any file outside `translated/pNNN.html` for pages in
your assigned range. Do not modify `p017.html` (the reference example) or any other existing
file.
