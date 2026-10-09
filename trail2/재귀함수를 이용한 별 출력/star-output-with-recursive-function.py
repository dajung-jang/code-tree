n = int(input())

def abc(n):
    if n == 0: return
    abc(n-1)
    print('*' * n)

abc(n)