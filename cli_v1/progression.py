import json
import os
import datetime

def load_stats(filepath):
    """
    Loads the user's persistent stats. Returns default structure if blank or missing.
    """
    default_stats = {
        "total_questions_attempted": 0,
        "total_correct": 0,
        "total_incorrect": 0,
        "accuracy_percentage": 0.0,
        "sessions": []
    }
    
    if not os.path.exists(filepath):
        return default_stats
        
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return default_stats

def save_stats(filepath, stats):
    """
    Saves the stats dictionary cleanly to a JSON file.
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w') as file:
        json.dump(stats, file, indent=2)

def update_session(filepath, stats, session_correct, session_incorrect):
    """
    Updates the overall stats with the results of a single session,
    calculates new accuracy, and saves context to the file.
    """
    session_total = session_correct + session_incorrect
    if session_total == 0:
        return stats # Nothing to update
        
    # Update lifetime totals
    stats["total_questions_attempted"] += session_total
    stats["total_correct"] += session_correct
    stats["total_incorrect"] += session_incorrect
    
    # Recalculate global accuracy
    if stats["total_questions_attempted"] > 0:
        raw_accuracy = (stats["total_correct"] / stats["total_questions_attempted"]) * 100
        stats["accuracy_percentage"] = round(raw_accuracy, 2)
        
    # Log the session
    session_record = {
        "timestamp": datetime.datetime.now().isoformat(),
        "correct": session_correct,
        "incorrect": session_incorrect,
        "accuracy": round((session_correct / session_total) * 100, 2) if session_total > 0 else 0
    }
    stats["sessions"].append(session_record)
    
    # Save automatically
    save_stats(filepath, stats)
    return stats
