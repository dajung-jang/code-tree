n = int(input())
i = 1
cnt = 0
while n >= 0:
    n = n // i
    i += 1
    cnt += 1
print(cnt)

# 다른 풀이 
# n = int(input())
# cnt = 0
# for i in range(1, n+ 1):
#     n = n // i
#     cnt += 1
#     if n <= 1: break
# print(cnt)