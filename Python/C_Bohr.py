#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:29:05 2021

@author: rafa
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os 

t=np.linspace(0,2*np.pi,200)

def BSorbit(n,k,Z):
    if k in ['all']:
        for i in range(0,int(n)):
            N=int(n)
            B=i+1
            Z=int(Z)
            a=N**2/Z
            b=(N*B)/Z
            center=(N**2-B**2)/Z
            lim=(N**2 + 2)/Z
            x=center+a*np.cos((t))
            y=b*np.sin((t))
            plt.ylim(-lim,lim)
            plt.plot(x,y,label=('n='+ str(N)+' '+ 'm='+' '+ '±' +str(B)))
            plt.legend(loc='upper left')
            plt.title('Bohr-Sommerfeld Orbits')
        plt.show()

        
    else:
        N=int(n)
        B=abs(int(k))
        Z=int(Z)
        a=N**2/Z
        b=(N*B)/Z
        center=(N**2-B**2)
        lim=(N**2 + 2)/Z
        x=center+a*np.cos((t))
        y=b*np.sin((t))
        plt.ylim(-lim,lim)
        plt.plot(x,y,label=('n='+ str(n)+' '+ 'm='+ str(k)))
        plt.legend(loc='upper left')
        plt.show()

#BSorbit((sys.argv[1]), (sys.argv[2]), (sys.argv[3]))