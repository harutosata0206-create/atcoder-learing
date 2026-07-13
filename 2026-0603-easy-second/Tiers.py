S = input()

if S[len(S)-1] == "r":
    print(S[-2:])
else:
    print(S[-3:])