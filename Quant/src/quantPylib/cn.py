#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 07:37:38 2020

@author: davidarchilapena
"""

import eel

import numpy as np
import math
from matplotlib import pyplot as plt
from scipy import integrate
from mpl_toolkits import mplot3d

import decimal
decimal.getcontext().prec = 100


eel.init('src')

e= math.e
pi = math.pi
h= 6.62607015*(10**-34)
c= 299792458
kb= 1.381*10**(-23)

M= 2.898*10**(-3)

@eel.expose
def cn1(T):

    print(T)
    T=float(T)
    
    lmax= M/T
    
    def graf1(l):
        d = (8*pi*h*c)/(l**5*(e**(h*c/(l*kb*T)-1)))
        return d
    
    nm= 10**-9
    
    vec_f = np.vectorize(graf1)
    l= np.arange(100*nm,20000*nm,10*nm)
    ro= vec_f(l)
    plt.close('all')
    plt.clf()
    plt.plot(l,ro)
    plt.title('T={}'.format(T))
    plt.ylabel(r'$ \rho (\lambda) $')
    plt.xlabel(r'$\lambda (m)$')
    plt.annotate(r'Máximo $\lambda_Tmax =${}'.format(lmax), xy = (lmax, graf1(lmax)), xycoords = 'data', xytext = (lmax+2000*nm, graf1(lmax)), textcoords = 'data', arrowprops = dict(arrowstyle = "->"))
    plt.savefig("src/imgpython/cn1Plot.png", dpi=300)

@eel.expose
def cn2(lmax,f):

    lmax=float(lmax)
    f= float(lmax)
    
    if lmax=='':
        lmax= c/f
    
    T= M/lmax
    
    def graf1(l):
        d = (8*pi*h*c)/(l**5*(e**(h*c/(l*kb*T)-1)))
        return d
    
    nm= 10**-9
    
    vec_f = np.vectorize(graf1)
    l= np.arange(100*nm,20000*nm,10*nm)
    ro= vec_f(l)
    plt.close('all')
    plt.clf()
    plt.plot(l,ro)
    plt.title('T={}'.format(T))
    plt.ylabel(r'$ \rho (\lambda) $')
    plt.xlabel(r'$\lambda (m)$')
    plt.annotate(r'Máximo $\lambda_Tmax =${}'.format(lmax), xy = (lmax, graf1(lmax)), xycoords = 'data', xytext = (lmax+2000*nm, graf1(lmax)), textcoords = 'data', arrowprops = dict(arrowstyle = "->"))
    plt.savefig("src/imgpython/cn2Plot.png", dpi=300)

eel.start('cn.html', port=8030)

