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


def xaxisplot(i, wx,d, va, phi,ax):
    t = d/va
    x = (ax * np.cos(wx * t + phi))*i
    return x


def yaxisplot(i, wy, d, va, phi, ay):
    t = d / va
    y = (ay * np.cos(wy * t + phi)) * i
    return y


def makeplotx(wx,d, va, phi,ax):
    xlist = np.linespace(-10,10,num=300)
    ylist = yaxisplot(xlist, wx,d, va, phi,ax)

    


