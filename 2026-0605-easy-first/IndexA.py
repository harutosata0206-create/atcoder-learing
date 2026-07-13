N, M = map(int, input().split())
A = list(map(int, input().split()))

# 最初の長さMの区間の合計
window_sum = sum(A[:M])

# 最初の長さMの区間の重み付き合計
weighted_sum = 0
for i in range(M):
    weighted_sum += (i + 1) * A[i]

ans = weighted_sum

# 区間を1つずつ右にずらす
for left in range(1, N - M + 1):
    # 新しく入る要素
    new_value = A[left + M - 1]

    # 前の区間の合計を使って、重み付き合計を更新
    weighted_sum = weighted_sum - window_sum + M * new_value

    # window_sumも次の区間用に更新
    window_sum = window_sum - A[left - 1] + new_value

    ans = max(ans, weighted_sum)

print(ans)