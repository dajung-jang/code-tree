M, D = map(int, input().split())

# 풀이 2(해설 본 후 작성한 코드)
def last_day_number(m):
    if m == 2: 
        return 28
    if m in (4, 6, 9, 11):
        return 30
    return 31

def judge_day(m, d):
    if m <= 12 and d <= last_day_number(m):
        return True
    return False

if judge_day(M, D): print('Yes')
else: print('No')




'''
# 풀이 1
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

if M >12:
    print('No')
elif M == 2: print(day_28(D))
else:
    for i in arr_30:
        if i == M:
            print(day_30(D))
            break
    else: print(day_31(D))
'''