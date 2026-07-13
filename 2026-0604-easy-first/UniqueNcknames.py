N = int(input())

S = []
T = []

for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

for i in range(N):
    can_use_s = True
    can_use_t = True

    for j in range(N):
        if i == j:
            continue

        # 自分の姓 S[i] が、他人の姓または名とかぶるなら使えない
        if S[i] == S[j] or S[i] == T[j]:
            can_use_s = False

        # 自分の名 T[i] が、他人の姓または名とかぶるなら使えない
        if T[i] == S[j] or T[i] == T[j]:
            can_use_t = False

    # 姓も名も使えないなら無理
    if can_use_s == False and can_use_t == False:
        print("No")
        exit()

print("Yes")