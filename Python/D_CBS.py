#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:42:23 2021

Author: Scott W Harden 
Contributor: David Archila Peña
"""

# Code originaly made for expoential decay, adapted to work for
# CBS limit basis set extrapolation. 

import numpy as np
import scipy
import matplotlib.pyplot as plt


# x= np.linspace(0,6,50)
# xs=np.array([2,3,4,5,6])
# ys= np.array([-128.488775551593,-128.531861636113,\
#    -128.543469659171,-128.546770130004,\
#    -128.547061101241])
    

def monoExp(x, m, t, b):
    
    return m*np.exp(-t * x) + b    


def CBS(E2,E3,E4,E5,E6):
    
    E2=float(E2)
    E3=float(E3)
    E4=float(E4)
    E5=float(E5)
    E6=float(E6)
    
    x= np.linspace(0,6,50)
    xs=np.array([2,3,4,5,6])
    ys= np.array([E2,E3,E4,E5,E6])
    
    # perform the fit
    p0 = (10, 1, 20) # start with values near those we expect
    params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0)
    m, t, b = params
    
    
    # determine quality of the fit
    squaredDiffs = np.square(ys - monoExp(xs, m, t, b))
    squaredDiffsFromMean = np.square(ys - np.mean(ys))
    rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
    print(f"R² = {rSquared}")
    
    
    yb= np.array([b for i in range(len(x))])
    
    # plot the results
    plt.plot(xs, ys, 'k*', label="Data")
    plt.plot(x, monoExp(x, m, t, b), '--', label="Fitted")
    plt.plot(x,yb, 'b--',linewidth=0.5,label= "HF-CBS limit")
    plt.title(r"Fitted Exponential Curve to $E_R(L)=E_R(\infty)+Ae^{-BL}$")
    plt.legend()
    plt.savefig(fname='Dot',dpi=500)
    
    # inspect the parameters
    print(f"Y = {m} * e^(-{t} * x) + {b}")
    
    
#CBS(-128.488775551593,-128.531861636113,\
    #-128.543469659171,-128.546770130004,\
    #-128.547061101241)