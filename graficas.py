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
    y = (ay * np.sin(wy * t + phi)) * i
    return y


def makeplotx(wx,d, va, phi,ax):
    xlist = np.linespace(-10,10,num=300)
    ylist = yaxisplot(xlist, wx,d, va, phi,ax)
    mlp.plot(xlist, ylist)
    mlp.xlim(-100,100)
    mlp.ylim(-100, 100)
    mlp.title("Movimiento horizontal")
    mlp.shoow()

    
def makeplotx(wy,d, va, phi,ay):
    xlist = np.linespace(-10,10,num=300)
    ylist = yaxisplot(xlist, wy,d, va, phi,ay)
    mlp.plot(xlist, ylist)
    mlp.xlim(-100, 100)
    mlp.ylim(-100, 100)
    mlp.title("Movimiento vertical")
    mlp.shoow()

def sinuosoidalplot(wx,d, va, phi,ax, wy, ay):
    xlist = np.linespace(-10, 10, num=300)
    ylist = yaxisplot(xlist, wx, d, va, phi, ax)
    x2list = np.linespace(-10, 10, num=300)
    y2list = yaxisplot(xlist, wy, d, va, phi, ay)
    mlp.plot(xlist, ylist)
    mlp.plot(x2list, y2list)
    mlp.xlim(-100, 100)
    mlp.ylim(-100, 100)
    mlp.title("Pantalla")
    mlp.shoow()