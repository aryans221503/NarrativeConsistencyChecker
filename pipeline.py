import pandas as pd

from src.load_data import load_test_csv
from src.load_novels import load_novel_text
from src.chunking import chunk_text
from src.embeddings import embed_chunks
from src.vector_store import SimpleVectorStore
from src.claims import extract_claims
from src.evidence import retrieve_evidence
from src.reasoning import judge_claim
from src.classifier import final_decision


def main():
    print("STEP 6: Final Reasoning + results.csv")

    test_df = load_test_csv()

    # Load novels once
    monte_text = load_novel_text("data/novels/monte_cristo.txt")
    cast_text = load_novel_text("data/novels/castaways.txt")

    monte_chunks = chunk_text(monte_text)
    cast_chunks = chunk_text(cast_text)

    monte_store = SimpleVectorStore(monte_chunks, embed_chunks(monte_chunks))
    cast_store = SimpleVectorStore(cast_chunks, embed_chunks(cast_chunks))

    results = []

    for idx, row in test_df.iterrows():
        # ---- FIX THIS COLUMN NAME IF NEEDED ----
        backstory = row["content"]  # change if column name differs
        story = row["book_name"]                        # monte_cristo / castaways

        store = monte_store if story == "monte_cristo" else cast_store

        claims = extract_claims(backstory)

        verdicts = []
        for claim in claims:
            evidence = retrieve_evidence(claim, store, top_k=3)
            verdict = judge_claim(claim, evidence)
            verdicts.append(verdict)

        prediction = final_decision(verdicts)

        results.append({
            "StoryID": idx,
            "Prediction": prediction
        })

    # Save results.csv
    results_df = pd.DataFrame(results)
    results_df.to_csv("results.csv", index=False)

    print("results.csv generated successfully")


if __name__ == "__main__":
    main()
