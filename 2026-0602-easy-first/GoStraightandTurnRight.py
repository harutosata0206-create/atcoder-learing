N = int(input())
T = input()

count = 0
sx = 1
sy = 0
x = 0
y = 0

for i in range(N):
    if(T[i] == "R"):
        if(count % 4 == 0):
            sx = 0
            sy = -1
            count = count + 1
        elif(count % 4 == 1):
            sx = -1
            sy = 0
            count = count + 1
        elif(count % 4 == 2):
            sx = 0
            sy = 1
            count = count + 1
        else:
            sx = 1
            sy = 0
            count = count + 1
    if(T[i] == "S"):
        x = x + sx
        y = y + sy

print(x,y)