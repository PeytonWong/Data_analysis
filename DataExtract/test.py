#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# for letter in 'peyton':  # 第一个实例
#     if letter == 'h':
#         continue
#     print '当前字母 :', letter
#
#     if letter == 'o':
#         break
#     print '当前字母 :', letter
#
#
# var = 10  # 第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:
#         continue
#     print '当前变量值 :', var
# print "Good bye!"

# x = np.arange(50)
# y = np.arange(50)
# plt.plot(x, y)
# plt.legend(['x', 'y'])
# plt.show()


a = np.arange(27).reshape(3, 3, 3)
print a
