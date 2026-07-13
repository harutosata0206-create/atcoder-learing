H,W,N = map(int,input().split())
A = []
B = [0] * N
max = 0

for i in range(H):
    A.append(list(map(int,input().split())))

for n in range(N):
    B[n] = int(input())

for k in range(H):
    count = 0
    for l in range(N):
        count = A[k].count(B[l]) + count
    if(max < count):
        max = count

print(max)