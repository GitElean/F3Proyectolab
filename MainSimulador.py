# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:45:23 2021

@author: Elean Rivas 19062
         Mirka Monzon 18139
         Cristopher Barrios 18207
"""

import tkinter as tk
from tkinter import PhotoImage, font
import matplotlib as plt
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
a = tk.Entry(window) .grid(row=1, column=2)


#Voltaje de de placas de deflexión verticales
tk.Label(window, text="Deflexion vertical", bg="black", fg="white", font="none 12 bold") .grid(row=2, column=0)
b = tk.Entry(window) .grid(row=2, column=2)#para y

#Voltaje de placas de deflexión horizontales
tk.Label(window, text="Deflexion horizontal", bg="black", fg="white", font="none 12 bold") .grid(row=3, column=0)
c = tk.Entry(window) .grid(row=3, column=2) #para x

#Boton de modo cambia las señales (positivas a negativas)

#Control de señal sinosuidal
tk.Label(window, text="Señal Sinuosoidal", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0)
"""a = tk.Entry(window) .grid(row=1, column=2)
a = tk.Entry(window) .grid(row=1, column=2)"""

#Frecuencia de la señal W
tk.Label(window, text="Frecuencia", bg="black", fg="white", font="none 12 bold") .grid(row=5, column=0)
w = tk.Entry(window) .grid(row=5, column=2)

#Fase de la señal
tk.Label(window, text="Fase", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0)
phi = tk.Entry(window) .grid(row=6, column=2)

#Tiempo de latencia
tk.Label(window, text="Tiempo de latencia", bg="black", fg="white", font="none 12 bold") .grid(row=7, column=0)
f = tk.Entry(window) .grid(row=7, column=2)

#grafica eje x
plots.xaxisplot(w,dist, a, phi, c)
#grafica eje y
plots.xaxisplot(w,dist, a, phi, b)
#grafica sinusoidal


window.mainloop()
#Ecuaciones 
#La intensidad del campo ( E ), la distancia sobre la que actuó ( d ) y el ángulo ( θ ) son medibles, 
# y Thomson ya había calculado la velocidad del rayo ( v ). Por lo tanto, midiendo la deflexión, 
# Thomson pudo calcular la carga específica ( q / m ).

#---------------------------1
#t= d/v
#2

