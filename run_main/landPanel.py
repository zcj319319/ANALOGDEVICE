#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/8/11 18:06
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : landPanel.py
Software: PyCharm
'''
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTabWidget

from analog_device import Ui_MainWindow
from run_main.FFT.load_fft_panel import load_fft_ui
from run_main.Memory.load_memory_ui import load_memory_ui
from run_main.TRXXXX.box_link.loadingPanel_box import LoadingPanel_box
from run_main.TRXXXX.usb_link.load_TRXXX import TRPanel_operation


class LoadPanel(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoadPanel, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Evaluation platform")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/AI_pg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        with open('qss/qlist_stylesheet.qss', 'r') as f:
            self.listWidget.setStyleSheet(f.read())
        self.listWidget.itemClicked.connect(self.item_list_clicked)
        self.home.setStyleSheet("background-color:#949494")
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)

        self.tr_panel = TRPanel_operation()
        self.tabwidget = QTabWidget(self.stackedWidget)
        self.tabwidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabwidget.addTab(self.tr_panel,"USB-Link")
        self.tr_panel_box = LoadingPanel_box()
        self.tabwidget.addTab(self.tr_panel_box,"BOX-Link")
        with open('qss/qtabwidget.qss','r') as file:
            self.tabwidget.setStyleSheet(file.read())
        self.stackedWidget.insertWidget(1, self.tabwidget)

        self.memory_panel = load_memory_ui()
        self.stackedWidget.insertWidget(2,self.memory_panel)
        self.fft_panel=load_fft_ui()
        self.stackedWidget.insertWidget(3,self.fft_panel)
        self.help = QtWidgets.QWidget()
        self.stackedWidget.insertWidget(4,self.help)
        self.setStyleSheet('''
                            QTextBrowser{
                                    border: 1px solid gray;
                                    border-radius:10px;
                                    margin-top:4ex;
                                    font-family:SegoeUI;
                                    font:bold 12px;
                                }
                            ''')
    def item_list_clicked(self):
        item = self.listWidget.selectedItems()[0]
        if item.text() == "Home":
            self.stackedWidget.setCurrentIndex(0)
        elif item.text() == "Initial":
            self.stackedWidget.setCurrentIndex(1)
        elif item.text() == "Memory":
            self.stackedWidget.setCurrentIndex(2)
        elif item.text() == "FFT":
            self.stackedWidget.setCurrentIndex(3)
        else:
            self.stackedWidget.setCurrentIndex(4)






