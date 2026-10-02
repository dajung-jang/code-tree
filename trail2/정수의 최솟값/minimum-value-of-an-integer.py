a, b, c = map(int, input().split())

def abc(a, b, c):
    arr = [a, b, c]
    min_v = 101
    for i in range(3):
        if arr[i] < min_v: min_v = arr[i]
    print(min_v)
abc(a, b, c)
