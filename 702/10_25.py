# 1. Create an empty list:
students = []

# 2. Adding students
students.append(("Alex", 80))
students.append(("Tom", 60))
students.append(("Jim", 90))
students.append(("Kyle", 31))

# 3. Displaying Students
for student in students:
    print(f'{student[0]}: {student[1]}')

# 4. Calculate average
if students:
    sum_of_grades = sum([student[1] for student in students])
    average = sum_of_grades / len(students)
    print(f'Grade Average: {average}')

# 5. Finding the highest and lowest grades
max_a = max([student[1] for student in students])
min_a = min([student[1] for student in students])
min_b = students[0][1]
max_b = students[0][1]
for student in students:
    if student[1] > max_b:
        max_b = student[1]
    if student[1] < min_b:
        min_b = student[1]
print(min_a, max_a)
print(min_b, max_b)

# 6. Filtering
threshold = 75
for student in students:
    if student[1] > threshold:
        print(f'Student {student[0]} exceeded the threshold value of {threshold} with a grade of {student[1]}')
