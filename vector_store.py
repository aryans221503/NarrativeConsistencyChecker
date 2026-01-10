import numpy as np


class SimpleVectorStore:
    def __init__(self, chunks, embeddings):
        self.chunks = chunks
        self.embeddings = embeddings

    def search(self, query_embedding, top_k=5):
        """
        Returns top_k most similar chunks
        """
        scores = np.dot(self.embeddings, query_embedding)
        top_indices = np.argsort(scores)[-top_k:][::-1]

        return [self.chunks[i] for i in top_indices]

    def search_indices(self, query_embedding, top_k=5):
        scores = np.dot(self.embeddings, query_embedding)
        top_indices = np.argsort(scores)[-top_k:][::-1]
        return top_indices
