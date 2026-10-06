A = input()

def abc(A):
    cnt = 1
    for i in range(len(A) -1):
        if A[i] != A[i+1]: cnt += 1
    
    if cnt >= 2: return 'Yes'
    return 'No'
print(abc(A))
