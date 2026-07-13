# Python / AtCoder メモ

## 1. 入力

### 整数をスペース区切りで受け取る

```python
N, Q = map(int, input().split())
```

入力例:

```text
5 10
```

* `input()` で1行を文字列として受け取る
* `.split()` でスペースごとに分割する
* `map(int, ...)` で、それぞれを整数に変換する

---

### 文字列をスペース区切りで受け取る

```python
X, Y = input().split()
```

入力例:

```text
apple orange
```

`map(int, ...)` は、入力された文字列を整数へ変換するときに使う。

文字列のままでよい場合は不要。

---

### 横一列の整数をリストとして受け取る

```python
A = list(map(int, input().split()))
```

入力例:

```text
1 2 3 4 5
```

結果:

```python
A = [1, 2, 3, 4, 5]
```

---

### 複数行の文字列を二次元リストに格納する

```python
name = []

for _ in range(N):
    s, t = input().split()
    name.append([s, t])
```

入力例:

```text
sato haruto
tanaka taro
```

結果:

```python
name = [
    ["sato", "haruto"],
    ["tanaka", "taro"]
]
```

文字列を2つ受け取る場合は、最初に次のように分割する。

```python
s, t = input().split()
```

その後、リストへ追加する。

```python
name.append([s, t])
```

---

### 二次元配列を受け取る

```python
A = []

for _ in range(H):
    A.append(list(map(int, input().split())))
```

より短く書く場合:

```python
A = [list(map(int, input().split())) for _ in range(H)]
```

入力例:

```text
1 2 3
4 5 6
```

結果:

```python
A = [
    [1, 2, 3],
    [4, 5, 6]
]
```

要素には次のようにアクセスする。

```python
A[行][列]
A[i][j]
```

例:

```python
A[0] = [1, 2, 3]  # 0行目
A[1] = [4, 5, 6]  # 1行目
A[2] = [7, 8, 9]  # 2行目
```

---

## 2. 配列・リスト

### 0で初期化したリストを作る

```python
status = [0] * (N + 1)
```

例えば `N = 4` の場合:

```python
status = [0, 0, 0, 0, 0]
```

競技プログラミングでは、番号を `1` から `N` まで使うために、長さを `N + 1` にすることがある。

---

### リストの要素数を数える

```python
A.count(x)
```

例:

```python
A = [1, 2, 1, 3, 1]

count = A.count(1)

print(count)
```

出力:

```text
3
```

---

### 条件に一致する要素を数える

```python
count = 0

for i in range(H):
    for j in range(W):
        if A[i][j] in B:
            count += 1
```

`count =+ 1` ではなく、必ず次のように書く。

```python
count += 1
```

---

### リストの末尾を取り出す

```python
value = stack.pop()
```

`pop()` は、リストの末尾の要素を削除して、その値を返す。

```python
stack = [1, 2, 3]

value = stack.pop()

print(value)
print(stack)
```

出力:

```text
3
[1, 2]
```

スタックとして使う場合:

```python
stack.append(x)  # 末尾へ追加
stack.pop()      # 末尾から取り出す
```

---

## 3. 集合 `set`

### 重複を削除する

```python
B = set()
```

値を追加する場合:

```python
B.add(int(input()))
```

複数個追加する場合:

```python
B = set()

for _ in range(N):
    B.add(int(input()))
```

例:

```python
B = set()

B.add(1)
B.add(2)
B.add(1)

print(B)
```

結果:

```python
{1, 2}
```

同じ値を複数回追加しても、集合には1つだけ保存される。

---

### 値が集合に含まれているか確認する

```python
if x in B:
    print("含まれている")
```

リストよりも、値が存在するかどうかの判定を高速に行えることが多い。

---

## 4. 文字列

### 指定した文字を探す

```python
位置 = S.find("|")
```

例:

```python
S = "abc|def"

index = S.find("|")

print(index)
```

出力:

```text
3
```

指定した位置以降から検索する場合:

```python
index = S.find("|", start)
```

例:

```python
S = "a|b|c"

index = S.find("|", 2)

print(index)
```

出力:

```text
3
```

見つからなかった場合は `-1` が返る。

```python
if S.find("|") == -1:
    print("見つからない")
```

---

### 文字列の先頭と末尾を削除する

先頭から `A` 文字削除する。

```python
S = S[A:]
```

末尾から `B` 文字削除する。

```python
S = S[:-B]
```

両方を同時に行う場合:

```python
S = S[A:-B]
```

例:

```python
S = "abcdefgh"

A = 2
B = 3

S = S[A:-B]

print(S)
```

出力:

```text
cde
```

末尾から削除するときは、`-` を忘れない。

```python
S[:-B]
```

次のコードは意味が異なる。

```python
S[:B]
```

これは、先頭から `B` 文字だけを残す処理。

---

### 文字列の文字を変更する

Pythonの文字列は、直接変更できない。

次のコードはエラーになる。

```python
S[i] = "a"
```

変更したい場合は、一度リストへ変換する。

```python
S = list(S)

S[i] = "a"

S = "".join(S)
```

例:

```python
S = "cat"

S = list(S)
S[0] = "b"
S = "".join(S)

print(S)
```

出力:

```text
bat
```

