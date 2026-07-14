A = []
n = 0

A.append(int(input()))

while A[n] != 0:
    n = n + 1
    A.append(int(input()))

for i in range(len(A)):
    print(A[n-i])
