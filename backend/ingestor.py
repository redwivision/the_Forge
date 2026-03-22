import fitz  # PyMuPDF
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file immediately
load_dotenv()

from sqlmodel import Session
from database import engine
from Models import Topic, Problem

# --- THE FORGE: SMART SIEVE (STAGE 1: THE SCOUT) ---

class ForgeIngestor:
    def __init__(self, api_key: str = None):
        if not api_key:
            api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("API Key not found. Set GOOGLE_API_KEY environment variable.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-3-flash-preview')

    def scout_pdf(self, pdf_path: str):
        """
        Stage 1: The Scout
        Extracts the Table of Contents and maps the chapter 'Battlefield'.
        """
        print(f"📖 Opening PDF: {pdf_path}")
        doc = fitz.open(pdf_path)
        print(f"📄 PDF Opened. Total Pages: {len(doc)}")
        
        toc = doc.get_toc()
        
        # If the PDF has no built-in TOC, we scan the first 15 pages for a 'Contents' page
        if not toc:
            print("🔍 No built-in TOC found. Sifting through first 15 pages...")
            toc_text = ""
            for i in range(min(15, len(doc))):
                print(f"  - Reading Page {i+1}...")
                toc_text += doc[i].get_text()
            
            print("🧠 Sending TOC to Gemini for analysis...")
            return self._analyze_toc_with_ai(toc_text)
        
        return {"status": "success", "toc": toc}

    def sift_chapter(self, pdf_path: str, start_page: int, end_page: int):
        """
        Stage 2: The Sifter
        Extracts a specific range of pages and filters them for gold (Topics & Problems).
        """
        print(f"🌪️ Sifting Chapter from page {start_page} to {end_page}...")
        raw_text = self._extract_text_range(pdf_path, start_page, end_page)
        
        print("🧠 Analyzing content with AI...")
        return self._sift_content_with_ai(raw_text)

    def _extract_text_range(self, pdf_path: str, start: int, end: int):
        doc = fitz.open(pdf_path)
        text = ""
        # fitz is 0-indexed, so we adjust if the Scout returned 1-indexed printed pages
        for i in range(start - 1, min(end, len(doc))):
            text += doc[i].get_text()
        return text

    def _sift_content_with_ai(self, raw_text: str):
        """
        The Filter: Extracts 'Gold' (Topics and Problems) from raw 'Junk'.
        """
        prompt = f"""
        You are the 'Sifter' for The Forge Learning Engine. 
        I am giving you the raw text from a chapter of a Physics textbook.
        
        Your goal is to extract:
        1. **Topics**: Clear, nameable concepts (e.g. 'Scalars and Vectors').
        2. **Problems**: Actual exercises or test questions found in the text.
        
        Ignore introductory 'fluff', learning objectives, or blank pages.
        
        Output ONLY a JSON object:
        {{
            "topics": [
                {{"id": "vectors", "name": "Scalars and Vectors", "mastery_score": 0.0}}
            ],
            "problems": [
                {{"id": "p1", "topic_id": "vectors", "question": "...", "answer": "..."}}
            ]
        }}
        
        TEXT:
        {raw_text[:8000]} 
        """
        
        response = self.model.generate_content(prompt)
        try:
            clean_json = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(clean_json)
        except json.JSONDecodeError:
            print("❌ Error: Sifter failed to parse JSON.")
            return {"error": "sifting_failed", "raw": response.text}

    def _analyze_toc_with_ai(self, raw_text: str):
        """
        Uses Gemini to turn a messy Table of Contents into a clean Chapter Map.
        """
        prompt = f"""
        You are the 'Scout' for The Forge Learning Engine. 
        I am giving you the raw text from the first few pages of a Physics textbook.
        Your goal is to extract the main Chapters and their starting page numbers.
        
        Output ONLY a JSON list of objects:
        [
            {{"title": "Chapter 1: Measurement", "page": 10}},
            {{"title": "Chapter 2: Motion", "page": 45}}
        ]
        
        RAW TEXT:
        {raw_text[:5000]} 
        """
        
        response = self.model.generate_content(prompt)
        try:
            clean_json = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(clean_json)
        except json.JSONDecodeError:
            print("❌ Error: Scout failed to parse JSON.")
            return {"error": "failed_to_parse_toc", "raw": response.text}

    def mine_to_db(self, sifted_data: dict):
        """
        Stage 4: The Miner (Sync to DB)
        Takes the AI JSON and commits it to the SQLite database.
        """
        print("⛏️ Mining data to database...")
        with Session(engine) as session:
            # 1. Add Topics
            for t_data in sifted_data.get("topics", []):
                topic = Topic(
                    id=t_data["id"],
                    name=t_data["name"],
                    mastery_score=t_data.get("mastery_score", 0.0)
                )
                session.merge(topic) # Use merge to update if exists
            
            # 2. Add Problems
            for p_data in sifted_data.get("problems", []):
                problem = Problem(
                    id=p_data["id"],
                    topic_id=p_data["topic_id"],
                    question=p_data["question"],
                    answer=p_data["answer"],
                    difficulty=p_data.get("difficulty", 2)
                )
                session.merge(problem)
            
            session.commit()
            print("✅ Database sync complete!")

if __name__ == "__main__":
    PDF_PATH = "/Users/Learning/Desktop/projects/the_forge/grade 9-physics.pdf"
    
    try:
        scout = ForgeIngestor()
        
        # Stage 1: Scout
        print("--- STAGE 1: THE SCOUT ---")
        battle_map = scout.scout_pdf(PDF_PATH)
        
        if isinstance(battle_map, list) and len(battle_map) > 1:
            # Stage 2: Sifter (Chapter 2)
            print("\n--- STAGE 2: THE SIFTER ---")
            ch2 = battle_map[1]
            ch3_start = battle_map[2]["page"] if len(battle_map) > 2 else ch2["page"] + 20
            
            sifted_gold = scout.sift_chapter(PDF_PATH, ch2["page"], ch3_start)
            
            # Stage 4: Miner (Sync to DB)
            if "error" not in sifted_gold:
                scout.mine_to_db(sifted_gold)
            else:
                print(f"❌ Sifting failed: {sifted_gold}")
            
    except Exception as e:
        print(f"Test Failed: {e}")
        import traceback
        traceback.print_exc()
