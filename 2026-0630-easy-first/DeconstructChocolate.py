H, W, Q = map(int, input().split())

query = []
for i in range(Q):
    query.append(list(map(int, input().split())))

for n in range(Q):
    if query[n][0] == 1:
        print(query[n][1] * W)
        H = H - query[n][1]
    elif query[n][0] == 2:
        print(query[n][1] * H)
        W = W - query[n][1]
