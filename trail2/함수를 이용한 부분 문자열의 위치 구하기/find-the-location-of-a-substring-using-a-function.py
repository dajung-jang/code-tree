text = input()
pattern = input()


def is_same(n):
   
    for i in range(len(pattern)):
        if n + i >= len(text) or text[n + i] != pattern[i] : return False
    return True

for j in range(len(text)):
    if is_same(j):
        print(j)
        break
    elif j == len(text) - 1: print(-1)
