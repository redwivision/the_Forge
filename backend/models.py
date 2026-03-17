from pydantic import BaseModel
from typing import List

class Topic(BaseModel):
    id: str
    name: str
    prerequisites: List[str] = []
    mastery_score: float = 0.0

class Problem(BaseModel):
    id: str
    topic_id: str
    question: str
    answer: str
    difficulty: int
