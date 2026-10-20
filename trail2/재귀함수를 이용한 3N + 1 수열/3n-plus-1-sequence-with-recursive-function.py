n = int(input())

cnt = 0

def abc(n):
    global cnt
    if n == 1:
        return
    if n % 2 == 0:
        cnt += 1
        n //= 2
        abc(n)
        return

    n = (n * 3 + 1)
    cnt += 1
    abc(n)
    return

abc(n)
print(cnt)
