import json
import os

def load_questions(filepath):
    """
    Loads questions from a JSON file.
    Returns an empty list if the file doesn't exist to prevent hard crashes.
    """
    if not os.path.exists(filepath):
        print(f"Warning: Question data missing at {filepath}")
        return []
        
    with open(filepath, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Question data is corrupted.")
            return []

def get_topics(questions):
    """
    Extracts a list of unique topics from the loaded questions.
    """
    topics = set()
    for q in questions:
        topics.add(q.get("topic", "Unknown"))
    return sorted(list(topics))

def get_questions_by_topic(questions, topic):
    """
    Filters the questions by a specific topic.
    """
    return [q for q in questions if q.get("topic", "").lower() == topic.lower()]
