n, m = map(int, input().split())

def lcm(a, b):
    big = max(a, b)
    multiple = big
    while multiple % a != 0 or multiple % b != 0:
        multiple += big
    return multiple
print(lcm(n, m))
        