sum_v = 0
cnt = 0
for _ in range(10):
    x = int(input())
    if x >= 0 and x <= 200:
        sum_v += x
        cnt += 1
avg = round(sum_v / cnt, 1)

print(sum_v, avg)

# ================
# # 변수 선언, 입력
# sum_val = 0
# cnt = 0

# for _ in range(10):
#     num = int(input())
#     if num >= 0 and num <= 200:
#         sum_val += num
#         cnt += 1

# # 0이상 200이하의 정수들의 평균을 구합니다.
# avg = sum_val / cnt

# # 출력
# print(f"{sum_val} {avg:.1f}")
