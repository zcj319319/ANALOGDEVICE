#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/8/12 16:53
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : load_memory_ui.py
Software: PyCharm
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem, QHeaderView

from run_main.Memory.memory_UI import Ui_MainWindow
from run_main.factory import Create_data


class load_memory_ui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setTreeWidget()
        self.func_descibe.itemClicked.connect(self.print_where_is)
        self.ApplyChanges.clicked.connect(self.traverse)
        self.spi_config_a()
        self.spi_config_b()
        self.chip_configuration()
        self.device_index()
        self.transfer()
        self.chip_pin_control_1()
        self.chip_pin_control_2()
        self.chip_pin_control_3()
        self.clock_divider_control()
        self.clkdiv_phase()
        self.clock_driver_and_sysref_control()
        self.clock_delay_control()
        self.ApplyChanges.setStyleSheet("background-color:#f8f8ff")
        self.Resetchip.setStyleSheet("background-color:#f8f8ff")
        self.software_defaults.setStyleSheet("background-color:#f8f8ff")
        self.Export.setStyleSheet("background-color:#f8f8ff")
        with open('qss/QlineEdit.qss', 'r') as f:
            self.search_register.setStyleSheet(f.read())


    def spi_config_a(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0000")
        root.setText(1, "SPI_CONFIG_A")
        root.setText(2, "Standard SPI")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([3, 4])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        # Soft Reset(self Clearing)
        root1.setText(0, "Soft Reset(self Clearing)")
        root1.setText(4, "bits:0,1:Reset")
        root2 = QTreeWidgetItem(root)
        # LSB first
        root2.setText(0, "LSB first")
        root2.setText(4, "bits:1,1:LSB shifted,0:MSB shifted")
        root3 = QTreeWidgetItem(root)
        # Address ascension
        root3.setText(0, "Address ascension")
        root3.setText(4, "bits:2,1:addresses to auto-increment,0:addresses to auto-decrement")
        root4 = QTreeWidgetItem(root)
        # Address ascension mirror
        root4.setText(0, "Address ascension mirror")
        root4.setText(4, "bits:5,1:addresses to auto-increment,0:addresses to auto-decrement")
        root5 = QTreeWidgetItem(root)
        # LSB first mirror
        root5.setText(0, "LSB first mirror")
        root5.setText(4, "bits:6,1:Least significant bit (LSB),0:Most significant bit (MSB)")
        root6 = QTreeWidgetItem(root)
        # Soft reset mirror(self clearing)
        root6.setText(0, "Soft reset mirror(self clearing)")
        root6.setText(4, "bits:7,1:Reset the SPI and registers (self clearing),0:do nothing")
        root.addChild(root1)
        root.addChild(root2)
        root.addChild(root3)
        root.addChild(root4)
        root.addChild(root5)
        root.addChild(root6)

    def spi_config_b(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0001")
        root.setText(1, "SPI_CONFIG_B")
        root.setText(2, "Standard SPI")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([0, 2, 3, 4, 5, 6])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "Datapath soft reset(self clearing)")
        root1.setText(4, "bits:1,1:Datapath soft reset (self clearing)")
        root2 = QTreeWidgetItem(root)
        root2.setText(0, "single instruction")
        root.addChild(root1)
        root.addChild(root2)

    def chip_configuration(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0002")
        root.setText(1, "chip_config")
        root.setText(2, "CLK/SYSREF/Pin Control Regusters")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([2, 3, 4, 5, 6, 7])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "Channel power mode")
        root1.setText(4, "bits:[1:0]")
        root.addChild(root1)

    def device_index(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0008")
        root.setText(1, "DEVICE_INDEX")
        root.setText(2, "Standard SPI")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([2, 3, 4, 5, 6, 7])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "Channel A/C")
        root1.setText(4, "bits:0,1:receives")
        root2 = QTreeWidgetItem(root)
        root2.setText(0, "Channel B/D")
        root2.setText(4, "bits:1,1:receives")
        root.addChild(root1)
        root.addChild(root2)

    def transfer(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "000F")
        root.setText(1, "Transfer")
        root.setText(2, "Standard SPI")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([1, 2, 3, 4, 5, 6, 7])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "chip_transfer")
        root1.setText(4, "Bits:0,1:synchronize 0:do nothing")
        root.addChild(root1)

    def chip_pin_control_1(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0040")
        root.setText(1, "Chip Pin Control 1")
        root.setText(2, "CLK/SYSREF/Pin Control Regusters")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "chip_fd_a_pin_func")
        root1.setText(4, "bits:[2:0],Fast Detect A/GPIO A0 pin functionality")
        root2 = QTreeWidgetItem(root)
        root2.setText(0, "chip_fd_b_pin_func")
        root2.setText(4, "bits:[5:3],Chip FD_B/GPIO_B0 pin functionality")
        root3 = QTreeWidgetItem(root)
        root3.setText(0, "chip_pdn_pin_func")
        root3.setText(4, "bits:[7:6],Global chip PDWN pin functionality")
        root.addChild(root1)
        root.addChild(root2)
        root.addChild(root3)

    def chip_pin_control_2(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0041")
        root.setText(1, "Chip Pin Control 2")
        root.setText(2, "CLK/SYSREF/Pin Control Regusters")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "chip_fd_a_pin_func2")
        root1.setText(4, "bits:[3:0],Chip FD_A/GPIO_A0 pin secondary functionality")
        root2 = QTreeWidgetItem(root)
        root2.setText(0, "chip_fd_b_pin_func2")
        root2.setText(4, "bits:[7:4],Chip FD_B/GPIO_B0 pin secondary functionality")
        root.addChild(root1)
        root.addChild(root2)

    def chip_pin_control_3(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0042")
        root.setText(1, "Chip Pin Control 3")
        root.setText(2, "CLK/SYSREF/Pin Control Regusters")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "chip_gpio_a1_pin_func")
        root1.setText(4, "bits:[3:0],Chip GPIO_B1 pin functionality")
        root2 = QTreeWidgetItem(root)
        root2.setText(0, "chip_gpio_b1_pin_func")
        root2.setText(4, "bits:[7:4],hip GPIO_B1 pin functionality")
        root.addChild(root1)
        root.addChild(root2)

    def clock_divider_control(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0108")
        root.setText(1, "CLOCK_DIVIDER_CONTROL")
        root.setText(2, "CLK/SYSREF/Pin Control Regusters")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([3, 4, 5, 6, 7])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "Clock Divider")
        root1.setText(4, "bits:[2:0],input clock divider(CLK± pins)")
        root.addChild(root1)

    def clkdiv_phase(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0109")
        root.setText(1, "CLKDIV_PHASE")
        root.setText(2, "CLK/SYSREF/Pin Control Regusters")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([4, 5, 6, 7])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "Clock divider phase offset")
        root1.setText(4, "bits:[3:0],Clock divider phase offset")
        root.addChild(root1)

    def clock_driver_and_sysref_control(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "010A")
        root.setText(1, "Clock Divider and SYSREF Control")
        root.setText(2, "CLK/SYSREF/Pin Control Regusters")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([4, 5, 6])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "Clock divider positive skew window")
        root1.setText(4, "bits:[1:0]")
        root2 = QTreeWidgetItem(root)
        root2.setText(0, "Clock divider positive skew window")
        root2.setText(4, "bits:[3:2]")
        root3 = QTreeWidgetItem(root)
        root3.setText(0, "Clock divider auto phase adjust enable")
        root3.setText(4, "bits:[7]")
        root.addChild(root1)
        root.addChild(root2)
        root.addChild(root3)

    def clock_delay_control(self):
        root = QTreeWidgetItem(self.func_descibe)
        root.setText(0, "0110")
        root.setText(1, "ClOCK_DELAY_CONTROL")
        root.setText(2, "CLK/SYSREF/Pin Control Regusters")
        create_data_1 = Create_data()
        self.func_descibe.setItemWidget(root, 3, create_data_1.line)
        create_data_1.setVisable([3, 4, 5, 6, 7])
        self.func_descibe.setItemWidget(root, 4, create_data_1.groupbox_init(self))
        root1 = QTreeWidgetItem(root)
        root1.setText(0, "Clock delay mode select")
        root1.setText(4, "bits:[2:0]")
        root.addChild(root1)

    def setTreeWidget(self):
        # 标题栏宽度均分
        self.func_descibe.header().setSectionResizeMode(QHeaderView.Stretch)
        with open('qss/styleSheet.qss', 'r') as file:
            self.func_descibe.setStyleSheet(file.read())

    def print_where_is(self, item: QTreeWidgetItem, column: int):
        print(column, item.text(column))

    def traverse(self):
        """遍历节点"""
        n = self.func_descibe.topLevelItemCount()  # 获取根节点数量
        for i in range(0, n):
            item = self.func_descibe.topLevelItem(i)  # 循环获取根节点
            text = item.text(0)  # 根节点文字信息（默认一列）
            print(text)

            count = item.childCount()  # 获取当前根节点的子节点数量
            if count != 0:
                for j in range(0, count):
                    string = item.child(j).text(0)  # 子节点的文字信息
                    print(string)
