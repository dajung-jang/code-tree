n = int(input())
arr = list(map(int, input().split()))

def abc(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

abc(arr)
print(*arr)