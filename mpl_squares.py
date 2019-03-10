#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt

squares = [1,4,9,16,25]

plt.plot(squares)
plt.title("Squares Number")
plt.xlabel("value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

