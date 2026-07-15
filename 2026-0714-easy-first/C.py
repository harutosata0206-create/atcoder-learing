N,M = map(int,input().split())

list = []

for n in range(N):
    list.append(n+1)

for m in range(M):
    A,B = map(int,input().split())
    if B in list:
        list.remove(B)

if len(list) > 1:
    print(-1)
else:
    print(*list)


# N, M = map(int, input().split())

# s = set(range(1, N + 1))

# for _ in range(M):
#     _, lose = map(int, input().split())
#     s.discard(lose)

# print(-1 if len(s) != 1 else s.pop())