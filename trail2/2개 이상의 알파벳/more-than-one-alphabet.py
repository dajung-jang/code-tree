A = input()
'''
# 방법 1
# 반복 돌면서 해당 인덱스랑 그 다음 인덱스만 비교
def abc(A):
    for i in range(len(A) -1):
        if A[i] != A[i+1]: return 'Yes'
    return 'No'
print(abc(A))
'''

# 방법 2
# 기준 인덱스를 정해놓고 나머지로 반복 돌면서 기준 인덱스랑 다른게 있는지 확인하는 방법
def abc(A):
    for i in range(1, len(A)):
        if A[0] != A[i]: return 'Yes'
    return 'No'
print(abc(A))