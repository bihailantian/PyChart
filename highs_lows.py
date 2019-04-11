#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import csv

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
