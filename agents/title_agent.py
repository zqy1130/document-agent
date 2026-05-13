import re

TITLE_PATTERNS = [
    r'^一、',
    r'^二、',
    r'^三、',
    r'^\（一\）',
    r'^\d+\.',
]

def detect_title(text):
    for p in TITLE_PATTERNS:
        if re.match(p, text):
            return True

    return False
