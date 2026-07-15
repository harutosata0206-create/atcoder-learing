N,M = map(int,input().split())
menu = []
B = []

for m in range(M):
    l = list(map(int,input().split()))
    menu.append(l[1:])

B = list(map(int,input().split()))

for n in range(N):
    # for _ in 





# N, M = map(int, input().split())

# used_by = [[] for _ in range(N + 1)]
# remaining = [0] * M

# for dish in range(M):
#     K, *A = map(int, input().split())
#     remaining[dish] = K
#     for ingredient in A:
#         used_by[ingredient].append(dish)

# B = list(map(int, input().split()))

# answer = 0

# for ingredient in B:
#     for dish in used_by[ingredient]:
#         remaining[dish] -= 1
#         answer += remaining[dish] == 0
#     print(answer)