'''
Author: your name
Date: 2020-12-28 20:48:50
LastEditTime: 2020-12-28 21:08:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /numerical_analysis/code/chapter5/accurate.py
'''
from math import log, sqrt, atan

x = 1.0

y = -log(x-sqrt(2*x)+1)/sqrt(2) + log(x+sqrt(2*x)+1)/sqrt(2) - sqrt(2)*atan(1-sqrt(2*x)) + sqrt(2)*atan(1+sqrt(2*x)) - 2*atan(x)/sqrt(x)

print(y)


