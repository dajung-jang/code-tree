n = int(input())

def abc(n):
    if n < 10:
        return n ** 2
    return abc(n // 10) + (n % 10) ** 2

print(abc(n))