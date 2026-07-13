A,B,C,D,E = input().split()

count = {}

count[A] = 1
if B not in count:
    count[B] = 0
count[B] += 1
if C not in count:
    count[C] = 0
count[C] += 1
if D not in count:
    count[D] = 0
count[D] += 1
if E not in count:
    count[E] = 0
count[E] += 1

if len(count) != 2 or count[A] != 2 and count[A] != 3:
    print("No")
else:
    print("Yes")