N = int(input())
A = []

for i in range(N):
    line = list(map(int,input().split()))
    L = line[0]
    content = line[1:]
    A.append(content)

X,Y = map(int,input().split())

print(A[X-1][Y-1])
