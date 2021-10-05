# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:17:43 2021

@author: Elean Rivas 19062
         Mirka Monzon 18139
         Cristopher Barrios 18207

gráficas
"""

import matplotlib as mlp
import numpy as np


def xaxisplot(wx,d, va, phi,ax):
    t = d/va
    return x = ax * np.cos(wx * t + phi)


def yaxisplot(wy, d, va, phi, ay):
    t = d / va
    return y = ay * np.cos(wy * t + phi)


def makeplotx(wx,d, va, phi,ax)
    xlist = np.linespace(-10,10,num=300)


