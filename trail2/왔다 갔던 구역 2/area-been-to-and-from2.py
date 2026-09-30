N = int(input())

arr = [0] * 2001
# OFFSET = 1000

now = 1000

for _ in range(N):
    x1, dir = input().split()
    x = int(x1)
    if dir == 'L':
        for i in range(now - x, now):
            arr[i] += 1
        now -= x

    else:
        for j in range(now, now + x):
            arr[j] += 1
        now += x

cnt = 0

for i in range(len(arr)):
    if arr[i] >= 2:
        cnt += 1

print(cnt)