from Models import Topic, Problem

TOPICS = [
    Topic(
        id="arithmetic",
        name="Basic Arithmetic",
        prerequisites=[],
        mastery_score=100
    ),
    Topic(
        id="algebra",
        name="Linear Equations",
        prerequisites=["arithmetic"],
        mastery_score=0.0
    ),
    Topic(
        id="vectors",
        name="Vector Basics",
        prerequisites=["algebra"],
        mastery_score=0.0
    ),
    Topic(
        id="forces",
        name="Newton's Second Law",
        prerequisites=["vectors"],
        mastery_score=0.0
    ),
]

PROBLEMS = [
    Problem(
        id="p1",
        topic_id="arithmetic",
        question="What is 15 + 27?",
        answer="42",
        difficulty=1
    ),
    Problem(
        id="p2",
        topic_id="algebra",
        question="Solve for x: 2x + 10 = 20",
        answer="5",
        difficulty=2
    ),
    Problem(
        id="p3",
        topic_id="vectors",
        question="Find the magnitude of a vector with components (3, 4).",
        answer="5",
        difficulty=2
    ),
    Problem(
        id="p4",
        topic_id="forces",
        question="A 10kg mass is pushed with a net force of 50N. What is the acceleration in m/s²?",
        answer="5",
        difficulty=1
    ),
]
