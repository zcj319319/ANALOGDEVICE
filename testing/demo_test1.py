#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/06/17 14:54
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : demo_test1.py
Software: PyCharm
'''
import sys
import math

import QCP as QCP
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from QCustomPlot2 import *
import QCustomPlot2
import matlab
import matlab.engine

app = QApplication(sys.argv)
window = QMainWindow()
window.resize(800, 600)

customPlot = QCustomPlot()
window.setCentralWidget(customPlot)

graph0 = customPlot.addGraph()
graph0.setPen(QPen(Qt.blue))
graph0.setBrush(QBrush(QColor(0, 0, 255, 20)))

graph1 = customPlot.addGraph()
graph1.setPen(QPen(Qt.red))

engine = matlab.engine.start_matlab()  # 启动matlab
[x,y0,y1]=engine.myfunc(nargout=3)

# for i in range (251):
#     x.append(i)
#     y0.append(math.exp(-i/150.0)*math.cos(i/10.0)) # exponentially decaying cosine
#     y1.append(math.exp(-i/150.0))                  # exponential envelope

graph0.setData(x, y0)
graph1.setData(x, y1)
pAxisTag = AxisTag(customPlot.graph().valueAxis())
pAxisTag.updatePositon(100)

customPlot.rescaleAxes()
customPlot.setInteraction(QCP.iRangeDrag)
customPlot.setInteraction(QCP.iRangeZoom)
customPlot.setInteraction(QCP.iSelectPlottables)
customPlot.axisRect().setRangeZoom(customPlot.xAxis.orientation())
# customPlot.setSelectionRectMode(QCP.srmZoom)
qCPItemTracer = QCPItemTracer(customPlot)
#
qCPItemTracer.setStyle(QCPItemTracer.tsCircle)
qCPItemTracer.setPen(QPen(Qt.red))
current_text =QCPItemText(customPlot)
current_text.setText("dsad")
current_text.position.setParentAnchor(qCPItemTracer.position)
# qCPItemTracer.position.setCoords(1,2)
current_text.position.setCoords(20,0)
textLabel = QCPItemText(customPlot)
textLabel.position.setCoords(30,0.75)
textLabel.setText("hello")
arrow = QCPItemLine(customPlot)
arrow.start.setParentAnchor(textLabel.bottom)
arrow.end.setCoords(20,0)


window.show()
sys.exit(app.exec_())