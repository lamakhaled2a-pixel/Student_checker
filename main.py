from grading import is_valid_score, classify_score
from report_writer import build_report, save_report
from advice import advice_generate


try:
        student_name = input("Enter student name: ").strip()
        if student_name == " ":   
            print("student name cannot be empty.")
        else:
            score = float(input("Enter student score from 0 to 100 :"))
            if not is_valid_score(score):
                print("score must be between 0 and 100.")
            else:
                while True:
                    student_class=input("Enter student class A , B OR C :").strip().upper()
                    if student_class in ["A", "B","C"]:
                         break
                    else:
                         print("Invalid class ! Please enter A,B OR C only ")
                status=classify_score(score)
                advice=advice_generate(score)
                report=build_report(student_name,score,status,student_class,advice)
                filename= save_report(student_name, report)

                print(report)
                print(f"Report saved to:{filename}")
           
except valueError:
    print("Invalid input. Score must be a number.")