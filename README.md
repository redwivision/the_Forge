# 🗡️ THE FORGE — Adaptive Learning Engine

*"Knowledge is not a library; it is a weapon. Forge it accordingly."*

---

## 🏔️ The Vision
**The Forge** is a high-performance knowledge engine designed to eliminate passive learning. Instead of just "reading," the student is guided through a **Directed Acyclic Graph (DAG)** of concepts, where each step must be mastered before the next is unlocked.

This system is the **Intelligence Module** of the JARVIS ecosystem.

---

## 🏗️ Technical Stack
- **Backend**: Python (FastAPI) 🐍
- **Models**: Pydantic (Strong Typing) 📐
- **Intelligence**: Custom Adaptive Recommendation Algorithm 🧠
- **Testing**: Automated Integration Test Suite 🧪

---

## 🗺️ Project Structure
```text
the_forge/
├── backend/
│   ├── Models.py       # Data Blueprints (Topic, Problem)
│   ├── logic.py        # The Decision Engine (Tutor)
│   ├── seed_data.py    # The Knowledge Graph (Physics/Math)
│   ├── main.py         # The FastAPI Logic Bridge
│   └── test_api.py     # Automated Stress Tests
├── MISSION.md          # Project Goals & Roadmap
└── README.md           # You are here
```

---

## ⚡ Level 1 & 2: Completed Foundations
- [x] **The Brain**: Implemented a graph-based recommendation engine that understands prerequisites.
- [x] **The Bridge**: Built a FastAPI server to expose the logic to external clients (Flutter/JARVIS).
- [x] **The Test**: Built an automated suite to simulate a student's journey.

---

## 🚀 The Future: Level 3 — RAG & PDF Ingestion
The next phase of The Forge will turn it into a true AI powerhouse:
- **Auto-Extraction**: Ingest PDF textbooks directly.
- **RAG (Retrieval Augmented Generation)**: Use LLMs to automatically generate the Knowledge Graph and Problem Bank.
- **JARVIS Link**: Real-time study planning for the JARVIS Assistant.

---

## 🧪 How to Run
1. Navigate to `backend/`
2. Install dependencies: `pip install fastapi uvicorn pydantic requests`
3. Start the server: `uvicorn main:app --reload`
4. Run tests: `python3 test_api.py`

*"We aren't building a study app. We are building the memory of an AI."* 🏗️🏛️🐐
