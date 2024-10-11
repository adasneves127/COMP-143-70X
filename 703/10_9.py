from random import randint

rand_num = randint(1, 100)
for i in range(10):
    # If i is an even number, print that it's even.
    # Otherwise, print that it is odd.
    if (i % 2) == 0:
        print(f'The number {i} is even')
    else:
        print(f'The number {i} is odd')

# num_1 = input("I'm thinking of a number between 1 and 100. Can you guess it? ")
# num_1 = int(num_1)
# for i in range(10000):
#     if num_1 > rand_num:
#         print('Too High!')
#     elif num_1 < rand_num:
#         print('Too Low!')
#     else:
#         print("You got it!")
#         exit()
#
#     num_1 = input("Try another number: ")
#     num_1 = int(num_1)

my_list = ['hi', 'bye', 'good day', 'computers']
target_word = 'good dey'
is_found = False
for word in my_list:
    if word == target_word:
        is_found = True
if is_found:
    print('I found the target word!')
else:
    print('I did not find the target word!')


my_list = [
    ['These', 'are', 'some', 'words'],
    [1,3,5,7,9],
    [True, False, True, False],
    [(1, 5), (2,8), (3,7),(9,0)]
]
# for sub_list in my_list:
#     for item in sub_list:
#         print(item)

# def print_n_dim_list(x):
#     if type(x) is not list:
#         print(x)
#     else:
#         for item in x:
#             print_n_dim_list(item)

# print_n_dim_list(my_list)