文字を削除したい場合:

```python
S = list(S)
S[i] = ""
S = "".join(S)
```

ただし、単純な置換なら `replace()` も使える。

```python
S = S.replace("a", "b")
```

---

### 先頭を0埋めする

2桁で0埋めする場合:

```python
print("%02d" % ans)
```

例:

```python
ans = 1

print("%02d" % ans)
```

出力:

```text
01
```

現在は、f文字列を使う書き方も分かりやすい。

```python
print(f"{ans:02d}")
```

3桁の場合:

```python
print(f"{ans:03d}")
```

例:

```text
001
```

---

## 5. 辞書 `dict`

### 文字と数値を対応付ける

```python
order = {
    "A": 1,
    "B": 2,
    "C": 3
}
```

値を取り出す。

```python
print(order["A"])
```

出力:

```text
1
```

辞書を使うと、各文字や名前に対応する値を分かりやすく管理できる。

---

### 辞書のキーを順番に取り出す

```python
for key in order:
    print(key)
```

`for key in order:` と書くと、辞書のキーが順番に入る。

```python
order = {
    "A": 1,
    "B": 2,
    "C": 3
}

for key in order:
    print(key, order[key])
```

出力:

```text
A 1
B 2
C 3
```

キーと値を同時に取り出す場合:

```python
for key, value in order.items():
    print(key, value)
```

---

## 6. 座標移動・方向管理

4方向を配列で管理し、現在の方向を示す番号だけを変更する。

```python
# 東、南、西、北
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
```

現在の方向:

```python
direction = 0
```

対応関係:

```text
direction = 0: 東
direction = 1: 南
direction = 2: 西
direction = 3: 北
```

右へ90度回転する場合:

```python
direction = (direction + 1) % 4
```

前へ進む場合:

```python
x += dx[direction]
y += dy[direction]
```

全体例:

```python
# 東、南、西、北
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x = 0
y = 0
direction = 0

for c in T:
    if c == "R":
        direction = (direction + 1) % 4
    else:
        x += dx[direction]
        y += dy[direction]
```

方向ごとに大量の `if` 文を書くのではなく、移動量を配列へ保存しておくと簡潔に書ける。

---

## 7. ソート

### 勝利数が多い順、IDが小さい順に並べる

```python
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
```

### 解説

次のコードで、プレイヤーIDと勝利数をセットで保存する。

```python
result.append([player_id, win_count])
```

各要素は次の形になる。

```python
[player_id, win_count]
```

例:

```python
[
    [1, 3],
    [2, 5],
    [3, 3]
]
```

ソート部分:

```python
result.sort(key=lambda player: (-player[1], player[0]))
```

ソート条件は次のとおり。

1. `player[1]`、つまり勝利数が多い順
2. 勝利数が同じ場合は、`player[0]`、つまりIDが小さい順

通常のソートは小さい順なので、勝利数にマイナスを付ける。

```python
-player[1]
```

これにより、勝利数が大きいものから並ぶ。

```python
(-player[1], player[0])
```

複数の条件で並べたい場合は、タプルとして指定する。

---

### タプルを使った書き方

リストではなくタプルでもよい。

```python
result.append((player_id, win_count))
```

結果からIDだけを取り出す部分は、内包表記で短くできる。

```python
answer = [player[0] for player in result]

print(*answer)
```

全体を少し短くすると次のようになる。

```python
N = int(input())

result = []

for player_id in range(1, N + 1):
    S = input()
    win_count = S.count("o")
    result.append((player_id, win_count))

result.sort(key=lambda player: (-player[1], player[0]))

answer = [player[0] for player in result]

print(*answer)
```

---

## 8. `range()` の基本

```python
for i in range(N):
    print(i)
```

`0` から `N - 1` まで繰り返す。

```text
0, 1, 2, ..., N - 1
```

---

### 1からNまで繰り返す

```python
for i in range(1, N + 1):
    print(i)
```

```text
1, 2, 3, ..., N
```

---

### 開始位置・終了位置・増加量を指定する

```python
range(開始, 終了, 増加量)
```

例:

```python
for i in range(2, 10, 2):
    print(i)
```

出力:

```text
2
4
6
8
```

終了位置の値自体は含まれない。

---

## 9. よくある間違い

### `int(input)` ではなく `int(input())`

誤り:

```python
B.add(int(input))
```

正しい書き方:

```python
B.add(int(input()))
```

`input` は関数そのものを表す。

`input()` と書くことで、実際に入力を受け取る。

---

### `count =+ 1` ではなく `count += 1`

誤り:

```python
count =+ 1
```

これは実質的に次と同じ。

```python
count = 1
```

正しい書き方:

```python
count += 1
```

---

### Pythonのコメントは `//` ではなく `#`

誤り:

```python
for i in range(N): // 繰り返す
```

正しい書き方:

```python
for i in range(N):  # 繰り返す
```

`//` はPythonでは切り捨て除算として使われる。

```python
7 // 2
```

結果:

```text
3
```

---

### 二次元配列は `A[i][j]`

```python
A[i][j]
```

* `i`: 行番号
* `j`: 列番号

一般的には次の順番でループする。

```python
for i in range(H):
    for j in range(W):
        print(A[i][j])
```

---
