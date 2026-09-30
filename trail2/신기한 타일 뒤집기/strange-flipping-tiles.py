N = int(input())

arr = ['g'] * 100000

now = 100

for _ in range(N):
    x1, dir = input().split()
    x = int(x1)
    
    if dir == 'L':
        for i in range(now-x + 1, now + 1):
            arr[i] = 'w'
        now -= (x - 1)
    else:
        for i in range(now, now + x):
            arr[i] = 'b'
        now += (x - 1)

cnt_g = 0
cnt_b = 0
cnt_w = 0

for i in arr:
    if i == 'g': cnt_g += 1
    elif i == 'b': cnt_b += 1
    else: cnt_w += 1

print(cnt_w, cnt_b)

