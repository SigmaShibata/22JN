import matplotlib.pyplot as plt
import math
import random

x_nums = []
y_nums = []
x_lines = [1, -1, -1, 1, 1]
y_lines = [1, 1, -1, -1, 1]
x_random = []
y_random = []

for i in range(101):
    theta = (i / 100) * 2 * math.pi
    x_num = math.cos(theta)
    y_num = math.sin(theta)
    x_nums.append(x_num)
    y_nums.append(y_num)

for _ in range(500):
    x_random.append(random.uniform(-1, 1))
    y_random.append(random.uniform(-1, 1))

plt.plot(x_nums, y_nums, color="blue")
plt.plot(x_lines, y_lines, color="red")
plt.scatter(x_random, y_random, color="green")
plt.show()