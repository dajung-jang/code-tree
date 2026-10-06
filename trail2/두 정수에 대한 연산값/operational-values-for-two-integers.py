a, b = map(int, input().split())

def abc(a, b):
    if a > b: 
        a += 25
        b *= 2
        return a, b
    else:
        a *= 2
        b += 25
        return a, b
a, b = abc(a, b)
print(a, b)
