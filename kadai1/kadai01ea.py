a, b, c = input("整数を3つ入力 --> ").split()
sum = int(a) + int(b) + int(c)
# 通常の記法
print(a + "と" + b + "と" + c + "の和は" + str(sum) + "です。")
# formatメソッドを使用した場合
print("{}と{}と{}の和は{}です。".format(a, b, c, sum))
# f文字列を使用した場合
print(f"{a}と{b}と{c}の和は{sum}です。")