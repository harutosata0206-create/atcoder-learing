N = int(input())
A = list(map(int,input().split()))

answer = -1

for i in range(N):
    if A[i:].count(A[i]) > 1:
        x = A[i+1:].index(A[i]) + 2
        if answer == -1 or answer > x:
            answer = x

print(answer)

# 回答例
# N = int(input())
# A = list(map(int, input().split()))

# last_position = {}
# answer = N + 1

# for i in range(N):
#     value = A[i]

#     if value in last_position:
#         length = i - last_position[value] + 1
#         answer = min(answer, length)

#     last_position[value] = i

# if answer == N + 1:
#     print(-1)
# else:
#     print(answer)
