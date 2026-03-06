import re


def sanitize_input(text: str):

    text = text.strip()

    # remove dangerous SQL patterns
    text = re.sub(r"[;'\"]", "", text)

    return text