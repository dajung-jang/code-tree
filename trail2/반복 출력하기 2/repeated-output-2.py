n = int(input())

# 올라가면서 출력
# def print_hello(x):
#     if x == n:
#         return
#     print('HelloWorld')
#     print_hello(x + 1)
# print_hello(0)

# 내려가면서 출력
def print_hello(n):
    if n == 0:
        return
    print_hello(n - 1)
    print('HelloWorld')

print_hello(n)