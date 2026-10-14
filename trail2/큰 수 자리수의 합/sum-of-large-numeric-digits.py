a, b, c = map(int, input().split())

mul_v = a * b * c
sum_v = 0
for i in range(len(str(mul_v))-1, -1, -1):
    sum_v += mul_v // (10 ** i)
    mul_v = mul_v % (10 ** i)

print(sum_v)