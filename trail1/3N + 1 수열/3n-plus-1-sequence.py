cnt = 0

n = int(input())

while 1:
    if n == 1: break

    if n % 2 == 0:
        n = n // 2
        cnt += 1
    else: 
        n = (n * 3) + 1
        cnt += 1
    
print(cnt)

# ===================
# # 변수 선언 및 입력
# n = int(input())
# cnt = 0
    
# while True:
#     # n이 1이 될 때까지 홀수일 때는 n = 3n+1을, 짝수일 때는 n = n/2를 반복합니다.
#     if n == 1:
#         break
        
#     if n % 2 == 1:
#         n = 3 * n + 1
#     else:
#         n = n // 2
        
#     cnt += 1
    
# print(cnt)
