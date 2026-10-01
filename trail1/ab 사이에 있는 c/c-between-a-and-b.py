a, b, c = map(int, input().split())
for i in range(a, b+1):
    if i % c == 0:
        print('YES')
        break
    if i == b: print('NO')
        
# ==========================
# # 변수 선언 및 입력
# inp = input()
# arr = inp.split()
# a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
# satisfied = False

# for i in range(a, b + 1):
#     # a에서 b사이의 값 중 c의 배수가 있는지 확인합니다.
#     if i % c == 0:
#         satisfied = True


# # 출력
# if satisfied == True:
#     print("YES")
# else:
#     print("NO")
