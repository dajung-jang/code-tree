N = int(input())

arr = [0] * 201
OFFSET = 100

for _ in range(N):
    x1, x2 = map(int, input().split())

    for i in range(x1, x2):
        arr[i] += 1

print(max(arr))