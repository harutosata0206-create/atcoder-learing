N, D = map(int, input().split())

S = []
ans = 0
count = 0

for i in range(N):
    S.append(input())

for n in range(D):
    ok = True

    for k in range(N):
        if S[k][n] == "x":
            ok = False
            break

    if ok:
        count += 1
        if ans < count:
            ans = count
    else:
        count = 0

print(ans)