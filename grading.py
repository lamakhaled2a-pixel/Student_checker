def is_valid_score(score):
    return score >= 0 and score <= 100 

def classify_score(score):
    if score >= 85:
        return "Excellent"
    elif score >= 50:
        return "Passed"
    else:
        return "Failed"
