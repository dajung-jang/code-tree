n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_v = arr[m-1]
def abc(arr, m):
    global sum_v
    while m != 1:
        if m % 2 == 1:
            m -= 1
        else: m = m // 2
        sum_v += arr[m-1]


abc(arr, m)
print(sum_v)
    
    
    