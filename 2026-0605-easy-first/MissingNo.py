# ソートしてからnとn+1を比べて飛んでたらn+1を出力する方針

N = int(input())

A = list(map(int,input().split()))

A.sort()

for i in range(N):
    if(A[i] != A[i+1] - 1):
        print(A[i]+1)
        exit()