number = int(input())
p = int(input())
bit_atposition_p = 2 << p

result = (number & bit_atposition_p) >> p
print(result)