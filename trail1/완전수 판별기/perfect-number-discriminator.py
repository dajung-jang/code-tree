n = int(input())

arr = []

for i in range(1, n + 1):
    if n % i == 0 and n != i:
        arr.append(i)

sum_v = 0

for i in arr:
    sum_v += i

if n == sum_v:
    print('P')
else: print('N')
    