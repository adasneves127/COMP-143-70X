students = []

students.append(('Name1', 50))
students.append(('Name2', 80))
students.append(('Name3', 99))
students.append(('Name4', 73))


grades = [grade for _, grade in students]

print(max(grades))
print(min(grades))
max_grade = grades[0]
min_grade = grades[0]
for grade in grades:
    if grade < min_grade:
        min_grade = grade
    if grade > max_grade:
        max_grade = grade
print(max_grade)
print(min_grade)

threshold = 85
for student in students:
    if student[1] > threshold:
        # Print something
        print()




