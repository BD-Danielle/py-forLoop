n = 5
arr = [[0] * n for _ in range(n)]
print(arr)
num = 1
for i in range(n):
    for j in range(i, n - i):
        arr[i][j] = num
        num += 1
    for j in range(i + 1, n - i):
        arr[j][n - i - 1] = num
        num += 1
    for j in range(i + 1, n - i):
        arr[n - i - 1][n - j - 1] = num
        num += 1
    for j in range(i + 1, n - i - 1):
        arr[n - j - 1][i] = num
        num += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end="\t")
    print()