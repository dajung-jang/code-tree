n = int(input())

def abc(n):
    if n == 0: return
    print('* ' * n)
    abc(n-1)
    print('* ' * n)

abc(n)