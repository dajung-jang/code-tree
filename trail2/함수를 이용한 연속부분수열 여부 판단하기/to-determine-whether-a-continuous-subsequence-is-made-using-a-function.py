n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def abc(a, b):
    for i in range(len(a) - len(b) + 1):
        if a[i] == b[0]:
            for j in range(len(b)):
                if a[i+j] != b[j]:
                    break
                elif j == len(b) -1:
                    return print('Yes')
    return print('No')
abc(a, b)



    
