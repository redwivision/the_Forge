from sqlmodel import SQLModel, Field
from typing import List, Optional

class Topic(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    # Prerequisites are IDs, which we'll handle as a simple mapping for now.
    # Note: SQLModel can't store List[str] in SQLite directly without a relation,
    # so we'll store it as a comma-separated string or just use our RAM-based logic
    # for Level 2.5 and migrate to relations in Level 3.
    # For now, let's keep it simple:
    prerequisites_raw: str = "" # "topic1,topic2"
    mastery_score: float = 0.0

class Problem(SQLModel, table=True):
    id: str = Field(primary_key=True)
    topic_id: str
    question: str
    answer: str
    difficulty: int
