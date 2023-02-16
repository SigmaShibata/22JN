nums = []
for i in range(6):
    again = True
    while again:
        num = int(input(str(i + 1) + "つ目の整数を入力 --> "))
        if num in nums:
            print("異なる整数を入力してください。")
        else:
            nums.append(num)
            again = False
nums.sort()
nums.reverse()
print(f"3番目に大きい数は{nums[2]}です。")