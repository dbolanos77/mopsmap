# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:41:45 2019

@author: Daniela Bolaños
""log normal distribution"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi

r_min = 0.005
r_max = 20
n0 = 2000000   #particle number density g/m³
r_mod = 0.471      #modal radius
sigma = 2.51  # width of size distribution, σ > 1
r = np.linspace(r_min,r_max,50)
n = (1/np.sqrt(2*pi))*(n0/np.log(sigma))*(1/r)*np.exp((-1/2)*((np.log(r)-np.log(r_mod))/np.log(sigma))**2)
plt.plot(r,n)
plt.ylabel('particle concentration')
plt.xlabel('particle size (um)')
plt.show()