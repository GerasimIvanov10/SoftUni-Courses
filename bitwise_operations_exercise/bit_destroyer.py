n = int(input())
p = int(input())
mask = ~(1 << p)

result = (n & mask)

print(result)

