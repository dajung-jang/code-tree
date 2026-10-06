n, m = map(int, input().split())

def swap(a, b):
    a, b = b, a
    return a, b

result = swap(n, m)
print(*result)