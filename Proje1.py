import pandas as pd

"""
AA    90-100 Pass
BA    85-89 Pass
BB    80-84 Pass
CB    75-79 Pass
CC    70-74 Pass
DC    65-69 Pass
DD    60-64 Pass
FD    50-59 Fail
FF    0-49 Fail
"""

lesson = 'Physics'
print("\nLesson: ", lesson, "\n")

students = []

control = 1
students_index = 0
while control == 1:
    student = ['student_name', 'student_surname', 'student_number', 'grade', 'letter_grade', 'status', 'lesson']
    student[0] = input("Name: ") 
    student[1] = input("Surname: ")
    student[2] = input("School number: ")
    grade = int(input("Grade: "))
    student[3] = grade

    if (grade >= 90):
        letter_grade = 'AA'
        status = 'Pass'
    elif (grade >= 85 and grade <= 89):
        letter_grade = 'BA'
        status = 'Pass'
    elif (grade >= 80 and grade <= 84):
        letter_grade = 'BB'
        status = 'Pass'
    elif (grade >= 75 and grade <= 79):
        letter_grade = 'CB'
        status = 'Pass'
    elif (grade >= 70 and grade <= 74):
        letter_grade = 'CC'
        status = 'Pass'
    elif (grade >= 65 and grade <= 69):
        letter_grade = 'DC'
        status = 'Pass'
    elif (grade >= 60 and grade <= 64):
        letter_grade = 'DD'
        status = 'Pass'
    elif (grade >= 50 and grade <= 59):
        letter_grade = 'FD'
        status = 'Fail'
    elif (grade <= 49):
        letter_grade = 'FF'
        status = 'Fail'
    
    student[4] = letter_grade
    student[5] = status
    student[6] = lesson
    students.insert(students_index, student)
    students_index += 1

    control = int(input("[Press '1' to continue or press '0' to terminate]: "))
    print("")
    if (control == 0):
        break

print("\n", students , "\n")

my_columns = ['Name', 'Surname', 'Number', 'Grade', 'Letter Grade', 'Status', 'Lesson']
df = pd.DataFrame(columns = my_columns)

for student in students:
    df = df.append(
        {
        "Name": student[0],
        'Surname': student[1],
        'Number': student[2],
        'Grade': student[3],
        'Letter Grade': student[4],
        'Status': student[5],
        'Lesson': student[6],
        },ignore_index = True)

df.to_excel("student_grading_system.xlsx")


