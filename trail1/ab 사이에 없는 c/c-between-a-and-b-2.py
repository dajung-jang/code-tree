a, b, c = map(int, input().split())

is_true = 'YES'
for i in range(a, b+1):
    if i % c == 0: is_true = 'NO'
print(is_true)