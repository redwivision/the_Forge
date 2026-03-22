from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
from Models import Topic, Problem
from logic import get_next_recommendation
from database import engine, create_db_and_tables, get_session
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Create the file (forge.db) and tables
    create_db_and_tables()
    
    # 2. Seed the DB if it's empty
    with Session(engine) as session:
        statement = select(Topic)
        results = session.exec(statement).all()
        if not results:
            print("🌱 Seeding initial topics into the Forge...")
            initial_topics = [
                Topic(id="arithmetic", name="Basic Arithmetic", prerequisites_raw="", mastery_score=0.0),
                Topic(id="algebra", name="Linear Equations", prerequisites_raw="arithmetic", mastery_score=0.0),
                Topic(id="vectors", name="Vector Basics", prerequisites_raw="algebra", mastery_score=0.0),
                Topic(id="forces", name="Newton's Second Law", prerequisites_raw="vectors", mastery_score=0.0),
            ]
            for topic in initial_topics:
                session.add(topic)
            problems = [
                Problem(id="p1", topic_id="arithmetic", question="What is 2 + 2?", answer="4", difficulty=1),
                Problem(id="p2", topic_id="arithmetic", question="What is 3 * 3?", answer="9", difficulty=1),
                Problem(id="p3", topic_id="algebra", question="Solve for x: x + 2 = 5", answer="3", difficulty=2),
                Problem(id="p4", topic_id="algebra", question="Solve for x: 2x = 6", answer="3", difficulty=2),
                Problem(id="p5", topic_id="vectors", question="What is the dot product of [1, 2] and [3, 4]?", answer="11", difficulty=3),
                Problem(id="p6", topic_id="vectors", question="What is the cross product of [1, 2, 3] and [4, 5, 6]?", answer="[-3, 6, -3]", difficulty=3),
                Problem(id="p7", topic_id="forces", question="What is the force required to accelerate a 10kg mass at 2m/s^2?", answer="20N", difficulty=4),
                Problem(id="p8", topic_id="forces", question="What is the acceleration of a 10kg mass with a force of 20N applied to it?", answer="2m/s^2", difficulty=4),
            ]
            for problem in problems:
                session.add(problem)
            session.commit()
    yield
    engine.dispose()

app = FastAPI(title="The Forge API", lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "The Forge is hot. SQLite power is now online, Red."}

@app.get("/topics")
def list_topics(session: Session = Depends(get_session)):
    """Returns the entire Knowledge Graph from the Database."""
    statement = select(Topic)
    results = session.exec(statement).all()
    return results

@app.get("/recommendation")
def suggest_next(session: Session = Depends(get_session)):
    """Calls the Brain with data from the Database."""
    statement = select(Topic)
    topics = session.exec(statement).all()
    recommendation = get_next_recommendation(topics)
    if not recommendation:
        return {"status": "Complete", "message": "All topics mastered. The Forge is cold."}
    return recommendation

@app.post("/evaluate/{topic_id}")
def complete_topic(topic_id: str, session: Session = Depends(get_session)):
    """Permanent progress update."""
    statement = select(Topic).where(Topic.id == topic_id)
    topic = session.exec(statement).first()
    
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    topic.mastery_score = 100.0
    session.add(topic)
    session.commit()
    session.refresh(topic)
    
# --- TOPIC CRUD ---

@app.post("/topics", response_model=Topic)
def create_topic(topic: Topic, session: Session = Depends(get_session)):
    """Add a new concept to the Forge."""
    session.add(topic)
    session.commit()
    session.refresh(topic)
    return topic

@app.get("/topics/{topic_id}", response_model=Topic)
def get_topic(topic_id: str, session: Session = Depends(get_session)):
    """Deep-dive into a single topic."""
    topic = session.get(Topic, topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic

@app.patch("/topics/{topic_id}", response_model=Topic)
def update_topic(topic_id: str, update_data: dict, session: Session = Depends(get_session)):
    """Refine a topic (change name, difficulty, etc)."""
    topic = session.get(Topic, topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # partial update logic
    for key, value in update_data.items():
        if hasattr(topic, key):
            setattr(topic, key, value)
    
    session.add(topic)
    session.commit()
    session.refresh(topic)
    return topic

@app.delete("/topics/{topic_id}")
def delete_topic(topic_id: str, session: Session = Depends(get_session)):
    """Purge a mistake from the memory."""
    topic = session.get(Topic, topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    session.delete(topic)
    session.commit()
    return {"status": "Success", "message": f"Topic '{topic_id}' deleted."}

# --- PROBLEM CRUD ---

@app.post("/problems", response_model=Problem)
def create_problem(problem: Problem, session: Session = Depends(get_session)):
    """Add a new challenge to the bank."""
    session.add(problem)
    session.commit()
    session.refresh(problem)
    return problem

@app.get("/problems/{problem_id}", response_model=Problem)
def get_problem(problem_id: str, session: Session = Depends(get_session)):
    """Retrieve a specific challenge."""
    problem = session.get(Problem, problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem

@app.patch("/problems/{problem_id}", response_model=Problem)
def update_problem(problem_id: str, update_data: dict, session: Session = Depends(get_session)):
    """Fix a typo or update the answer."""
    problem = session.get(Problem, problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    for key, value in update_data.items():
        if hasattr(problem, key):
            setattr(problem, key, value)
    
    session.add(problem)
    session.commit()
    session.refresh(problem)
    return problem

@app.delete("/problems/{problem_id}")
def delete_problem(problem_id: str, session: Session = Depends(get_session)):
    """Remove a problematic challenge."""
    problem = session.get(Problem, problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    session.delete(problem)
    session.commit()
    return {"status": "Success", "message": f"Problem '{problem_id}' deleted."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
