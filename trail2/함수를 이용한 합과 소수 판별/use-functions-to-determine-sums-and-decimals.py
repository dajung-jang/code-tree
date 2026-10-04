a, b = map(int, input().split())

# def abc(a, b):
#     result= 0
#     cnt = 0
#     for i in range(a, b+1):
#         for j in range(1, i+1):
#             if i % j == 0:
#                 cnt += 1
#         if cnt == 2 and ((i // 10) + (i % 10)) % 2 == 0:
#             result += 1
#         cnt = 0
#     return result

# print(abc(a, b))

cnt = 0
def is_prime(n):
    if n == 1: return False

    for i in range(2, n):
        if n % i == 0: return False
    
    return True

def is_even(n):
    if ((n // 10) + (n % 10)) % 2 == 0: return True
    return False

def result(n):
    if is_prime(n) and is_even(n): return True
    return False

for i in range(a, b+1):
    if result(i): cnt += 1

print(cnt)