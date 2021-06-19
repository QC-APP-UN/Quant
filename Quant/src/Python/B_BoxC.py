#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:17:46 2020

@author: davidarchilapena
"""

import eel

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math

eel.init('src')

# psi = (2/L1)**(1/2)*(np.sin(n1*pi*x)/L1)

e= math.e
pi = math.pi

@eel.expose
def anonda(n1,n2,c1,c2):
    
    n1= float(n1)
    n2= float(n2)
    c1= float(c1)
    c2= float(c2)

    plt.close('all')
    plt.clf()

    cn1= c1/(c1+c2)
    cn2= c2/(c1+c2)
    
    N2= 1/(c1**2+c2**2)
    
    
    L=1.0 # De referencia
    
    def p1(x):
        y= cn1*((2/L)**(0.5)*np.sin(pi*x*n1/L))
        return y
    
    def p2(x):
        y= cn2*((2/L)**(0.5)*np.sin(pi*x*n2/L))
        return y
    
    psi1 = np.vectorize(p1)
    psi2 = np.vectorize(p2)
    
    
    E1= (n1*pi*2)**2/(8) 
    E2= (n2*pi*2)**2/(8)
    x = np.linspace(0, 1, 1000)
    y = N2*(cn1*((psi1(x))**2) + cn2*((psi2(x))**2) + np.cos((E2-E1)*(2*pi)*0)*psi1(x)*psi2(x))
    fig = plt.figure()
    line, = plt.plot(x, y, lw=3)
    plt.xlabel('x')
    plt.ylabel(r'$|\psi(x)|^2$')
    plt.title(r'$|\psi_r(x,t)|^2$')
    
    def init():
        line.set_data([], [])
        return line,
    def animate(i):
        x = np.linspace(0, 1, 1000)
        E1= (n1*pi*2)**2/(8) 
        E2= (n2*pi*2)**2/(8)
        T= 1/(E2-E1)
        t= i*T/8
        y = N2*(cn1*((psi1(x))**2) + cn2*((psi2(x))**2) + np.cos((E2-E1)*(2*pi)*t)*psi1(x)*psi2(x))
        line.set_data(x, y)
        return line,
    
    anim = FuncAnimation(fig, animate, init_func=init,
                                   frames=200, interval=1, blit=True)
    
    anim.save('src/imgpython/anondaPlot.gif', writer='imagemagick', dpi=300)
    
    
eel.start('anonda.html', port=8840)





