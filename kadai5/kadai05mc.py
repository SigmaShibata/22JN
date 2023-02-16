import matplotlib.pyplot as plt
import math
import random

plt.rcParams['font.family'] = "MS Gothic"   # 日本語表示対応フォント設定

x_nums = []
y_nums = []
x_lines = [1, -1, -1, 1, 1]
y_lines = [1, 1, -1, -1, 1]
x_random_in = []
y_random_in = []
x_random_out = []
y_random_out = []
num_plot = 500  # ランダムな座標を選ぶ回数

for i in range(101):
    theta = (i / 100) * 2 * math.pi
    x_num = math.cos(theta)
    y_num = math.sin(theta)
    x_nums.append(x_num)
    y_nums.append(y_num)

for _ in range(num_plot):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if math.sqrt(x**2 + y**2) <= 1: # 円の領域に含まれるか
        x_random_in.append(x)
        y_random_in.append(y)
    else:
        x_random_out.append(x)
        y_random_out.append(y)

calc_pi = (4 * len(x_random_in)) / num_plot
plt.plot(x_nums, y_nums, color="blue")
plt.plot(x_lines, y_lines, color="red")
plt.scatter(x_random_out, y_random_out, color="green")
plt.scatter(x_random_in, y_random_in, color="orange")
plt.text(-1, 1.2, f"円周率の近似値：{calc_pi}")
plt.show()