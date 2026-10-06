a, b = map(int, input().split())

# 조건 1
def is_mul2(n):
    return n % 2 == 0

# 조건 2
def is_5(n):
    return n % 10 == 5

# 조건 3
def is_3(n):
    return n % 3 == 0 and n % 9 != 0

# 판단함수
def is_true(n):
    return is_mul2(n) or is_5(n) or is_3(n)

cnt = 0
for i in range(a, b+1):
    if is_true(i) == False: cnt += 1

print(cnt)