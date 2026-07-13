N = int(input())

a = []

for i in range(N):
    row =[]
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(a[i-1][j-1] + a[i-1][j])
    a.append(row)
    print(*row)