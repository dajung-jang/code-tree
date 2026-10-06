a, b = map(int, input().split())

# 판단 함수
def is_target(n):
    if n % 3 == 0: return True
    # if 에서 해당되면 바로 함수 종료 되니까 그것 자체로  elif 역할을 해서 
    # elif 적어줄 필요 없음
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9: return True
        # 같은 의미 (in을 쓰면 결과를 True, False 로 반환함)
        if (n % 10) in (3, 6, 9): return True
        n = n // 10
    return False

# 메인 함수
def count_numbers(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if is_target(i): cnt += 1
    return cnt


print(count_numbers(a, b))
