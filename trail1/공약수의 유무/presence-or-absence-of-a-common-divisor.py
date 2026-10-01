a, b = map(int, input().split())

is_true = 0
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0: is_true = 1

print(is_true)
