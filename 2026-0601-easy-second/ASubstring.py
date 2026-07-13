N,A,B = map(int,input().split())
S = input()

if A != 0:
    S = S[A:]
if B != 0:
    S = S[:-B]

print(S)