"""
横書きを縦書きに変換する
※入力は全て全角文字
"""

num = int(input("入力する行数 --> "))
text = []       # 入力された文字列を格納するリスト
max_length = 0  # 入力された文字列の最大長を格納する変数

# 各行の文字列を入力
for i in range(num):
    # 入力された文字列の1文字ずつを要素とするリストを作成
    row = list(input(str(i + 1) + "行目 --> "))
    # 最大長の更新判定
    if len(row) > max_length:
        max_length = len(row)
    text.append(row)            # 2次元リストを作成

# 入力された文字列を縦書きで表示
for i in range(max_length):
    for j in range(num - 1, -1, -1):
        # 出力すべき文字が存在するかの判定
        if len(text[j]) > i:
            print(text[j][i], end="")
        else:
            print("　", end="")
    print()