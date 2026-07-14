N = int(input())
A = list(map(int,input().split()))
answer = []

for i in range(N):
    if A[i] % 2 == 0:
        answer.append(A[i])

print(*answer)
