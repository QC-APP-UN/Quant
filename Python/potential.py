#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 18:17:10 2021

@author: johanna
"""

import matplotlib.pyplot as plt
import numpy as np

#Valores experimentales de la molécula H2

Xe = 0.741 #A
Xmin=0.3
Xmax=2.5
Dx=0.019
Der = 151.29 #De adimensional
a=1.9451


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

    
    
    
    
    
    
    
    
    
    
    
