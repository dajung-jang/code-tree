a, b = map(int, input().split())

i = a
print(a, end=' ')

while a <= b:
    if a % 2 != 0:
        a *= 2
    else:
        a += 3
    
    if a > b: break
    print(a, end=' ')