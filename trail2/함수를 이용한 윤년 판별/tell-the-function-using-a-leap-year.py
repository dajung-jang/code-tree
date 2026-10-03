y = int(input())

def abc(y):
    result = 'false'

    if y % 4 == 0 and y % 100 != 0:
        result = 'true'    
    return result

print(abc(y))