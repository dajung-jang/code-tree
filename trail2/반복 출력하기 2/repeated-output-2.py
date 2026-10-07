n = int(input())

def print_hello(x):
    if x == n:
        return
    print('HelloWorld')
    print_hello(x + 1)

print_hello(0)