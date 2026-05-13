from parser.pdf_parser import parse_pdf
from parser.docx_parser import parse_docx

def route_file(path):
    if path.endswith(".pdf"):
        return parse_pdf(path)

    if path.endswith(".docx"):
        return parse_docx(path)

    return {"error": "unsupported file"}
