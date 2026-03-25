import os
from question_engine import load_questions, get_topics, get_questions_by_topic
from evaluator import check_answer
from progression import load_stats, update_session

# Define paths relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(BASE_DIR, 'data', 'questions.json')
STATS_FILE = os.path.join(BASE_DIR, 'data', 'user_stats.json')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("=" * 40)
    print("        THE FORGE - MATH CLI v1         ")
    print("=" * 40)
    print("Initializing engine...")
    
    # 1. Load Data
    questions_db = load_questions(QUESTIONS_FILE)
    if not questions_db:
        print("\n[!] FATAL: No questions found in the database. Exiting.")
        return
        
    stats = load_stats(STATS_FILE)
    
    # Show welcome
    print(f"\nWelcome back, Apprentice.")
    print(f"Lifetime Accuracy: {stats['accuracy_percentage']}%\n")
    
    # 2. Topic Selection
    topics = get_topics(questions_db)
    print("AVAILABLE TOPICS:")
    for idx, t in enumerate(topics):
        print(f"[{idx + 1}] {t}")
        
    print(f"[{len(topics) + 1}] Exit")
    
    choice = input("\nSelect your protocol: ").strip()
    
    if not choice.isdigit():
        print("Invalid selection. Aborting.")
        return
        
    choice_idx = int(choice) - 1
    
    if choice_idx == len(topics):
        print("Exiting The Forge. Goodbye.")
        return
        
    if choice_idx < 0 or choice_idx >= len(topics):
        print("Protocol not recognized. Aborting.")
        return
        
    selected_topic = topics[choice_idx]
    
    # 3. Load Questions for Topic
    active_questions = get_questions_by_topic(questions_db, selected_topic)
    
    # 4. The Interactive Loop
    session_correct = 0
    session_incorrect = 0
    
    clear_screen()
    print(f"--- STARTING SESSION: {selected_topic.upper()} ---\n")
    
    for i, q in enumerate(active_questions):
        print(f"Problem {i + 1}/{len(active_questions)}:")
        print(f">> {q['question_text']}")
        
        # Accept User Input
        user_ans = input("Answer: ").strip()
        
        # Evaluate
        is_correct = check_answer(user_ans, q['correct_answer'])
        
        if is_correct:
            print("[+] CORRECT.\n")
            session_correct += 1
        else:
            print(f"[-] INCORRECT. The answer was: {q['correct_answer']}\n")
            session_incorrect += 1
            
    # 5. Session Summary
    clear_screen()
    print("=" * 40)
    print("            SESSION COMPLETE            ")
    print("=" * 40)
    print(f"Topic: {selected_topic}")
    print(f"Correct: {session_correct}")
    print(f"Incorrect: {session_incorrect}")
    
    total = session_correct + session_incorrect
    if total > 0:
        accuracy = (session_correct / total) * 100
        print(f"Session Accuracy: {round(accuracy, 2)}%")
    print("=" * 40)
    
    # 6. Save Stats
    print("Saving progression to database...")
    update_session(STATS_FILE, stats, session_correct, session_incorrect)
    print("Done. See you next time.")

if __name__ == "__main__":
    main()
