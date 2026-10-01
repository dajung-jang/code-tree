cnt = 0
n = int(input())

while 1:
    n = n // 2
    cnt += 1

    if n == 1: break
print(cnt)