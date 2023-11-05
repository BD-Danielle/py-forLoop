n = 5
arr = [[0] * n for _ in range(n)]
num = 1
for i in range(n):
    for j in range(i, n - i): # 0 0 1, 0 1 2, 0 2 3, 0 3 4, 0 4 5, 1 1 17, 1 2 18, 1 3 19, 2 2 25
        arr[i][j] = num
        num += 1
    for j in range(i + 1, n - i): # 1 4 6, 2 4 7, 3 4 8, 4 4 9, 2 3 20, 3 3 21
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