import csv

# 班分けデータを、list(list(set()))の3次元配列で管理する方針とします。
# 5行9列のset（計45個）が存在するイメージです。
weeks = []  # 週ごとに班分けを格納するリスト（3次元配列）

# csvファイルを読み込み、データをweeksリストに格納
for i in range(1, 6):
    file = open(f"csv13/班分け_{i}.csv", "r", encoding="utf-8-sig")
    data = csv.reader(file) # csvモジュールを使用してファイルを読み込む
    groups = []         # 1週分の班分けを格納するリスト（2次元配列）
    for row in data:
        names =set()    # setオブジェクト（JavaのSetと性質は同じ）
        row0 = row[0].split(",")
        for name in row0:
            if len(name) == 2:  # "n班"の部分は無視
                continue
            names.add(name)
        groups.append(names)
    weeks.append(groups)    
    file.close()

# 1.重複班チェック
# 2.重複ペアチェック（ついでにチェックします）
duplicated_groups = []   # 重複班を管理するリスト
duplicated_members = {}  # 同じ班になった人の回数を管理する2次元辞書
for i, week in enumerate(weeks, start=1):   # i週目
    for j, group in enumerate(week, start=1):   # j班
        # 1.重複班チェック処理
        for k in range(i+1, 6): # 比較対象（k週目） ※i週目より後の週のみチェック
            for l in range(1, 10):  # 比較対象（l班）
                if group == weeks[k-1][l-1]: # setは要素順を考慮しないので、単純比較が可能
                    duplicated_groups.append(f"{i}週目の{j}班と{k}週目の{l}班")
        # 2.重複ペアチェック処理
        for member in group:    # 班ごとに総当たりで数え上げ
            for other in group:
                if member != other: # 自分自身は除く
                    if member in duplicated_members:
                        if other in duplicated_members[member]: # keyが存在すれば値を+1、しなければ値1で追加
                            duplicated_members[member][other] += 1
                        else:
                            duplicated_members[member][other] = 1
                    else:
                        duplicated_members[member] = {other: 1}

# 重複班を表示
if len(duplicated_groups) > 0:
    for text in duplicated_groups:
        print(text)
else:
    print("重複班は存在しませんでした")

# 2回以上同じ班になったペアを表示
is_duplicated = False   # 2回以上同じ班になったペアが存在するかを管理するフラグ
for member in duplicated_members:
    for other in duplicated_members[member]:
        if duplicated_members[member][other] > 1:
            print(f"{member}さんと{other}さん：{duplicated_members[member][other]}回")
            is_duplicated = True
            del duplicated_members[other][member]   # 対称データを削除（重複する情報のため）
if not is_duplicated:
    print("2回以上同じ班になったペアはありませんでした。")