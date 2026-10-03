a, b = map(int, input().split())

def abc(a, b):
    cnt = 0
    for i in range(a, b + 1):
        bool_v = 0
        if i % 3 == 0:
            bool_v = 1
        elif (i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
            bool_v = 1
        elif bool_v == 0:
            for j in range(1, len(str(b))+1):
                if i // 10 ** j == 3 or i // 10 ** j == 6 or i // 10 ** j == 9:
                    bool_v = 1
        if bool_v == 1:
            cnt += 1
    return cnt
print(abc(a, b))
