H, W = map(int, input().split())
R, C = map(int, input().split())

if H == 1 and W == 1:
    print(0)
elif H == 1 or W == 1:
    if R == 1 and C == 1 or R == 1 and C == W or R == H and C == 1 or R == H and C == W:
        print(1)
    else:
        print(2)
else:
    if R == 1 and C == 1 or R == 1 and C == W or R == H and C == 1 or R == H and C == W:
        print(2)
    elif R == 1 or C == 1 or R == H or C == W:
        print(3)
    else:
        print(4)
