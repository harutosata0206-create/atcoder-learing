N,M = map(int,input().split())

if (N % 2 == 0 and N / 2 >= M) or (N % 2 != 0 and N // 2 + 1 >= M):
    print("Yes")
else:
    print("No")


# N, M = map(int, input().split())

# if M <= (N + 1) // 2:
#     print("Yes")
# else:
#     print("No")