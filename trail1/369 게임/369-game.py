n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0 or i % 6 == 0 or i % 9 == 0: print(0, end=' ')
    elif i >= 10:
        if str(i)[0] == '3' or str(i)[0] == '6' or str(i)[0] == '9': print(0, end=' ')
        elif str(i)[1] == '3' or str(i)[1] == '6' or str(i)[1] == '9': print(0, end=' ')
        else: print(i, end=' ')
    
    else: print(i, end=' ')

# -----------

# for i in range(1, n + 1):
#     if i % 3 == 0 : print(0, end=' ')
#     # 10으로 나눈 나머지 그니까 일의자리 숫자가 3, 6, 9인지 확인
#     elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9: print(0, end=' ')
#     # 10으로 나눈 몫 그니까 10의 자리가 3, 6, 9 인지 확인
#     elif i // 10 == 3 or i // 10 == 6 or i // 10 == 9: print(0, end=' ')
#     else: print(i, end=' ')