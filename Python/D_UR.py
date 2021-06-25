#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:35:32 2021

@author: Valeria Cortéz
Contributor 1: Johanna Aldana
Contributor 2: David Archila Peña

"""
import matplotlib.pyplot as plt
import numpy as np

def UR(xe,xmin,xmax,dx,der,a):
    
    #Valores experimentales de la molécula H2

    Xe = float(xe)
    Xmin= float(xmin)
    Xmax= float(xmax)
    Dx= float(dx)
    Der = float(der) #De adimensional
    a= float(a)
    
    
    #Curva de potencial de Morse para H2
        
    
    X=np.arange(Xmin, Xmax+Dx,Dx)
    n=len(X)
    def Morse(X):
        return (Der*(np.exp(-2*a*(X-Xe))-2*np.exp(-a*(X-Xe))))
    diff=np.zeros((n,n))
    x=np.linspace(Xmin, Xmax, n)
    plt.plot(X,Morse(X), "ko-")
    plt.ylabel("U(R)", fontsize=14)
    plt.xlabel("R", fontsize=14)
    plt.show()
    
    
