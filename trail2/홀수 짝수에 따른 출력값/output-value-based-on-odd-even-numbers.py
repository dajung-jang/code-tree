N = int(input())

def abc(n):
    if n % 2 == 0:
        if n == 2: return 2
        return abc(n-2) + n
    if n == 1: return 1
    return abc(n-2) + n

print(abc(N))

# n-2 + n 인건 똑같으니까 이건 한번ㅁ나 써도 되네

def abc(n):
    if n == 1: return 1
    if n == 2 : return 2

    return abc(n-2) + n