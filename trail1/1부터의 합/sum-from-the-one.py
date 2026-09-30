n = int(input())
sum_v = 0
cnt = 0
for i in range(1, 101):
    sum_v += i
    cnt += 1
    if sum_v >= n: break
print(cnt)