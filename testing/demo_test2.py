#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/06/29 14:23
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo_test2.py
Software: PyCharm
'''
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

fig, ax = plt.subplots()
x = [1,2,3,4,5]
y = [1,2,3,4,5]
ax.scatter(x, y)

po_annotation = []
for i in range(len(x)):
    # 标注点的坐标
    point_x = x[i]
    point_y = y[i]
    point, = plt.plot(point_x, point_y, 'o', c='darkgreen')
    # 标注plt.annotate
    annotation = plt.annotate(y[i], xy=(x[i], y[i]), size=15)
    # 默认鼠标未指向时不显示标注信息
    annotation.set_visible(False)
    po_annotation.append([point, annotation])

def on_move(event):
    visibility_changed = False
    for point, annotation in po_annotation:
        should_be_visible = (point.contains(event)[0] == True)

        if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)
    if visibility_changed:
        plt.draw()

on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)
plt.show()
