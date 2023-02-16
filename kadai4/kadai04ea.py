import csv
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"   # 日本語表示対応フォント設定

# ファイルを読み込みモード、エンコーディング'utf-8-sig'で開く
f = open("kokusei_pop_2015.csv", "r", encoding="utf-8-sig")   
data = csv.reader(f)        # csvモジュールを使用してファイルを読み込む

regions = ["北海道地方", "東北地方", "関東地方", "中部地方", "近畿地方", "中国地方", "四国地方", "九州地方"]
pops = [0] * 8              # 地方毎の人口を格納するリスト（8要素全て0で初期化）

# 読み込んだデータを１行ずつ取得してリストに格納
for row in data:
    # はじめの４行は使用しないので、処理せず次の行へ進む
    if row[0] in ("都道府県コード", "00", "0A", "0B"):
        continue            # continue: 現在の処理を飛ばして次のループへ進む
    else:
        pcode = int(row[0])
        if pcode == 1:
            pops[0] += int(row[6])
        elif 2 <= pcode <= 7:
            pops[1] += int(row[6])
        elif 8 <= pcode <= 14:
            pops[2] += int(row[6])
        elif 15 <= pcode <= 24:
            pops[3] += int(row[6])
        elif 25 <= pcode <= 30:
            pops[4] += int(row[6])
        elif 31 <= pcode <= 35:
            pops[5] += int(row[6])
        elif 36 <= pcode <= 39:
            pops[6] += int(row[6])
        elif 40 <= pcode <= 47:
            pops[7] += int(row[6])

# 円グラフの作成及び表示
plt.pie(
    pops, labels=regions,
    counterclock=False, startangle=90, autopct="%1.2f%%"
    )
plt.title("2015年の日本における地方毎の人口比率")
plt.show()

f.close()