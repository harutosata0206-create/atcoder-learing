# 毎日の回答日記

## 2026-0713

### 問題

/2026-0710-easy-first

### 学習メモ

#### lineで分割を考えたいときは一度lineを取得してから `L = line[0] content = line[1:]`このように切る

分割をしたいときは一度すべて受け取ってから分割する

```py
for i in range(N):
    line = list(map(int,input().split()))
    L = line[0]
    content = line[1:]
    A.append(content)
```

---

#### 辞書型での記録

ある数などに対応していてどんどん書き換わるような処理を書きたいときには辞書型で記録する

```python
N = int(input())
A = list(map(int, input().split()))

last_position = {}
answer = N + 1

for i in range(N):
    value = A[i]

    if value in last_position:
        length = i - last_position[value] + 1
        answer = min(answer, length)

    last_position[value] = i

if answer == N + 1:
    print(-1)
else:
    print(answer)
```

このようにlast_positionに数字と最後に出てきた座標を書き残しておくことで計算量が非常に少なくなり効率的になる

#### min(~,~)

min関数 

カッコ内の中から最小の数を抜き出す関数
文字列などでは文字の長さからminを導き出す

##### 参考文献
https://paiza.jp/works/reference/article-python-min

#### 一言振り返り
C問題は解けはするが計算量などを考えて解く必要があると感じた。  
どんどん解いていってある程度慣れていかないといけないと感じた。  
ただ計算量に対してもある程度の知識はあるのでそれを応用できるくらい競技プログラミングのようなアルゴリズム問題になれていく。  

<br />

---


## 2026-0714

### 回答問題

/2026-0713-easy-first

### *answer

pythonではprint(*answer)と記述すると、リストの表示が変わる

### itertools

要素の並び替えをすべて作るための機能
並び替えをするときはこれを使うとよい

### C問題(MakeIsomorphic.py)解説

`G = [[False] * N for _ in range(N)]`

隣接行列を作っている  
N=4なら
```txt
False False False False
False False False False
False False False False
False False False False
```
これで辺があるかないかを探している

---

先ほどのfalseの配列に

```py
for _ in range(MG):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u][v] = True
    G[v][u] = True
```

Gの配列を登録した  
無向グラフなのでu→v , v→uの両方をTrueに変更  

Hも同様に変更

---

費用を保存する表を作る

```py
cost = [[0] * N for _ in range(N)]
```

cost[i][j] は、グラフHの頂点 i と頂点 j の間の辺を追加または削除する料金を表します

---

```py
for i in range(N - 1):
    A = list(map(int, input().split()))

    for j in range(i + 1, N):
        cost[i][j] = A[j - i - 1]
        cost[j][i] = A[j - i - 1]
```

この時costは
```py
cost = [
    [0,  10, 20, 30],
    [10, 0,  40, 50],
    [20, 40, 0,  60],
    [30, 50, 60, 0]
]
```
このようになっている

---

最小値を出すためにanswer = float("inf") (無限)を入れる

---

すべての向きを試すために`for p in permutations(range(N)):`  

pの向きで二重for文(どれくらいの料金がかかるかを全探索)  

```py
for i in range(N):
    for j in range(i + 1, N):
```

```txt
(0, 1)
(0, 2)
(0, 3)
(1, 2)
(1, 3)
(2, 3)
```

---

`g_edge = G[i][j]`で先ほどのtrue,falseから線があるかないかを判別

---

`h_edge = H[p[i]][p[j]]`  

これは回した頂点と考えるのが良い

---

`total += cost[p[i]][p[j]]`  
料金は回した側のを足す

---

#### 最重要解法

```py
for p in permutations(range(3)):
```

で頂点をすべての通り考えること。  

```py
for p in permutations(range(3)):
    print(p)
```

この出力は

```txt
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)
```

このようになる  

単純無向グラフである以上左右反転させた場合も考えなければならない

### 一言振り返り

マジで難しい  
C問題はしっかりと難しいなと感じた  
慣れもそうだし基礎的なpythonへの知識が乏しいので、これからもしっかり勉強してある程度使えるレベルに上がりたい  

<br />

---

## 2026-0715

### 回答問題

/2026-0714-easy-first

### a.discard() 

```py
if B[i] in list:
    list.remove(B[i])
```

これではremoveが引っかからないが、計算量が大きくなってしまう  
そこで

```py
list.discard(B[i])
```

これはdiscardという、list内に存在するかにかかわらずB[i]を捨てることが出来る関数でいちいちif文などをつけなくても処理を行うことが出来る  

### *A

```py
K,*A = map(int,input().split())
```

この時Aには残りの数値(K以外)がリストとして記録されるようになる

### C問題(E.py)解説

正解コード
```py
N, M = map(int, input().split())

used_by = [[] for _ in range(N + 1)]
remaining = [0] * M

for dish in range(M):
    K, *A = map(int, input().split())
    remaining[dish] = K
    for ingredient in A:
        used_by[ingredient].append(dish)

B = list(map(int, input().split()))

answer = 0

for ingredient in B:
    for dish in used_by[ingredient]:
        remaining[dish] -= 1
        answer += remaining[dish] == 0
    print(answer)
```

- used_by
食材xを使っている料理名を格納する(食材(B)から料理の値を変えることが出来る→計算量が減る)

- remaining
残りの苦手食材量を記録  
remaining[dish] = Kで対応する食材量になっている


### 今日の一言

よくよく見てみたら解けそうな問題だった  
ただBを主体で見るためにused_byを作成するっていうところが全然思いつかなかったので計算量に関してと、それを実現するコードを書く力がめちゃくちゃ足りないと感じた  
ただどんどん解くスピードや解法へのアプローチの仕方がよくなってきていると感じるので、これからもどんどん学習を進めたい  