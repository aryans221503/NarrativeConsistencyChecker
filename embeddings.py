from sentence_transformers import SentenceTransformer


def embed_chunks(chunks):
    """
    Takes a list of text chunks
    Returns a list of embedding vectors
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings

def embed_query(query):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode(query)

