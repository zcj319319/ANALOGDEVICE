#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/8/12 16:45
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : load_fft_panel.py
Software: PyCharm
'''
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from run_main.FFT.fft_UI import Ui_MainWindow
import matlab.engine
import matlab

from run_main.pragh_paint import config_info

engine = matlab.engine.start_matlab()  # 启动matlab


class load_fft_ui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_param()
        self.file_toolButton.clicked.connect(self.openFile)
        self.run_btn.clicked.connect(self.run_project)
        self.textEdit_2.setStyleSheet("background-color:#949494")
        with open('qss/groupbox.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def init_param(self):
        self.sample_rate_txt.setText('3e9')
        self.smpBitsMode_txt.setText('256')
        self.sectNum_txt.setText('16')
        self.sectBits_txt.setText('32')
        self.wordBits_txt.setText('8')
        self.memoryVol_txt.setText('65536')
        # self.sigbw_input.setText('100e6')
        # self.dpdbw_input.setText('300e6')
        # self.sideband_input.setText('3000')
        # self.sideband_sig_input.setText('10e6')
        # self.fullscale_input.setText('1200')
        # self.Rl_input.setText('100')
        # self.num_interleave_input.setText('4')
        # self.num_HD_input.setText('5')
        # self.num_IMD_input.setText('5')
        # self.window_input.setText('hann')
        # self.nyquitst_zone_input.setText('2')
        # self.dacOSR_input.setText('1')
        # self.plot_range_input.setText('0')
        # self.dbc_th_HD_input.setText('-20')
        # self.dbc_th_IMD_input.setText('-20')
        # self.dbc_th_IL_input.setText('-20')
        # self.dbc_th_SFDR_input.setText('-20')
        # self.ENOB_include_HD_input.setText('0')
        # self.plot_option_input.setText('1')
        self.figure_overwrite_input.setText('1')
        # self.refclk_ratio_input.setText('1')
        # self.sig_angle_input.setText('0')
        # self.dc_1f_noise_cancel_input.setText('20e6')

    def check_param(self):
        self.config_transfer = {}
        self.param_transfer = {}
        config = config_info()
        if self.sample_rate_txt.text().strip(" ") == '':
            self.config_transfer['sample_rate'] = float(config.sample_rate)
        else:
            self.config_transfer['sample_rate'] = float(self.sample_rate_txt.text().strip(" "))
        if self.smpBitsMode_txt.text().strip(" ") == '':
            self.config_transfer['smpBitsMode'] = float(config.smpBitsMode)
        else:
            self.config_transfer['smpBitsMode'] = float(self.smpBitsMode_txt.text().strip(" "))
        if self.sectNum_txt.text().strip(" ") == '':
            self.config_transfer['sectNum'] = float(config.sectNum)
        else:
            self.config_transfer['sectNum'] = float(self.sectNum_txt.text().strip(" "))
        if self.sectBits_txt.text().strip(" ") == '':
            self.config_transfer['sectBits'] = float(config.sectBits)
        else:
            self.config_transfer['sectBits'] = float(self.sectBits_txt.text().strip(" "))
        if self.wordBits_txt.text().strip(" ") == '':
            self.config_transfer['wordBits'] = float(config.wordBits)
        else:
            self.config_transfer['wordBits'] = float(self.wordBits_txt.text().strip(" "))
        if self.memoryVol_txt.text().strip(" ") == '':
            self.config_transfer['memoryVol'] = float(config.memoryVol)
        else:
            self.config_transfer['memoryVol'] = float(self.memoryVol_txt.text().strip(" "))

        if self.sigbw_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['sigbw'] = float(self.sigbw_input.text().strip(" "))
        if self.dpdbw_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['dpdbw'] = float(self.dpdbw_input.text().strip(" "))
        if self.sideband_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['sideband'] = float(self.sideband_input.text().strip(" "))
        if self.sideband_sig_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['sideband_sig'] = float(self.sideband_sig_input.text().strip(" "))
        if self.fullscale_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['fullscale'] = float(self.fullscale_input.text().strip(" "))
        if self.Rl_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['Rl'] = float(self.Rl_input.text().strip(" "))
        if self.num_interleave_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['num_interleave'] = float(self.num_interleave_input.text().strip(" "))
        if self.num_HD_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['num_HD'] = float(self.num_HD_input.text().strip(" "))
        if self.num_IMD_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['num_IMD'] = float(self.num_IMD_input.text().strip(" "))
        if self.window_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['window'] = self.window_input.text().strip(" ")
        if self.nyquitst_zone_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['nyquitst_zone'] = float(self.nyquitst_zone_input.text().strip(" "))
        if self.dacOSR_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['dacOSR'] = float(self.dacOSR_input.text().strip(" "))
        if self.plot_range_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['plot_range'] = float(self.plot_range_input.text().strip(" "))
        if self.dbc_th_HD_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['dbc_th_HD'] = float(self.dbc_th_HD_input.text().strip(" "))
        if self.dbc_th_IMD_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['dbc_th_IMD'] = float(self.dbc_th_IMD_input.text().strip(" "))
        if self.dbc_th_IL_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['dbc_th_IL'] = float(self.dbc_th_IL_input.text().strip(" "))
        if self.dbc_th_SFDR_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['dbc_th_SFDR'] = float(self.dbc_th_SFDR_input.text().strip(" "))
        if self.ENOB_include_HD_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['ENOB_include_HD'] = float(self.ENOB_include_HD_input.text().strip(" "))
        if self.plot_option_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['plot_option'] = float(self.plot_option_input.text().strip(" "))
        if self.figure_overwrite_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['figure_overwrite'] = float(self.figure_overwrite_input.text().strip(" "))
        self.param_transfer['imd_mode'] = float(self.imd_mode_cmbox.currentText())
        if self.refclk_ratio_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['refclk_ratio'] = float(self.refclk_ratio_input.text().strip(" "))
        if self.sig_angle_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['sig_angle'] = float(self.sig_angle_input.text().strip(" "))
        if self.dc_1f_noise_cancel_input.text().strip(" ") == '':
            pass
        else:
            self.param_transfer['dc_1f_noise_cancel'] = float(self.dc_1f_noise_cancel_input.text().strip(" "))

    def openFile(self):
        curPath = QDir.currentPath()
        file_path, f_type = QFileDialog.getOpenFileName(self, 'choose a File', curPath,
                                                        'All Files (*);;Text Files (*.txt)')
        if len(file_path) != 0:
            self.file_path_lineinput.setText(file_path)
        else:
            return

    def run_project(self):
        if len(self.file_path_lineinput.text()) == 0:
            QMessageBox.information(self, 'warning', 'please input file!')
        else:
            self.check_param()
            engine.memory_data_analyze(self.file_path_lineinput.text(), self.config_transfer,
                                       self.param_transfer)
