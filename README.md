# AtCoder Learning Notes

AtCoderで解いたPythonコードと、問題を解く中で覚えた内容を残すためのリポジトリです。

## フォルダ構成

```text
atcoder-learning/
├── README.md
├── notes/
│   └── python-notes.md
└── solutions/
    └── daily-training/
```

## `notes/python-notes.md`

問題を解いている途中で覚えた内容を、簡単に追記します。

記録する内容:

* Pythonの入力方法
* リスト、文字列、辞書、集合の使い方
* ソートやスライス
* アルゴリズムの基本
* 間違えやすかった書き方

書き方は厳密に統一しません。

基本的には次の形で残します。

````markdown
## 内容の名前

簡単な説明

```python
# コード例
````

注意点があれば1〜2行追加する。

````

新しい内容を学んだときだけ追記し、すでに書いてある内容は増やさず修正します。

ノートが長くなって探しにくくなった場合は、その時点でファイルを分けます。

## `solutions/daily-training/`

Daily Trainingで解いたコードを保存します。

フォルダ名:

```text
YYYY-MM-DD-easy-part-1
YYYY-MM-DD-easy-part-2
YYYY-MM-DD-hard-part-1
YYYY-MM-DD-hard-part-2
````

例:

```text
2026-07-13-easy-part-1/
├── abc400_a.py
├── abc380_b.py
└── abc350_c.py
```

ファイル名には、元のコンテスト番号と問題記号を入れます。

```text
abc400_a.py
abc380_b.py
```

## メモを残す基準

次のどれかに当てはまる場合だけメモします。

* 初めて使った書き方
* 忘れていた文法
* 同じミスをしそうな内容
* 今後も使いそうな解法
* 解説を読んで覚えておきたい内容

簡単に解けて、新しい学びがない問題はコードだけ保存します。

## 基本方針

* 問題を解く時間を優先する
* メモは短く書く
* 最初からきれいに分けすぎない
* 長くなったら後から整理する
* AIは文章整理やファイル分割に使う
