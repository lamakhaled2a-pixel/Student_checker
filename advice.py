def advice_generate(score):
    if score >=85:
        return "well done , keep up the good work :)"
    elif score >= 70 :
        return "you must review small mistakes and practice more"
    elif score >= 50 :
        return "you passed but need more practice"
    else:
        return " you need support and should review the basics"