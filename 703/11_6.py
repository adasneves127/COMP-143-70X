# Dictionaries

my_dictionary = {
    "name": "Alex",
    "grade": 94
}

print(my_dictionary['name'])
my_dictionary['gpa'] = 3.68
my_dictionary['classes'] = []
print(f"Name: {my_dictionary['name']}, GPA: {my_dictionary['gpa']}")
print('Student Data:')
for foo, bar in my_dictionary.items():
    print(f'\t{foo.title()}: {bar}')
my_dictionary['classes'].append('COMP 151')
my_dictionary['classes'].append('COMP 206')
my_dictionary['classes'].append('COMP 250')
my_dictionary['classes'].append('COMP 350')
print(my_dictionary)

