
user_name = input("What is your name? ")
user_age = input("How old are you? ")

print(f"Hi {user_name}! It's quite cool that you are {user_age} years old!")

file = open('output.txt', 'w')
file.write(user_name)
file.write('\n')
file.write(user_age)
file.close()
