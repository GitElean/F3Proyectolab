# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:17:43 2021

@author: Usuario

gráficas
"""

import matplotlib as mlp
import numpy as np


def xaxisplot(wx,d, va, phi,ax):
    t = d/va
    x=ax*np.cos(wx * t + phi)
    pass

def yaxisplot(wy, t, phi, ay):
    y = ay * np.cos(wy * t + phi)
    pass

def sinosuidalplot():
    pass

