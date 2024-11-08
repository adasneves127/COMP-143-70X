my_dictionary = {
    "name": "Alex",
    "grade": 96
}

my_dictionary['gpa'] = 3.6
my_dictionary['courses'] = ['COMP 151', 'COMP 152', 'MATH 161E']
for key, val in my_dictionary.items():
    if key == 'courses' and len(val) != 0:
        print('Courses Taken: ')
        for course in val:
            print(f'\t{course}')
    elif key != 'courses':
        print(f"{key}: {val}")

# my_dictionary['advisor'] = 'Margaret'
student_advisor = my_dictionary.get('advisor')

if student_advisor is None:
    print('No Advisor Assigned!')
    my_dictionary['advisor'] = 'Alex'
else:
    print(student_advisor)

print(my_dictionary)

person = {
    "title": "student",
    "personal_data": {
        "name": "Alex Dasneves",
        "age": 21,
        "hometown": "Fairhaven, MA"
    },
    "academic_information": {
        "grade": "Senior",
        "major": "Computer Science"
    }
}
