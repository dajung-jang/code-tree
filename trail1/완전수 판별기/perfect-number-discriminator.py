n = int(input())

arr = []

# 여기서 자기자신은 약수로 포함 안하게 걍 범위 자체를 1 ~ n-1 즉 range(1, n)으로만 해도 될듯
for i in range(1, n + 1):
    if n % i == 0 and n != i:
        arr.append(i)

sum_v = 0

for i in arr:
    sum_v += i

if n == sum_v:
    print('P')
else: print('N')
    