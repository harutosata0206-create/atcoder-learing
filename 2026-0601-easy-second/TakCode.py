def check(S, y, x):
    # 左上 3×3 が全部 #
    for dy in range(3):
        for dx in range(3):
            if S[y + dy][x + dx] != "#":
                return False

    # 左上 3×3 の右と下に隣接する部分が全部 .
    for i in range(4):
        if S[y + i][x + 3] != ".":
            return False
        if S[y + 3][x + i] != ".":
            return False

    # 右下 3×3 が全部 #
    for dy in range(3):
        for dx in range(3):
            if S[y + 6 + dy][x + 6 + dx] != "#":
                return False

    # 右下 3×3 の左と上に隣接する部分が全部 .
    for i in range(4):
        if S[y + 5][x + 5 + i] != ".":
            return False
        if S[y + 5 + i][x + 5] != ".":
            return False

    return True

N,M = map(int,input().split())

S = []

for n in range(N):
    S.append(input())

#2重for文
for x_start in range(N-8):
    for y_start in range(M-8):
        result = check(S,x_start,y_start)
        if result == True:
            print(x_start + 1,y_start + 1)