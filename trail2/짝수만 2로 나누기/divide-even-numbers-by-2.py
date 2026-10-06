n = int(input())
arr = list(map(int, input().split()))

def change(arr, n):
    for i in range(n):
        if arr[i] % 2 == 0: 
            arr[i] = arr[i] // 2
    return arr

print(*change(arr, n))
