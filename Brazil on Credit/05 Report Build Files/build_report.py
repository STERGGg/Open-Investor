"""Builds the Word report from report_text.md, the charts in ../outputs/charts and references.txt."""
import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = Path(__file__).parent
CH = HERE.parent / "04 Outputs" / "charts"
NAVY = RGBColor(0x14, 0x2B, 0x4F)
BLUE = RGBColor(0x2A, 0x78, 0xD6)
GREY = RGBColor(0x52, 0x51, 0x4E)

doc = Document()
sec = doc.sections[0]
sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
for side in ("left_margin", "right_margin"):
    setattr(sec, side, Cm(2.3))
sec.top_margin = sec.bottom_margin = Cm(2.2)

st = doc.styles["Normal"]
st.font.name = "Calibri"; st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
st.paragraph_format.space_after = Pt(7)
st.paragraph_format.line_spacing = 1.15
for name, size, color in (("Heading 1", 17, NAVY), ("Heading 2", 13, BLUE), ("Title", 30, NAVY)):
    h = doc.styles[name]; h.font.name = "Calibri"; h.font.size = Pt(size); h.font.color.rgb = color; h.font.bold = True
    rpr = h.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rf.set(qn(a), "Calibri")
doc.styles["Heading 1"].paragraph_format.space_before = Pt(6)
doc.styles["Heading 1"].paragraph_format.space_after = Pt(10)
doc.styles["Heading 2"].paragraph_format.space_before = Pt(10)


def shade(cell, hexcol):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexcol)
    tcPr.append(shd)


def borders(cell, color="2A78D6"):
    tcPr = cell._tc.get_or_add_tcPr(); b = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "18" if edge == "left" else "4"); e.set(qn("w:color"), color if edge == "left" else "D6E4F5")
        b.append(e)
    tcPr.append(b)


def add_runs(p, text):
    """Supports **bold** and keeps citations in brackets in a muted colour."""
    parts = re.split(r"(\*\*[^*]+\*\*|\[[A-Z0-9, ]+\])", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**"):
            r = p.add_run(part[2:-2]); r.bold = True
        elif re.fullmatch(r"\[[A-Z0-9, ]+\]", part):
            r = p.add_run(part); r.font.color.rgb = GREY; r.font.size = Pt(9)
        else:
            p.add_run(part)


def page_number_footer():
    p = sec.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run()
    for tag, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), tag); r._r.append(f)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; r._r.append(it)
    r.font.size = Pt(9); r.font.color.rgb = GREY

page_number_footer()

# Cover
for _ in range(5):
    doc.add_paragraph()
t = doc.add_paragraph(style="Title"); t.add_run("Brazil on Credit")
p = doc.add_paragraph(); r = p.add_run("Lula, the Bolsonaros and a country paying 445% on its credit cards")
r.font.size = Pt(15); r.font.color.rgb = BLUE
doc.add_paragraph()
p = doc.add_paragraph(); r = p.add_run("Independent research project, October 2026"); r.font.size = Pt(11); r.font.color.rgb = GREY
doc.add_paragraph()
p = doc.add_paragraph(); r = p.add_run("Nine Python models built on official data from the Banco Central do Brasil, the IMF and Nasdaq.")
r.italic = True; r.font.size = Pt(10.5); r.font.color.rgb = GREY
p.add_run().add_break(WD_BREAK.PAGE)

text = (HERE / "report_text.md").read_text()
blocks = [b.strip("\n") for b in re.split(r"\n\s*\n", text) if b.strip()]

# Contents page from the headings
doc.add_heading("Contents", level=1)
for b in blocks:
    if b.startswith("# "):
        p = doc.add_paragraph(b[2:].replace("  ", "   ")); p.paragraph_format.space_after = Pt(3)
    elif b.startswith("## "):
        p = doc.add_paragraph(b[3:]); p.paragraph_format.left_indent = Cm(0.8); p.paragraph_format.space_after = Pt(2)
        for r in p.runs: r.font.size = Pt(10); r.font.color.rgb = GREY
p = doc.add_paragraph("References"); p.paragraph_format.space_after = Pt(3)
doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

first_h1 = True
for b in blocks:
    if b.startswith("# "):
        title = b[2:]
        hp = doc.add_heading(title.replace("  ", "   "), level=1)
        if not first_h1:
            hp.paragraph_format.space_before = Pt(20)
        first_h1 = False
    elif b.startswith("## "):
        doc.add_heading(b[3:], level=2)
    elif b.startswith("[FIG") or b.startswith("[COMIC"):
        fn = re.match(r"\[(?:FIG|COMIC) ([^\]]+)\]", b).group(1).strip()
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        src = (CH / fn) if b.startswith("[FIG") else (HERE.parent / "04 Outputs" / "comics" / fn)
        width = Cm(15.5) if b.startswith("[FIG") else Cm(12.5)
        p.add_run().add_picture(str(src), width=width)
        p.paragraph_format.space_after = Pt(10)
    elif b.startswith("> Q:"):
        lines = [l[2:] for l in b.split("\n")]
        q = lines[0][3:].strip(); a = " ".join(l[3:].strip() if l.startswith("A:") else l for l in lines[1:])
        tbl = doc.add_table(rows=1, cols=1); tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        trPr = tbl.rows[0]._tr.get_or_add_trPr(); cs = OxmlElement("w:cantSplit"); trPr.append(cs)
        c = tbl.rows[0].cells[0]; shade(c, "EEF4FC"); borders(c)
        p = c.paragraphs[0]; r = p.add_run("Question  "); r.bold = True; r.font.color.rgb = BLUE; r.font.size = Pt(10)
        r = p.add_run(q); r.bold = True; r.font.size = Pt(10.5)
        p2 = c.add_paragraph(); r = p2.add_run("Answer  "); r.bold = True; r.font.color.rgb = BLUE; r.font.size = Pt(10)
        add_runs(p2, a)
        for r in p2.runs[1:]:
            if r.font.size is None: r.font.size = Pt(10.5)
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
    else:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_runs(p, b)

doc.add_page_break()
doc.add_heading("References", level=1)
for line in (HERE / "references.txt").read_text().strip().split("\n"):
    key, desc, url = line.split("|")
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(f"[{key}]  "); r.bold = True; r.font.size = Pt(9.5)
    r = p.add_run(desc + " "); r.font.size = Pt(9.5)
    r = p.add_run(url); r.font.size = Pt(8.5); r.font.color.rgb = GREY

doc.core_properties.author = ""
doc.core_properties.last_modified_by = ""
doc.core_properties.title = "Brazil on Credit"
out = HERE / "Brazil on Credit.docx"
doc.save(out)
print("saved", out)
