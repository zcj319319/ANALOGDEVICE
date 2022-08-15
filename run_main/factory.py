#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/8/10 14:12
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : factory.py
Software: PyCharm
'''

from PyQt5.QtWidgets import QTreeWidgetItem, QHBoxLayout, QLineEdit, QGroupBox, QPushButton


class Create_data:
    def __init__(self):
        self.groupbox = None
        self.zero = QPushButton("0")
        self.one = QPushButton("0")
        self.two = QPushButton("0")
        self.three = QPushButton("0")
        self.four = QPushButton("0")
        self.five = QPushButton("0")
        self.six = QPushButton("0")
        self.seven = QPushButton("0")
        self.line = QLineEdit()
        self.line.setText("0x00")
        self.h1_layout = QHBoxLayout()
        self.line.setDisabled(True)
        self.zero.clicked.connect(lambda: self.item_change(self.zero))
        self.one.clicked.connect(lambda: self.item_change(self.one))
        self.two.clicked.connect(lambda: self.item_change(self.two))
        self.three.clicked.connect(lambda: self.item_change(self.three))
        self.four.clicked.connect(lambda: self.item_change(self.four))
        self.five.clicked.connect(lambda: self.item_change(self.five))
        self.six.clicked.connect(lambda: self.item_change(self.six))
        self.seven.clicked.connect(lambda: self.item_change(self.seven))

    def groupbox_init(self, obj):
        self.groupbox = QGroupBox(obj)
        self.groupbox.setLayout(self.h1_layout)
        self.h1_layout.addWidget(self.seven)
        self.h1_layout.addWidget(self.six)
        self.h1_layout.addWidget(self.five)
        self.h1_layout.addWidget(self.four)
        self.h1_layout.addWidget(self.three)
        self.h1_layout.addWidget(self.two)
        self.h1_layout.addWidget(self.one)
        self.h1_layout.addWidget(self.zero)
        self.h1_layout.setContentsMargins(0, 0, 0, 0)
        self.h1_layout.setSpacing(0)
        return self.groupbox

    def item_change(self, btn):
        if btn.text() == "0":
            btn.setText("1")
            self.line_counting()
        else:
            btn.setText("0")
            self.line_counting()

    def setVisable(self, lis_num):
        for i in lis_num:
            if i == 0:
                self.zero.setDisabled(True)
                self.zero.setStyleSheet('''QPushButton{background:#5a586c}''')
            elif i == 1:
                self.one.setDisabled(True)
                self.one.setStyleSheet('''QPushButton{background:#5a586c}''')
            elif i == 2:
                self.two.setDisabled(True)
                self.two.setStyleSheet('''QPushButton{background:#5a586c}''')
            elif i == 3:
                self.three.setDisabled(True)
                self.three.setStyleSheet('''QPushButton{background:#5a586c}''')
            elif i == 4:
                self.four.setDisabled(True)
                self.four.setStyleSheet('''QPushButton{background:#5a586c}''')
            elif i == 5:
                self.five.setDisabled(True)
                self.five.setStyleSheet('''QPushButton{background:#5a586c}''')
            elif i == 6:
                self.six.setDisabled(True)
                self.six.setStyleSheet('''QPushButton{background:#5a586c}''')
            elif i == 7:
                self.seven.setDisabled(True)
                self.seven.setStyleSheet('''QPushButton{background:#5a586c}''')

    def line_counting(self):
        text_str = self.seven.text() + self.six.text() + self.five.text() + self.four.text() + self.three.text() + self.two.text() + self.one.text() + self.zero.text()
        self.line.setText(hex(int(text_str, 2)))
