import csv
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"   # 日本語表示対応フォント設定

# ファイルを読み込みモード、エンコーディング'utf-8-sig'で開く
f_syain = open("syain.csv", "r", encoding="utf-8-sig")   
d_syain = csv.reader(f_syain)        # csvモジュールを使用してファイルを読み込む
f_syutoku = open("syutoku.csv", "r", encoding="utf-8-sig")   
d_syutoku = csv.reader(f_syutoku)    # csvモジュールを使用してファイルを読み込む

l_syain = []                     # 社員データを格納するリスト
l_syutoku = []                   # 資格取得データを格納するリスト
nums_pops = {}                   # 資格取得数毎の人数を格納する辞書{資格数：人数}

# 社員データを１行ずつ取得してリストに格納
for syain in d_syain:
    # はじめの1行以外をリストに格納
    if syain[0] != "syno":
        l_syain.append(syain)

# 資格取得データを１行ずつ取得してリストに格納
for syutoku in d_syutoku:
    # はじめの1行以外をリストに格納
    if syutoku[0] != "syno":
        l_syutoku.append(syutoku)

# 社員リストを１行ずつ取得
for syain in l_syain:
    if syain[0] != "syno":
        cnt = 0
        # 資格取得リストを１行ずつ取得
        for syutoku in l_syutoku:
            # synoが一致すれば、カウント+1
            if syutoku[0] == syain[0]:
                cnt += 1
        # nums辞書の人数をカウント（キーがなければ新規に作成）
        if cnt in nums_pops:
            nums_pops[cnt] += 1
        else:
            nums_pops[cnt] = 1

nums = []       # x軸データ（資格取得数）を格納するリスト
pops = []       # y軸データ（人数）を格納するリスト

# nums_pops辞書のデータをnumsリスト・popsリストに格納
for i in range(max(nums_pops) + 1):
    if i in nums_pops:
        nums.append(i)
        pops.append(nums_pops[i])

# 縦棒グラフを作成及び表示

plt.bar(nums, pops)                             # 縦棒グラフを作成
plt.title("〇〇社における取得資格数毎の人数")     # グラフタイトルを設定
plt.xlabel("取得資格数")                         # x軸のラベルを設定
plt.ylabel("人数")                              # y軸のラベルを設定
plt.xticks(range(max(nums_pops) + 1))           # x軸の目盛りを設定（0から最大取得数まで1刻み）
plt.grid(True, axis="y")                        # y軸のみグリッド表示
plt.show()                                      # 縦棒グラフを表示

f_syain.close()
f_syutoku.close()