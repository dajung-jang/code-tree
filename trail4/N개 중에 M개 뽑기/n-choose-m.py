N, M = map(int, input().split())

used = [0] * (N+1)
path = [] * M
def abc(level):
    if level == M:
        print(*path)
        return
    for i in range(1, N+1):
        if used[i] == 1: continue
        path.append(i)
        used[i] = 1
        abc(level+1)
        path.pop()
        used[i] = 0
abc(0)