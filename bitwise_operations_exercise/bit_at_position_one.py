number = int(input())
bit_at_position_1 = 1 << 1

result = (number & bit_at_position_1) >> 1
print(result)

