cnt = 0
while 1:
    if cnt == 3: break
    n = int(input())
    if n % 2 == 1:
        continue
    else: 
        print(n // 2) 
        cnt += 1