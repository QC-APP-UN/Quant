#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROYECTO QUÍMICA CUÁNTICA
"""

import eel

eel.init('src')


import math
from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate
import os

e= math.e
pi = math.pi

@eel.expose
def Cnormalize():
    os.remove("src/imgpython/normPlot.png")

@eel.expose
def Gnormalize(f):
    sol= integrate.quad(lambda x: eval(f),-np.inf,np.inf)
    
    fun=f
    def f(x):
        f = eval(fun)/sol[0]
        return f

    vec_f = np.vectorize(f)
    x= np.arange(-10,10,.1)
    y= vec_f(x)
    plt.close('all')
    plt.clf()
    plt.plot(x,y)
    plot=plt.savefig("src/imgpython/normPlot.png")
    return plot


@eel.expose
def Nnormalize(f):
    sol= integrate.quad(lambda x: eval(str(f)),-np.inf,np.inf)
    StringSol= str(sol[0]) 
    print(StringSol)
    return StringSol


eel.start('norm.html', port=8070)