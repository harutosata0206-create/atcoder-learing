S = input()

count = {}
# dictionary型を使うことで各文字に対応する数をわかりやすく管理できる

# 各文字の出現回数を数える
for ch in S:
    if ch not in count:
        count[ch] = 0
    count[ch] += 1

freq_count = {}

# 「出現回数ごとに何種類あるか」を数える
for value in count.values():
    if value not in freq_count:
        freq_count[value] = 0
    freq_count[value] += 1

# 各出現回数に対して、文字の種類数が2でなければダメ
for num in freq_count.values():
    if num != 2:
        print("No")
        exit()

print("Yes")