import matplotlib.pyplot as plt
import math

x_nums = []
y_nums = []
x_lines = [1, -1, -1, 1, 1]
y_lines = [1, 1, -1, -1, 1]

for i in range(101):
    theta = (i / 100) * 2 * math.pi
    x_num = math.cos(theta)
    y_num = math.sin(theta)
    x_nums.append(x_num)
    y_nums.append(y_num)

plt.plot(x_nums, y_nums, color="blue")
plt.plot(x_lines, y_lines, color="red")
plt.show()