from sentence_transformers import SentenceTransformer

# Load model only once (important for speed)
_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks):
    """
    Takes a list of text chunks and returns embeddings
    """
    return _model.encode(chunks, show_progress_bar=True)


def embed_query(query):
    """
    Takes a single string query and returns its embedding
    """
    return _model.encode(query)


def judge_claim_against_chunk(claim, chunk):
    claim = claim.lower()
    chunk = chunk.lower()

    if "never" in chunk and any(w in chunk for w in claim.split()):
        return "CONTRADICT"

    if "refused" in chunk and any(w in chunk for w in claim.split()):
        return "CONTRADICT"

    if any(w in chunk for w in claim.split()):
        return "SUPPORT"

    return "UNCLEAR"


def score_verdict(verdict):
    if verdict == "SUPPORT":
        return 1
    if verdict == "CONTRADICT":
        return -2
    return 0

from collections import Counter


def aggregate_claim_verdict(chunk_verdicts):
    counts = Counter(chunk_verdicts)

    if counts["CONTRADICT"] >= 2:
        return "CONTRADICT"

    if counts["SUPPORT"] >= 2:
        return "SUPPORT"

    return "UNCLEAR"

def retrieve_evidence_with_position(claim, vector_store, top_k=5):
    claim_embedding = embed_query(claim)

    indices = vector_store.search_indices(claim_embedding, top_k)
    return indices

def temporal_inconsistency(verdicts, indices, total_chunks):
    for v, idx in zip(verdicts, indices):
        if v == "SUPPORT" and idx < total_chunks * 0.3:
            return True
    return False
