# Student scores are given:
student_scores= {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}
# make a dictionary containing grades :

student_grades = {}

for students in student_scores:
    score = student_scores[students]
    if score > 90:
        student_grades[students] = "Outstanding"
    elif score > 80:
        student_grades[students] = "Exceeds Exception"
    elif score > 70:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"

print(student_grades)