n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def abc(x):
    sum_v = 0
    for i in range(queries[x][0] - 1, queries[x][1]):
        sum_v += arr[i]
    return sum_v

for j in range(m):
    print(abc(j))


