
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# 현재 위치
now = 100000

# 색 표시할 arr (black = b, white = w, gray = g)
color_arr = [0] * 200001

# 블랙, 화이트로 몇번 칠해졌는지 확인용 arr
black_cnt = [0] * 200001
white_cnt = [0] * 200001


for i in range(n):

    if dir[i] == 'R':
        for j in range(now, now + x[i]):
            if color_arr[j] == 'g': continue
            color_arr[j] = 'b'
            black_cnt[j] += 1
            if black_cnt[j] >= 2 and white_cnt[j] >= 2: color_arr[j] = 'g'
        now = now + x[i] - 1
    elif dir[i] == 'L':
        for j in range(now, now - x[i], -1):
            if color_arr[j] == 'g': continue
            color_arr[j] = 'w'
            white_cnt[j] += 1
            if black_cnt[j] >= 2 and white_cnt[j] >= 2: color_arr[j] = 'g'
        now = now - x[i] + 1

cnt_b = 0
cnt_w = 0
cnt_g = 0
for i in color_arr:
    if i == 'b': cnt_b += 1
    elif i == 'w': cnt_w += 1
    elif i == 'g': cnt_g += 1

print(cnt_w, cnt_b, cnt_g)

