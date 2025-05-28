# `mermaid-flow.md`

## 📘 Overview

This document provides a structured system overview of the **Symbolic Dissonance** tool using a Mermaid.js flowchart. The tool's primary function is to detect metaphor used as **epistemic sedative**—that is, language that obscures clarity or masks cognitive dissonance under the guise of profundity—and offer alternatives grounded in higher epistemic utility. It leverages contextual awareness and large language models (LLMs) to analyze and reframe language in real time.

---

## 🧠 System Architecture

```mermaid
graph TD
    A[User Input (Text)] --> B[Preprocessing]
    B --> C[Context Windowing]
    C --> D[LLM Inference]
    D --> E[Metaphor Detection Module]
    E --> F{Metaphor as Sedative?}
    F -->|Yes| G[Suggest Replacement Metaphor]
    F -->|No| H[Pass-through]
    G --> I[Structured Output]
    H --> I
```

---

## 🔍 Component Breakdown

### A. User Input

* Raw input: sentence, paragraph, or stream of prose
* CLI-based in initial implementation

### B. Preprocessing

* Text normalization
* Tokenization (if needed)
* Removal of noise or formatting inconsistencies

### C. Context Windowing

* Defines a local textual window (e.g., 2-3 paragraphs before and after)
* Optionally uses embedding similarity to find semantic anchors

### D. LLM Inference

* Runs selected LLM (e.g., GPT-style or fine-tuned BERT/DistilBERT) on the context
* Extracts interpretive signals, patterns, or latent tensions in language use

### E. Metaphor Detection Module

* Looks for metaphorical phrases
* Flags metaphors historically used in ML/AI, e.g., “hallucination,” “black box,” “emergent,” “understanding”
* Applies pattern rules and model-attested metaphor embeddings

### F. Sedative Filter

* Uses heuristics or trained classifier to distinguish “productive” vs “sedative” metaphors
* Considers emotional tone, structural displacement, epistemic weight

### G. Replacement Suggestion

* Surfaces candidate metaphors or literal reframings
* Grounds them in ontology-aligned language and descriptive clarity

### H. Pass-through

* If metaphor is not sedative, text remains unaltered

### I. Structured Output

* Final text rendered for user
* Highlighted metaphor tags (optional)
* Suggested edits in diff-style output

---

## 🧰 Planned Extensions

* Rich CLI with `--context`, `--threshold`, and `--explain` flags
* VS Code plugin with hover tooltips and edit suggestions
* Plug-in architecture for metaphor ontologies and cultural lexicons

---

