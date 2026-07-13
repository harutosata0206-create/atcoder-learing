N = int(input())
S = input()
count = 0


for i in range(len(S) - 2):
    if(S[i] == "A" and  S[i+1] == "B" and  S[i+2] == "C"):
        count = count + 1
        print(i + 1)
        break

if(count == 0):
    print("-1")