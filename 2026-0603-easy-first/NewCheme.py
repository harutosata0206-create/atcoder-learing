S = list(map(int,input().split()))
check = 0

if(S[0]< 100 or S[len(S)-1]>675):
    check = 1

for i in range(len(S)):
    if(S[i] % 25 != 0):
        check = 1
    
    if(i != len(S) - 1  and S[i]>S[i+1]):
        check = 1

if(check == 0):
    print("Yes")
else:
    print("No")