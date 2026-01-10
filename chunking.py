def chunk_text(text, chunk_size=1000, overlap=200):
    """
    Splits long text into overlapping word-based chunks.

    text: full novel text (string)
    chunk_size: number of words per chunk
    overlap: number of overlapping words between chunks
    """

    words = text.split()
    chunks = []

    start = 0
    total_words = len(words)

    while start < total_words:
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)
        chunks.append(chunk_text)

        # move start forward with overlap
        start = end - overlap

        if start < 0:
            start = 0

    return chunks
