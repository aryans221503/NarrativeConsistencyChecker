# 📖 Narrative Consistency Checker

A reasoning-based NLP system that determines whether a **hypothetical character backstory** is **logically consistent** with the narrative of a **full-length novel**.

This project focuses on **long-context reasoning**, **evidence retrieval**, and **LLM-driven classification** to evaluate narrative coherence in fiction.

---

## 🚀 Problem Statement

Given:
- A **full novel** (long-form text)
- A **hypothetical backstory** for a character

The task is to **classify** whether the backstory is:
- ✅ **Consistent** with the narrative, or  
- ❌ **Inconsistent**, based on contradictions or missing evidence.

---

## 🧠 Core Techniques Used

- **Long-Context Chunking**  
  Splitting large narrative text into manageable, semantically coherent chunks.

- **Evidence Retrieval**  
  Identifying the most relevant passages from the novel that relate to the character and events in the backstory.

- **Reasoning-Based Classification**  
  Using LLMs to reason over retrieved evidence and determine logical consistency.

---

## 🏗️ System Architecture

Novel Text
↓
Long-Context Chunking
↓
Evidence Retrieval (Relevant Passages)
↓
LLM Reasoning Engine
↓
Consistency Classification
(Consistent / Inconsistent)


---

## 📂 Project Structure

NarrativeConsistencyChecker/
│
├── data/
│ ├── novels/ # Full novel texts
│ ├── backstories/ # Hypothetical character backstories
│
├── preprocessing/
│ ├── chunking.py # Long-context chunking logic
│
├── retrieval/
│ ├── evidence_retriever.py # Passage retrieval logic
│
├── reasoning/
│ ├── consistency_checker.py # LLM-based reasoning & classification
│
├── utils/
│ ├── text_utils.py
│
├── main.py # End-to-end pipeline
├── requirements.txt
└── README.md


---

## ⚙️ How It Works

1. **Chunk the Novel**  
   The novel is split into overlapping text chunks to preserve narrative context.

2. **Retrieve Evidence**  
   Relevant chunks are selected based on semantic similarity to the backstory.

3. **Reason Over Evidence**  
   A language model evaluates whether the backstory aligns with the retrieved narrative evidence.

4. **Final Classification**  
   Output:
   - `Consistent`
   - `Inconsistent`

---

## 🧪 Example Input

**Backstory:**
> "The character grew up in a coastal town and lost their family in a shipwreck."

**Output:**
❌ Inconsistent
Reason: The narrative states the character was raised inland and their family is alive.


---

## 🛠 Tech Stack

- **Python**
- **Natural Language Processing**
- **Large Language Models (LLMs)**
- **Semantic Search / Embeddings**
- **Prompt-based Reasoning**

---

## 🎯 Use Cases

- Fiction analysis & literary research
- Story validation tools for writers
- Narrative QA systems
- AI-assisted creative writing
- Long-context LLM evaluation

---

## 📈 Future Improvements

- Multi-character consistency checks
- Fine-grained contradiction detection
- Support for multi-novel series
- Confidence scoring for predictions
- Visualization of evidence passages

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests.

---

## 📜 License

This project is licensed under the MIT License.
