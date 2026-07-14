N = int(input())

Mg = int(input())

for i in range(Mg):

# from itertools import permutations

# N = int(input())

# # グラフG
# MG = int(input())
# G = [[False] * N for _ in range(N)]

# for _ in range(MG):
#     u, v = map(int, input().split())
#     u -= 1
#     v -= 1
#     G[u][v] = True
#     G[v][u] = True

# # グラフH
# MH = int(input())
# H = [[False] * N for _ in range(N)]

# for _ in range(MH):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     H[a][b] = True
#     H[b][a] = True

# # 辺を追加・削除する料金
# cost = [[0] * N for _ in range(N)]

# for i in range(N - 1):
#     A = list(map(int, input().split()))

#     for j in range(i + 1, N):
#         cost[i][j] = A[j - i - 1]
#         cost[j][i] = A[j - i - 1]

# answer = float("inf")

# # p[i] = Gの頂点iに対応させるHの頂点番号
# for p in permutations(range(N)):
#     total = 0

#     for i in range(N):
#         for j in range(i + 1, N):

#             # Gのi-j間に辺があるか
#             g_edge = G[i][j]

#             # 対応するHのp[i]-p[j]間に辺があるか
#             h_edge = H[p[i]][p[j]]

#             # 辺の有無が異なるなら、Hを変更する必要がある
#             if g_edge != h_edge:
#                 total += cost[p[i]][p[j]]

#     answer = min(answer, total)

# print(answer)
