N,K = input().split()

K = int(K)
count = 0

for n in range(int(N),0,-1):
    num = 0
    ns = str(n)
    for i in range(len(ns)):
        Ni = int(ns[i])
        num += Ni
    if num == K:
        count += 1
print(count)