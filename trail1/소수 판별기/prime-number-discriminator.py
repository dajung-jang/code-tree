n = int(input())
arr = [0] * (n+1)

for i in range(2, n):
    if n % i == 0: arr[i] += 1

result = 'P'
for i in arr:
    if i != 0: 
        result = 'C'
        break
print(result)