a, b = map(int, input().split())

# 판단 함수
def is_target(n):
    if n % 3 == 0: return True
    # if 에서 해당되면 바로 함수 종료 되니까 그것 자체로  elif 역할을 해서 
    # elif 적어줄 필요 없음
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9: return True
        n = n // 10
    return False

# 메인 함수
def count_numbers(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if is_target(i): cnt += 1
    return cnt


print(count_numbers(a, b))
