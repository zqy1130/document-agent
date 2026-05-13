from docx import Document
from agents.structure_agent import build_structure

def parse_docx(path):
    doc = Document(path)

    lines = []

    for p in doc.paragraphs:
        if p.text.strip():
            lines.append(p.text.strip())

    return build_structure(lines)
