a, o, c = input().split()
a = int(a)
c = int(c)

def abc(a, o, c):
    if o == '+':
        print(a, o, c, '=', a + c)
    elif o == '-':
        print(a, o, c, '=', a - c)
    elif o == '/':
        print(a, o, c, '=', int(a / c))
    elif o == '*':
        print(a, o, c, '=', a * c)
    else: print('False')

abc(a, o, c)