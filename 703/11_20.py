i = 1
while i < 6:
    print(i)
    i = i + 1
print()
num = int(input("Enter a number, or type '0' to quit: "))
total = 0
while num != 0:
    total = total + num
    num = int(input("Enter a number, or type '0' to quit: "))
print(f'The total of the numbers you entered was: {total}')


