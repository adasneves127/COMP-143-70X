for num in range(10):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f"{num} is odd")

# Using both sets of quotes in a string, by "Escaping" the quotes
# print('Alex said \"Kyle\'s favorite flavor of ice cream is chocolate\"')

grade = 90
if grade >= 90:
    print('You got an A')
elif grade >= 80:
    print('You got a B')
elif grade >= 70:
    print('You got a C')
elif grade >= 60:
    print('You got a D')
else:
    print('You got a F')

# Nested Lists:
my_list = [
    ['These', 'are', 'some', 'words'],
    [1,3,5,7,9],
    [True, False, True,False],
    [(1,5), (2,8), (3,7), (9,0)]
]

print(my_list)
print(my_list[0])
print(type(my_list[0]))
print(my_list[1][1])

for sublist in my_list:
    print(sublist)

def print_n_dim_list(x):
    if type(x) is not list and type(x) is not tuple:
        print(x)
    else:
        for element in x:
            print_n_dim_list(element)

print_n_dim_list(my_list)

for i in range(10):
    for j in range(10):
        for k in range(10):
            print(i, j, k)
