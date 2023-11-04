# 巢狀迴圈模擬井字遊戲的棋盤：
for i in range(3):
    for j in range(3):
        if j < 2:
            print("_|", end="")
        else:
            print("_", end="")
    print()
    if i < 2:
        print(" | | ")