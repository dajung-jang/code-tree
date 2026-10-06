a, b = map(int, input().split())

def abc(a, b):
    if a > b:
        a *= 2
        b += 10
        return a, b
    a += 10
    b *= 2
    return a, b
a, b = abc(a, b)
print(a, b)