cnt = 0

n = int(input())

while 1:
    if n == 1: break

    elif n % 2 == 0:
        n = n // 2
        cnt += 1
    else: 
        n = (n * 3) + 1
        cnt += 1
    

print(cnt)