#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from datetime import datetime


# python列表获取元素最后一个值的方法
list1 = [1, 2, 3, 4, 5]

print(list1[-1])



first_date = datetime.strptime("2014-07-01","%Y-%m-%d")
first_date2 = datetime.strptime("2014-07-01","%y")
print(first_date)
print(first_date2)
