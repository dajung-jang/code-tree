n = int(input())

def abc(n):
    if n == 1: return 1
    return abc(n-1) + n

print(abc(n))