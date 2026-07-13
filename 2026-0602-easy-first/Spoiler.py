S = input()

l = S.find("|")
r = S.find("|", l + 1)

print(S[:l] + S[r + 1:])