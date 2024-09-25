x = 5
x = 7
x = 10
y = 3.6

# Integers                                     -- 3, 7,10, -100, 897533
# Strings                                      -- "This is a string", 'So is this!'
# Floating-Point Numbers (floats)              -- 3.6, 7.3, 10.8, -100.648908, 3.0
# Lists                                        -- ["Apple", "Banana", "Orange", ...]
# Boolean (Bool)                               -- True, False
# Tuple                                        -- ("Apple", "Banana", "Orange", ...)
# Dictionary (Dict)                            -- {"name": "Alex", "gpa": 3.6}

name = "Alex", "Dasneves"
#
#
# print(f"Name: {name}")
#
# name = "Shea", "Haskins"
# print(f"Name: {name}")
# # name[1] = "Jones" # This doesn't work!
#
# print(8 + 5)
# print("Hello, " + "World!")
# # print("Hello" + x)
# # print(x + "World!")
# print(type(x))
# print(type(y))
#
# # This is later in the semester.
# student = {
#     "name": "Alex",
#     "gpa": 3.6
# }
#
# print(student['name'])
#
# print(0.1 + 0.2)
#
# user_name = input("What is your name? ")
# print(f"Nice to meet you, {user_name}!")


names = []
for count in range(3):
    names.append(input("Please enter a name? "))

print("You entered: ")
for name in names:
    print(name)
