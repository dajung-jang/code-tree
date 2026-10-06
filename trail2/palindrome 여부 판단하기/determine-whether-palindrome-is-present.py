A = input()

def abc(A):
    for i in range(len(A)):
        if A[i] != A[len(A) - i - 1]: return False
    return True

if abc(A): print('Yes')
else: print('No')

# def is_ture(A):
#     b = []
#     for i in range(len(A)-1, -1, -1):
#         b.append(A[i])
#     if A == b:
#         return 'Yes'
#     return 'No', b

# print(is_ture(A))
