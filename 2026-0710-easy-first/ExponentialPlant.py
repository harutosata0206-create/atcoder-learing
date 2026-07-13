H = int(input())
tall = 0
count = 0
up = 1

while tall<=H:
    tall = tall + up
    up *= 2
    count += 1

print(count)
