# Bool(ean)s
# True or False values

# Boring method
x = True
y = False

num_1 = 7.0
num_2 = 7

# print(f'It is a {num_1 == num_2} statement that {num_1} is equal to {num_2}')
# print(f'It is a {num_1 != num_2} statement that {num_1} is not equal to {num_2}')
# print(f'It is a {num_1 < num_2} statement that {num_1} is less than {num_2}')
# print(f'It is a {num_1 > num_2} statement that {num_1} is greater than {num_2}')
# print(f'It is a {num_1 >= num_2} statement that {num_1} is greater than or equal to {num_2}')
# print(f'It is a {num_1 <= num_2} statement that {num_1} is less than or equal to {num_2}')

for i in range(10):
    if i == 4:
        print("Hello number 4!")
    else:
        print("You aren't number 4!")

my_string = "The quick brown fox jumps over the lazy dog!"
e_count = 0
for character in my_string:
    if character == 'e':
        e_count = e_count + 1
print(f"I found {e_count} occurrences of 'e' in the string.")

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
for character in my_string:
    if character in vowels:
        vowel_count = vowel_count + 1
print(f"I found {vowel_count} vowels in the string.")

x = 0
x_list = []
for i in range(10):
    x_list.append(x)
    x = x + 1
print(x_list)

my_numbers = [74, 58, 37, 100, 74, 9, 96, 43, 91, 53, 89, 91, 96, 31, 100, 65, 25, 30, 49, 6, 35, 17, 22, 23, 22, 14, 97, 80, 75, 33, 49, 6, 68, 60, 7, 82, 21, 44, 53, 84, 14, 53, 96, 78, 77, 62, 70, 4, 23, 84, 33, 9, 61, 8, 57, 77, 95, 20, 34, 57, 31, 99, 56, 1, 86, 34, 79, 62, 1, 41237, 33, 88, 91, 83, 8, 78, 34, 18, 16, 42, 25, 96, 13, 42, 79, 6, 69, 88, 65, 53, 24, 65, 12, 11, 1, 53, 81, 77, 29, 7]
max_num = my_numbers[0]
for num in my_numbers:
    if num > max_num:
        max_num = num
print(f"The largest number I found was: {max_num}")
