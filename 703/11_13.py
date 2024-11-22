import json
import math

# # Reading a file
# my_file = open('10_9.py')
# for line in my_file:
#     print(line)
#
# my_string = 'This is a string that I want to write to a file.'
# my_file = open('output.txt', 'w')
# my_file.write(my_string)
# my_file.close()

# student_data = [
#     {
#         "name": "Alex",
#         "grade": "90"
#     },
#     {
#         "name": "Tony",
#         "grade": "39"
#     },
#     {
#         "name": "Abby",
#         "grade": "78"
#     }
# ]
my_file = open('output.txt')
student_data = json.loads(my_file.read())
my_file.close()

print(student_data)

my_file = open('output.txt', 'w')
json_data = json.dumps(student_data)
my_file.write(json_data)
my_file.close()

# Opening a file for writing will delete and remake the existing file!
x = open('test.txt', 'a')
x.write('This is a test!\n')
x.close()

# This is bad!
# math.e = 2
