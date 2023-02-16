num = int(input("整数を入力 --> "))
while num < 1 or num > 20:
    print("1から20までの整数を入力してください。")
    num = int(input("整数を入力 --> "))

total = 1
for i in range(1, num + 1):
    total *= i
    print(f"{i}! = {total}")
