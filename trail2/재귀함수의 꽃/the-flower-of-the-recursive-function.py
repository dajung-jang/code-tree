n = int(input())

def abc(n):
    if n == 0: return
    print(n, end= ' ')
    abc(n-1)
    print(n, end = ' ')

abc(n)