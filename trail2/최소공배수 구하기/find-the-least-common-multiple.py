n, m = map(int, input().split())

# def lcm(a, b):
#     big = max(a, b)
#     multiple = big
#     while multiple % a != 0 or multiple % b != 0:
#         multiple += big
#     return multiple
# print(lcm(n, m))
        
def abc(n, m):
    i = max(n, m)
    while 1:
        if i % n == 0 and i % m == 0:
            print(i)
            break
        else: i += 1
abc(n, m)