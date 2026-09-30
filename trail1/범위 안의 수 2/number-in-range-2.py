sum_v = 0
cnt = 0
for _ in range(10):
    x = int(input())
    if x >= 0 and x <= 200:
        sum_v += x
        cnt += 1
avg = round(sum_v / cnt, 1)

print(sum_v, avg)