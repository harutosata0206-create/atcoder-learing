S = input()

pos = []

for i in range(len(S)):
    if S[i] == "#":
        pos.append(i + 1)

for i in range(0, len(pos), 2):
    print(pos[i],",",pos[i + 1],sep="")