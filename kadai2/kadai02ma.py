# 商品一覧を表示する関数
def display_goods(goods):
    print("商品コード\t価格")
    for key in goods:
        print(f"{key}\t\t{goods[key]}")

# 商品を検索する関数
def search_goods(goods):
    code = int(input("商品コード-->"))
    if code in goods:
        return {"code": code, "name": goods[code]}
    else:
        return {"code": code, "name": None}     # None: 何も入っていないことを表すオブジェクト

# 商品を追加する関数
def append_goods(goods):
    target = search_goods(goods)
    if target["name"] is None:    # オブジェクトがNoneかどうかは「is None」で判定する
        new_code = target["code"]
        new_name = input("商品名-->")
        goods[new_code] = new_name
        print(f"商品コード{new_code}：{new_name} を登録しました。")
    else:
        print(f"商品コード{target['code']}：{target['name']} は既に登録されています。")

# 商品を削除する関数
def delete_goods(goods):
    target = search_goods(goods)
    if target["name"] is None:
        print(f"商品コード{target['code']} は登録されていません。")
    else:
        del goods[target["code"]]
        print(f"商品コード{target['code']}：{target['name']} を削除しました。")

# 商品辞書を作成{商品コード: 商品名}
goods = {10: "テレビ", 20: "電話機", 30: "FAX", 40: "洗濯機", 50: "掃除機"}

# メニューを表示
menu = 0
while menu != 9:
    menu = int(input("一覧:1 追加:2 削除:3 終了:9 -->"))
    if menu == 1:
        display_goods(goods)
    if menu == 2:
        append_goods(goods)
    if menu == 3:
        delete_goods(goods)
print("終了しました。")