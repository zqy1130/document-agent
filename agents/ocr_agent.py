from paddleocr import PaddleOCR

ocr_model = PaddleOCR(use_angle_cls=True, lang='ch')

def run_ocr(image_path):
    result = ocr_model.ocr(image_path)

    texts = []

    for line in result[0]:
        texts.append(line[1][0])

    return texts
