import fitz

from agents.ocr_agent import run_ocr
from agents.structure_agent import build_structure

def parse_pdf(pdf_path):
    doc = fitz.open(pdf_path)

    all_pages = []

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)

        pix = page.get_pixmap()

        image_path = f"output/page_{page_index}.png"

        pix.save(image_path)

        texts = run_ocr(image_path)

        all_pages.extend(texts)

    result = build_structure(all_pages)

    return result
