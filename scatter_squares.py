#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# 传递实参edgecolor='none'删除数据点的轮廓
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,edgecolor='none', s=40)

plt.title("Squares Number")
plt.xlabel("value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which="major", labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

# 自动保存图表
# plt.savefig('squares_plot.png', bbox_inches='tight')
