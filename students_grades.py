students_grades = {
    'Alice':[85, 92, 78, 92],
    'Bob': [90, 88, 84, 100],
    'Charlie': [70, 65, 72],
    'Diana': [95, 100, 98]
}

def calculate_averange(grades):
    average = sum(grades) / len(grades)
    return average

def assign_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    elif average >= 50:
        return 'E'
    else:
        return 'F'

students_with_A = set()

for student, body in students_grades.items():
    print("Student", student, "ma body", body)
    prumer = calculate_averange(body)
    znamka = assign_letter_grade(prumer)
    print(f"Student {student} ma prumer {prumer} a dostava znamku {znamka}")

    if znamka == "A":
        students_with_A.add(student)

print("\nStudent with an 'A' grade:")
for student in students_with_A:
    print(student)
print(f"\nNumber of student with A is: {len(students_with_A)}")