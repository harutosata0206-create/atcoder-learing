N = int(input())
X = []
Y = []

for n in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

for k in range(N):
    l = 0
    max = 0
    for i in range(N-1,-1,-1):
        l = (X[k] - X[i]) ** 2 + (Y[k] - Y[i]) ** 2
        if l >= max:
            max = l
            ans = i
    print(ans+1)