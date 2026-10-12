n = int(input())

def abc(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return abc(n // 2) + 1
    
    else:
        return abc(n // 3) + 1
print(abc(n))
        
