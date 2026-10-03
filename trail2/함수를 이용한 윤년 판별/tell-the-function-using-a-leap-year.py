y = int(input())

def abc(y):
    result = 'false'

    if y % 4 == 0:
        if y % 400 != 0: result = 'false'
        else : result = 'true'

    return result

print(abc(y))