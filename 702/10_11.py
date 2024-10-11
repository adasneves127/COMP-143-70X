for i in range(10):
    # Print "{number} is even" if the number is even
    # Otherwise, print that "number" is odd.
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

grade = 95
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

my_list = [
    ['These', 'are', 'some', 'words'],
    [1,3,5,7,9],
    [True, False, True, False],
    [(1, 5), (2,8), (3, 7), (9, 0)]
]
for sublist in my_list:
    print(sublist)

def print_n_dim_list(x):
    if type(x) is not list and type(x) is not tuple:
        print(x)
    else:
        for element in x:
            print_n_dim_list(element)

print_n_dim_list(my_list)

# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             print(i, j, k)

