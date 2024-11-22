
user_name = input("What is your name? ")
user_age = input("What is your age? ")

print(f"Nice to meet you {user_name}! So cool that you are {user_age} years old!")

file = open("output.txt", 'w')

file.write(user_name)
file.write('\n')
file.write(user_age)

file.close()
