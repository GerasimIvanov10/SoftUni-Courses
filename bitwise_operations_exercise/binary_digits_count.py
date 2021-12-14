number = int(input())
binary_number = input()

n = bin(number)[2:]

count_zero = 0
count_one = 0

for binary_number in n:
    if binary_number == '0':
        count_zero += 1
    elif binary_number == '1':
        count_one += 1

if binary_number == '0':
    print(count_zero)
elif binary_number == '1':
    print(count_one)
