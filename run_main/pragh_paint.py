#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/07/01 17:37
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : pragh_paint.py
Software: PyCharm
'''


class config_info:
    def __init__(self):
        self.sample_rate = 3e9
        self.smpBitsMode = 256
        self.sectNum = 16
        self.sectBits = 32
        self.wordBits = 8
        self.memoryVol = 65536


class param_info:
    def __init__(self):
        self.sigbw = 100e6
        self.dpdbw = 300e6
        self.sideband = 3000
        self.sideband_sig = 10e6
        self.fullscale = 1200
        self.Rl = 100
        self.num_interleave = 4
        self.num_HD = 5
        self.num_IMD = 5
        self.window = 'hann'
        self.nyquitst_zone = 2
        self.dacOSR = 1
        self.plot_range = 0
        self.dbc_th_HD = -20
        self.dbc_th_IMD = -20
        self.dbc_th_IL = -20
        self.dbc_th_SFDR = -20
        self.ENOB_include_HD = 0
        self.plot_option = 1
        self.figure_overwrite = 0
        self.imd_mode = 0
        self.refclk_ratio = 1
        self.sig_angle = 0
        self.dc_1f_noise_cancel = 20e6



config = config_info()
param = param_info()
config_transfer = {'smpBitsMode': float(config.smpBitsMode), 'sectNum': float(config.sectNum),
                   'sectBits': float(config.sectBits),
                   'wordBits': float(config.wordBits), 'memoryVol': float(config.memoryVol)}
param_transfer = {'sigbw': float(param.sigbw), 'dpdbw': float(param.dpdbw),
                  'sideband': float(param.sideband),
                  'sideband_sig': float(param.sideband_sig), 'fullscale': float(param.fullscale),
                  'Rl': float(param.Rl),
                  'num_interleave': float(param.num_interleave), 'num_HD': float(param.num_HD),
                  'num_IMD': float(param.num_IMD), 'window': param.window,
                  'nyquitst_zone': float(param.nyquitst_zone),
                  'dacOSR': float(param.dacOSR),
                  'plot_range': float(param.plot_range), 'dbc_th_HD': float(param.dbc_th_HD),
                  'dbc_th_IMD': float(param.dbc_th_IMD),
                  'dbc_th_IL': float(param.dbc_th_IL),
                  'dbc_th_SFDR': float(param.dbc_th_SFDR),
                  'ENOB_include_HD': float(param.ENOB_include_HD),
                  'plot_option': float(param.plot_option),
                  'figure_overwrite': float(param.figure_overwrite), 'imd_mode': float(param.imd_mode),
                  'refclk_ratio': float(param.refclk_ratio),
                  'sig_angle': float(param.sig_angle),
                  'dc_1f_noise_cancel': float(param.dc_1f_noise_cancel)}