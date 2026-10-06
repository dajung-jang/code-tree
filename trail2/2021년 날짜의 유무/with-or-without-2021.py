M, D = map(int, input().split())

arr_31 = [1, 3, 5, 7, 8, 10, 12]
arr_30 = [4, 6, 9, 11]

def day_31(n):
    if n > 31: return 'No'
    for i in range(1, 32):
        if n == i: 
            return 'Yes'
            break
        elif i == 31: return 'No'
def day_30(n):
    if n > 30: return 'No'
    for i in range(1, 31):
        if n == i: 
            return 'Yes'
            break
        elif i == 30: return 'No'
def day_28(n):
    if n > 28: return 'No'
    for i in range(1, 29):
        if n == i: 
            return 'Yes'
            break
        elif i == 29: return 'No'

if M == 2: print(day_28(D))
else:
    for i in arr_30:
        if i == M:
            print(day_30(D))
            break
    else: print(day_31(D))
