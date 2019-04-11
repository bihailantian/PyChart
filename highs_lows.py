#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import csv

import matplotlib.pyplot as plt

# 读取文件头
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)

    # 打印文件头及其位置
    for index, column_header in enumerate(head_row):
        print(index, column_header)

    # 打印每一天的最高温
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)

    # 设置绘图窗口的尺寸
    fig = plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(highs, c='red')

    # 设置图形的格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
