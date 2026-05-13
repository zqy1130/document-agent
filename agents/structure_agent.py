from agents.title_agent import detect_title

def build_structure(lines):
    result = {
        "title": "文档",
        "content": []
    }

    current = None

    for line in lines:

        if detect_title(line):

            current = {
                "title": line,
                "content": ""
            }

            result["content"].append(current)

        else:

            if current:
                current["content"] += line + "\n"

    return result
