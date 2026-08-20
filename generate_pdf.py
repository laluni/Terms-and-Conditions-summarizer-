"""
Script to generate a PDF report from the NLP_Team_Report_Exp1_to_5.md markdown document.
Uses reportlab and markdown or weasyprint.
"""
import os
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors

def generate_pdf():
    md_path = os.path.join("docs", "NLP_Team_Report_Exp1_to_5.md")
    pdf_path = os.path.join("docs", "NLP_Laboratory_Assignment_Team_Report.pdf")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1A365D"),
        alignment=1, # Center
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'ExpHeader',
        parent=styles['Heading1'],
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h3_style = ParagraphStyle(
        'SubHeader',
        parent=styles['Heading3'],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['BodyText'],
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Code'],
        fontSize=8,
        leading=11,
        fontName='Courier',
        textColor=colors.HexColor("#1A202C"),
        backColor=colors.HexColor("#EDF2F7"),
        spaceBefore=4,
        spaceAfter=6
    )

    story = []
    
    lines = md_text.split("\n")
    in_code_block = False
    code_lines = []

    for line in lines:
        raw = line.strip()
        
        # Handle code blocks
        if raw.startswith("```"):
            if in_code_block:
                in_code_block = False
                story.append(Paragraph("<br/>".join(code_lines).replace(" ", "&nbsp;"), code_style))
                code_lines = []
            else:
                in_code_block = True
                code_lines = []
            continue
        
        if in_code_block:
            code_lines.append(raw.replace("<", "&lt;").replace(">", "&gt;"))
            continue

        if not raw:
            story.append(Spacer(1, 4))
            continue

        if raw.startswith("# "):
            if "Experiment" in raw:
                story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E0"), spaceBefore=10, spaceAfter=10))
                story.append(Paragraph(raw.replace("# ", ""), h1_style))
            else:
                story.append(Paragraph(raw.replace("# ", ""), title_style))
        elif raw.startswith("### "):
            story.append(Paragraph(raw.replace("### ", ""), h3_style))
        elif raw.startswith("---"):
            story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E2E8F0"), spaceBefore=6, spaceAfter=6))
        else:
            clean_line = raw.replace("**", "<b>").replace("__", "<b>").replace("`", "<font name='Courier'>").replace("<font name='Courier'>", "<font name='Courier'>", 1)
            # Basic bold formatting
            parts = clean_line.split("<b>")
            formatted = ""
            for idx, p in enumerate(parts):
                if idx % 2 == 1:
                    formatted += f"<b>{p}</b>"
                else:
                    formatted += p
            
            # Simple markdown bullet handling
            if raw.startswith("- ") or raw.startswith("* "):
                bullet_text = "&bull; " + raw[2:].replace("<", "&lt;").replace(">", "&gt;")
                story.append(Paragraph(bullet_text, body_style))
            elif raw.startswith("|"):
                # Table rows handled as small mono text if needed
                story.append(Paragraph(raw.replace("<", "&lt;").replace(">", "&gt;"), code_style))
            else:
                story.append(Paragraph(raw.replace("<", "&lt;").replace(">", "&gt;"), body_style))

    doc.build(story)
    print(f"[SUCCESS] PDF generated at: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
