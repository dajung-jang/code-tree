n = int(input())
# 교실, 화장실, 복도
room, bath, path = 0, 0, 0
# 현재 날짜


for i in range(1, n + 1):
    if i % 2 == 0:
        if i % 3 == 0 or i % 12 == 0: room -= 1
        room += 1
    if i % 3 == 0:
        if i % 12 == 0: path -= 1
        path += 1
    if i % 12 == 0:
        bath += 1

print(room, path, bath)