# 🎯 THE FORGE — MISSION CONTROL

*"Knowledge is not a library; it is a weapon. Forge it accordingly."*

---

## 🏔️ The Vision: The JARVIS Knowledge Engine
The Forge is NOT just an app. It is the **Intelligence Module** of the JARVIS ecosystem.
- **Goal**: Feed JARVIS a PDF textbook. 
- **Process**: LLM parses the PDF → Identifies Concepts (Topics) → Extracts Problems → Maps the Graph.
- **Output**: An adaptive study loop that tells Red exactly what to forge next.

---

## 🏛️ The Architecture: The "Graph" (The Bridge to RAG)
You asked: *"Why define topics and problems this way?"*
**The Answer**: This is our **Target Schema**. 
When we later build the **RAG (Retrieval Augmented Generation)** feature, the AI needs a "format" to output its findings. We are telling the AI: *"When you read this Physics book, I want you to give me a list of `Topic` objects and `Problem` objects that fit this specific structure."*

### Why a List in `seed_data.py`?
In programming, a `List` is a simple collection. Right now, it's manually written. Tomorrow, it will be the output of our PDF parser. By building the `logic.py` on top of this list now, we ensure the "Brain" works *before* the "Parser" is even built.

---

## 🗡️ The Roadmap (Updated for RAG Vision)

### Level 1: The Core logic (Manual Entry) — CURRENT
Build the engine that can "navigate" a graph of knowledge.
- [x] **Skeleton**: The `Topic` and `Problem` Blueprints.
- [x] **Muscles**: Manually seeded data for testing the brain.
- [/] **Nervous System**: The "Logic" that decides what is next.

### Level 2: The Logic Bridge (FastAPI)
Expose the Forge as a service that JARVIS can talk to.

### Level 3: The Intelligence Layer (PDF & RAG)
- **PDF Extraction**: Convert page text to raw data.
- **RAG Implementation**: Use LLMs to "auto-tag" and "auto-graph" the textbook.
- **JARVIS Link**: "JARVIS, Red has a Physics test. What's the plan?"

---

## 🎓 Why This Project Matters
This project will teach you the 3 most important skills in Software Engineering:
1. **Data Structures**: Using Graphs to represent complex knowledge.
2. **State Management**: Tracking mastery across a non-linear path.
3. **Algorithmic Thinking**: Building the "Brain" that JARVIS will eventually use.

*"We aren't building a study app. We are building the memory of an AI."*
