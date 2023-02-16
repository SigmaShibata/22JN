num = int(input("整数を入力 --> "))
while num < 1:
    print("1以上の整数を入力してください。")
    num = int(input("整数を入力 --> "))

for i in range(num):
    ast = "*" * i
    space = " " * (num - i - 1)
    print(space + ast + "*" + ast + space)