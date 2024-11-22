my_dictionary = {
    "name": "Alex",
    "grade": 96
}

my_dictionary['gpa'] = 3.6
my_dictionary['courses'] = ['COMP 151', 'COMP 152', 'COMP 206', 'COMP 250']

# I want to print out the keys and value in my dictionary...
for key, value in my_dictionary.items():
    if key == 'courses' and len(value) != 0:
        print('Courses Taken: ')
        for course in value:
            print(f'\t{course}')
    elif key != 'courses':
        print(f"{key}: {value}")

student_advisor = my_dictionary.get('advisor')
if student_advisor is None:
    print('No Advisor Assigned!')
    my_dictionary['advisor'] = 'Laura'
else:
    print(student_advisor)

print(my_dictionary)

person = {
    "name": "Alex",
    "age": 21,
    "hometown": "Fairhaven, MA",
    "hair color": "brown",
    "eye color": "brown",
    "height": "5'6\"",
    "occupation": "Peer-Assist Leader"
}

student = {
    "personal_details": person,
    "academic_details": {
        "institution": "BSU",
        "grade": "Senior",
        "gpa": 3.6,
        "classes_taken": [],
        "advisor": "Dr. Margaret Black",
        "majors": ["Computer Science"],
        "minors": ["Mathematics"]
    }
}

professor = {
    "personal_details": person,
    "academic_details": {
        "institution": "BSU",
        "title": "Full Professor",
        "salary": 95_000,
        "classes_taught": [],
        "advisee": [],
        "department": ['Computer Science'],
        "office": "DMF331",

    }
}

