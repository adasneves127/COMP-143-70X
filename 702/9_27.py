# Bool(ean)
# True or False value

x = True
y = False
num_1 = 7.0
num_2 = 7

print(f'It is a {num_1 == num_2} statement that {num_1} is equal to {num_2}')
print(f'It is a {num_1 != num_2} statement that {num_1} is not equal to {num_2}')
print(f'It is a {num_1 < num_2} statement that {num_1} is less than {num_2}')
print(f'It is a {num_1 > num_2} statement that {num_1} is greater than {num_2}')
for i in range(10):
    if i == 4:
        print("Hello Number 4!")
    else:
        print('You are not number 4!')

my_string = 'ThE quick brown fox jumps over the lazy dog!'
e_count = 0

for character in my_string.lower():
    if character == 'e':
        e_count = e_count + 1
print(f'I found {e_count} occurrences of e in the string')


vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
for character in my_string.lower():
    if character in vowels:
        vowel_count = vowel_count + 1
print(f'I found {vowel_count} vowels in your string!')

my_numbers = [36, 74, 3, 1, 98, 20, 65, 26, 72, 4, 62, 86, 58, 37, 91, 101, 91, 65, 100, 38, 34, 78, 54, 31, 46, 87, 37, 41, 75, 39, 38, 100, 81, 78, 10, 46, 62, 6, 77, 2, 71, 39, 18, 88, 9, 35, 97, 86, 63, 95, 83, 6, 46, 83, 98, 2, 93, 23, 71, 48, 66, 72, 49, 0, 28, 72, 45, 4, 52, 34, 41, 41, 86, 63, 76, 80, 80, 57, 41, 15, 100, 87, 92, 50, 38, 33, 76, 28, 46, 22, 14, 39, 86, 29, 99, 24, 90, 62, 78, 97]
max_num = my_numbers[0]
for number in my_numbers:
    if number > max_num:
        max_num = number
print(f"The largest number I found was {max_num}.")