from src.embeddings import embed_query


def retrieve_evidence(claim, vector_store, top_k=5):
    """
    Retrieves top_k relevant chunks for a claim
    """

    claim_embedding = embed_query(claim)
    evidence_chunks = vector_store.search(claim_embedding, top_k=top_k)

    return evidence_chunks
