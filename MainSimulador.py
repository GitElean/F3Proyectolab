# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:45:23 2021

@author: Elean Rivas 19062
         Mirka Monzon 18139
         Cristopher Barrios 18207
"""

import tkinter as tk
from tkinter import PhotoImage, font
import matplotlib.pyplot as plt
from numpy import double
import numpy as np
import graficas as plots

window = tk.Tk()
window.title("Simulador de tubos catódicos")
window.config(background="black")
window.geometry("800x600")

#Area de las placas de deflexion
area = 0.006 #metros

#Distancia de separacion entre las placas
dist = 0.005 #metros Dato d, de las funcioones para x e y #✓

#Distancia desde las placas de deflexión verticales a las horizontales
verHor = 0.003 #metros

photo1= PhotoImage(file="TuboCatodico.png")
tk.Label(window, image=photo1, bg="gray"). grid(row=0, column=4)

"""input"""
#Voltaje de aceleración de los electrones
tk.Label(window, text="Amplitud", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0)
a = double(tk.Entry(window) .grid(row=1, column=2))


#Voltaje de de placas de deflexión verticales
tk.Label(window, text="Deflexion vertical", bg="black", fg="white", font="none 12 bold") .grid(row=2, column=0)
b = double(tk.Entry(window) .grid(row=2, column=2))#para y

#Voltaje de placas de deflexión horizontales
tk.Label(window, text="Deflexion horizontal", bg="black", fg="white", font="none 12 bold") .grid(row=3, column=0)
c = double(tk.Entry(window) .grid(row=3, column=2)) #para x

#Boton de modo cambia las señales (positivas a negativas)

#Control de señal sinosuidal
tk.Label(window, text="Señal Sinuosoidal", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0)
"""a = tk.Entry(window) .grid(row=1, column=2)
a = tk.Entry(window) .grid(row=1, column=2)"""

#Frecuencia de la señal W
tk.Label(window, text="Frecuencia", bg="black", fg="white", font="none 12 bold") .grid(row=5, column=0)
w = double(tk.Entry(window) .grid(row=5, column=2))

#Fase de la señal
tk.Label(window, text="Fase", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0)
phi = double(tk.Entry(window) .grid(row=6, column=2))

#Tiempo de latencia
tk.Label(window, text="Tiempo de latencia", bg="black", fg="white", font="none 12 bold") .grid(row=7, column=0)
f = double(tk.Entry(window) .grid(row=7, column=2))





xlist = np.linspace(-10,10,num=1000)
ylist = plots.xaxisplot(xlist,w,dist,a,phi,b)
y1list = plots.yaxisplot(xlist,w,dist,a,phi,c)

def yg(x,y):
    plt.figure(num=0,dpi=120)
    plt.plot(x,y,label="vertical(y)")
    
def xg(x,y):
    plt.figure(num=0,dpi=120)
    plt.plot(x,y,label="vertical(x)")
    
def sg(x,y):
    plt.figure(num=0,dpi=120)
    plt.plot(x,y,label="Pantalla")
    
    
yg(xlist,y1list)
xg(xlist,ylist)
sg(ylist,y1list)


window.mainloop()
#Ecuaciones 
#La intensidad del campo ( E ), la distancia sobre la que actuó ( d ) y el ángulo ( θ ) son medibles, 
# y Thomson ya había calculado la velocidad del rayo ( v ). Por lo tanto, midiendo la deflexión, 
# Thomson pudo calcular la carga específica ( q / m ).

#---------------------------1
#t= d/v
#2

