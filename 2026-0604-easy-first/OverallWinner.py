N = int(input())
S = input()

countA = 0
countT = 0
first = 0
for n in range(N):
    if S[n] == "T":
        countT = countT + 1
    else:
        countA = countA + 1
    if countT == N / 2 and first == 0:
        first = 1
    elif countA == N / 2 and first == 0:
        first = 2

#a.countでもいけたかも

if countA < countT:
    print("T")
elif countA > countT:
    print("A")
else:
    if(first == 1):
        print("T")
    elif(first == 2):
        print("A")