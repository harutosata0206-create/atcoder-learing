X = int(input())

N = int(input())

W = list(map(int,input().split()))

Q = int(input())

already = {}

for n in range(Q):
    P = input()
    Pi= int(P)

    if P not in already:
        already[P] = 1
        X = X + W[Pi-1]
    elif already[P] == 1:
        already[P] = 0
        X = X - W[Pi-1]
    elif already[P] == 0:
        already[P] = 1
        X = X + W[Pi-1]
    print(X)