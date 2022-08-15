#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/07/05 10:36
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : plot_file.py
Software: PyCharm
'''
import numpy


def f_flip(input_in, nq):
    if divmod(nq, 2)[1]:
        out = input_in
    else:
        out = numpy.flip(input_in)
    return out


def f_trans(input_in, N_fft, fs, nq):
    if divmod(nq, 2)[1]:
        out = [j/ N_fft * fs + (nq - 1) / 2 * fs for j in input_in]
    else:
        out = [nq / 2 * fs - j / N_fft * fs for j in input_in]
    return out
