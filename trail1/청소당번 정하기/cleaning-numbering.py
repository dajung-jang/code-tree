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

# =============================
# # 변수 선언 및 입력
# n = int(input())
# cnt2, cnt3, cnt12 = 0, 0, 0

# # 각 날짜마다 확인합니다.
# for i in range(1, n + 1):
#     # 주기가 가장 긴 12일부터 확인합니다.
#     if i % 12 == 0:
#         cnt12 += 1
#     # 12일 주기에 들어오지 않는다면, 3일 주기에 들어오는지 확인합니다.
#     elif i % 3 == 0:
#         cnt3 += 1
#     # 3일 주기에도 들어오지 않는다면, 2일 주기에 들어오는지 확인합니다.
#     elif i % 2 == 0:
#         cnt2 += 1

# print(cnt2, cnt3, cnt12)