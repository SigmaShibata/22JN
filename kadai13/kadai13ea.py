nums_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
choice = []
total = 0
# 盤面を表示する関数
def display_nums(nums_list: list[list]):
    for nums in nums_list:
        for num in nums:
            print(num, end="\t")
        print()
# 入力された数字が盤面に存在するかチェックする関数
def check_nums(num: int, nums_list: list[list]):
    for nums in nums_list:
        if num in nums:
            return True
    return False
# 入力された数字が含まれる行と列を*に置換する関数
def change_nums(num: int, nums_list: list[list]):
    for i in range(4):
        for j in range(4):
            if num == nums_list[i][j]:
                nums_list[i] = ["*", "*", "*", "*"]
                for k in range(4):
                    nums_list[k][j] = "*"
# メイン処理
for _ in range(4):
    display_nums(nums_list)
    num = int(input("表示されている数の中から１つ入力してください --> "))
    while not check_nums(num, nums_list):
        num = int(input("エラー：再度入力してください --> "))
    choice.append(num)
    total += int(num)
    change_nums(num, nums_list)

print("選んだ数字：", end="")
print(*choice)
print(f"選んだ数字の合計：{total}")
