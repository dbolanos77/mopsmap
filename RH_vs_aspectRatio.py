# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:01:53 2019

@author: Daniela Bolaños
"create a relatioship betwenn relative humedity and aspect ratio of a hygroscopic particle"""

import numpy as np
import matplotlib.pyplot as plt

#seleccione 1, 2 o 3: 1-relacion de aspecto decae linealmente con la humedad; 2- decae cuadráticamente; 3: decae con otro ajuste
case = 1

#defina parámetros de entrada
RH_stop = 50 #74valor de HR a partir del cual la partícula comienza a cambiar su forma debido a la humedad
RH_max= 77  #valor de RH en el cual la partícula es una esfera
xv= list(range(0,100,10))
xv = np.asarray(xv)
b=1.2     #relación de aspecto (aspect ratio) de la partícula seca.
y1=b
y3=1

# Caso 1: epsilon' (aspect ratio) es constante y luego decae linealmente
if case == 1:
    m = (1-b)/(RH_max-RH_stop) 
    b_nuevo=b-(m*RH_stop)
    y2=(m*xv)+b_nuevo
    y=y1*((xv>=0)&(xv<=RH_stop))+y2*((xv>RH_stop)&(xv<=RH_max))+y3*(xv>RH_max); 
    plt.plot(xv, y, 'b-')
    plt.ylabel('aspect ratio')
    plt.xlabel('Relative Humidity %')
    plt.show()
#Caso 2: epsilon' es constante y luego decae cuadráticamente
elif case==2:
    x = np.array([RH_max, RH_stop, 2*RH_stop-RH_max])
    y = np.array([1, b, 1])
    A, B, C = np.polyfit(x,y,2)
    y2 = A*(xv**2)+B*(xv)+C
    y = y1*((xv>=0)&(xv<=RH_stop))+y2*((xv>RH_stop)&(xv<=RH_max))+y3*(xv>RH_max); 
    plt.plot(xv, y, 'b-')
    plt.ylabel('aspect ratio')
    plt.xlabel('Relative Humidity %')
    plt.show()
#Caso 3: epsilon' es constante y luego decae con ajuste polinomial. Para este caso ajuste los 3 puntos que desea ajustar y el grado del polinomio que desea
else:
    x = np.array([RH_stop, RH_max, 99])
    y = np.array([b, 1, 1])
    A, B, C= np.polyfit(x,y,2)
    y2 = A*(xv**2)+B*(xv)+C
    y = y1*((xv>=0)&(xv<=RH_stop))+y2*((xv>RH_stop)&(xv<=RH_max))+y3*(xv>RH_max); 
    plt.plot(xv, y, 'b-')
    plt.ylabel('aspect ratio')
    plt.xlabel('Relative Humidity %')
    plt.show()
#escribir y en el template de bash