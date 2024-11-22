file = open('output.txt', 'r')
user_name = file.readline().rstrip()
user_age = file.readline()
file.close()

print(f"My friend told me your name is {user_name}, and that you are {user_age} years old!")
