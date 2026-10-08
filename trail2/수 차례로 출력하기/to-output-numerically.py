n = int(input())

def abc1(n):
    if n == 0: return
    abc1(n-1)
    print(n, end= ' ')

def abc2(n):
    if n == 0: return
    print(n, end=' ')
    abc2(n-1)

abc1(n)
print()
abc2(n)

