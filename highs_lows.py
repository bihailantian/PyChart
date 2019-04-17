#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import csv
from datetime import datetime

import matplotlib.pyplot as plt

first_date = datetime.strptime("2014-07-01", "%Y-%m-%d")
print(first_date)

# 读取文件头
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)

    # 打印文件头及其位置
    for index, column_header in enumerate(head_row):
        print(index, column_header)

    #  从文件中获取日期、最高气温和最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        low = int(row[3])
        lows.append(low)
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    print(highs)

    # 设置绘图窗口的尺寸
    fig = plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    # 着色
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)

    # 设置图形的格式
    plt.title("Daily high temperatures 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
