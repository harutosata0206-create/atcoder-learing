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
