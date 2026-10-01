sum_v = 0
cnt  = 0
while 1:
    x = int(input())
    if x // 10 == 2:
        sum_v += x
        cnt += 1
    else: break

avg = sum_v / cnt
print(f'{avg:.2f}')