n = int(input())

def abc(n):
    if n == 1: return 1
    if n == 2: return 1

    return abc(n-1) + abc(n-2)

print(abc(n))