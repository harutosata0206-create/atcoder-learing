N = int(input())

pastNum = []

while N not in pastNum:
    pastNum.append(N)
    ans = 0
    sN = str(N)
    for n in range(len(sN)):
        ans += int(sN[n])**2
    N = ans
    if(N == 1):
        print("Yes")
        exit()
print("No")