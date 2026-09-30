n = int(input())
sum_v = 0
cnt = 0
for _ in range(n):
    x = int(input())
    sum_v += x
    cnt += 1
avg = sum_v / cnt

print(f'{sum_v} {avg:.1f}')