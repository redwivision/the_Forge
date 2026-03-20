from fastapi import FastAPI, HTTPException
from Models import Topic, Problem
from logic import get_next_recommendation
from seed_data import TOPICS

app = FastAPI(title="The Forge API")

# --- THE DATA BRIDGE ---
# In a real app, this would be a database. 
# For now, it's our "In-Memory" storage.
USER_DATA = TOPICS

@app.get("/")
def read_root():
    return {"message": "The Forge is hot. Ready to master your craft, Red?"}

@app.get("/topics")
def list_topics():
    """Returns the entire Knowledge Graph and mastery levels."""
    return USER_DATA

@app.get("/recommendation")
def suggest_next():
    """Calls the Brain to see what Red should forge next."""
    recommendation = get_next_recommendation(USER_DATA)
    if not recommendation:
        return {"status": "Complete", "message": "All topics mastered. The Forge is cold."}
    return recommendation

@app.post("/evaluate/{topic_id}")
def complete_topic(topic_id: str):
    """
    Simulates mastering a topic.
    In the future, this will involve real math/physics problems.
    """
    for topic in USER_DATA:
        if topic.id == topic_id:
            topic.mastery_score = 100.0
            return {"status": "Success", "message": f"Topic '{topic.name}' mastered."}
    
    raise HTTPException(status_code=404, detail="Topic not found")
