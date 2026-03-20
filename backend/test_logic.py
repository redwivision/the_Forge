from Models import Topic
from logic import get_next_recommendation

def run_test():
    # Mock data setup
    topics = [
        Topic(id="arithmetic", name="Basic Arithmetic", prerequisites=[], mastery_score=0.0),
        Topic(id="algebra", name="Linear Equations", prerequisites=["arithmetic"], mastery_score=0.0),
        Topic(id="vectors", name="Vector Basics", prerequisites=["algebra"], mastery_score=0.0)
    ]

    print("--- SCENARIO 1: Fresh Start ---")
    rec = get_next_recommendation(topics)
    print(f"Recommended: {rec.name if rec else 'None'}") # Expected: Arithmetic

    print("\n--- SCENARIO 2: Arithmetic Mastered ---")
    topics[0].mastery_score = 100.0
    rec = get_next_recommendation(topics)
    print(f"Recommended: {rec.name if rec else 'None'}") # Expected: Algebra

    print("\n--- SCENARIO 3: Algebra Mastered ---")
    topics[1].mastery_score = 100.0
    rec = get_next_recommendation(topics)
    print(f"Recommended: {rec.name if rec else 'None'}") # Expected: Vectors

    print("\n--- SCENARIO 4: ALL Mastered ---")
    topics[2].mastery_score = 100.0
    rec = get_next_recommendation(topics)
    print(f"Recommended: {rec.name if rec else 'None'}") # Expected: None

if __name__ == "__main__":
    run_test()
