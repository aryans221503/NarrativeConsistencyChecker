def load_novel_text(path):
    """
    Loads full novel text from a .txt file.
    Returns a single large string.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text
