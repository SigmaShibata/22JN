print("任意の数の整数を入力（各整数間は半角スペースで区切る）")
num_list = input("-->").split()
total_int = 0
total_str = ""
# 
for i in range(len(num_list)):
    total_int += int(num_list[i])
    total_str += num_list[i]
    if i != len(num_list) - 1:
        total_str += "と"
# 
print(f"{total_str}の和は{total_int}です。")