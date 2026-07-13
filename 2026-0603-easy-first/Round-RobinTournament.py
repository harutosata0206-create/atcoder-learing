N = int(input())

result = []

for player_id in range(1, N + 1):
    S = input()
    win_count = S.count("o")

    result.append([player_id, win_count])

result.sort(key=lambda player: (-player[1], player[0]))

answer = []

for player in result:
    answer.append(player[0])

print(*answer)