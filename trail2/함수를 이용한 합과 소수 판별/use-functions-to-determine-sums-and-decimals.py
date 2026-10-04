a, b = map(int, input().split())

def abc(a, b):
    result= 0
    cnt = 0
    for i in range(a, b+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2 and ((i // 10) + (i % 10)) % 2 == 0:
            result += 1
        cnt = 0
    return result

print(abc(a, b))