def check_answer(user_input, correct_answer):
    """
    Evaluates the user's answer against the correct answer.
    Currently, compares strings without spaces and ignores case.
    This simple logic will be upgraded in future versions (e.g., math parsing).
    """
    if user_input is None or correct_answer is None:
        return False
        
    # Strip spaces and cast to lowercase for simple tolerance
    cleaned_input = str(user_input).replace(" ", "").lower()
    cleaned_correct = str(correct_answer).replace(" ", "").lower()
    
    return cleaned_input == cleaned_correct
