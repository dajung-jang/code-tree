a, b = map(int, input().split())

def abc(a, b):
    sum_v = 0
    for i in range(a, b+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0: cnt += 1
        if cnt == 2: sum_v += i
    print(sum_v)

abc(a, b)