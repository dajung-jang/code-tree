sum_v = 0
n = int(input())
for _ in range(n):
    x = int(input())
    if x % 2 == 1 and x % 3 == 0:
        sum_v += x
print(sum_v)