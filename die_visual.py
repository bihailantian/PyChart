#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pygal

from die import Die

# 创建一个D6
die1 = Die()
die2 = Die()
# 掷几次骰子，并将结果存储在一个列表中
results = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

print(results)

# 分析结果
frequencies = []

max_result = die1.num_sides + die2.num_sides
for value in range(2,  max_result+ 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = [ '2', '3', '4', '5', '6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual2.svg')

