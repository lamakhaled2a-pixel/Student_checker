def build_report(student_name, score, status,student_class,advice):
    report = f"""Student Performance Report

Student Name: {student_name} 
Score: {score}
Status: {status}
Student Class: {student_class}
advice :{advice}
"""
    return report

def save_report(student_name, report):
    filename = f"{student_name.lower().replace(' ','_')}_report.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
    return filename
