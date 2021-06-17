#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:38:31 2021

@author: rafa
"""

import numpy as np
import math
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import animation
import os
import sys


e= math.e
pi = math.pi

def fCaja(d,n1,n2,n3,L1,L2,L3,M):
    d=float(d)
    n1=float(n1)
    n2=float(n2)
    n3=float(n3)
    L1=float(L1)
    L2=float(L2)
    L3=float(L3)
    M=float(M)
    
    if d==1:
        
        def psi(x):
            psi = (2/L1)**(1/2)*(np.sin(n1*pi*x)/L1)
            return psi
    
        vec_psi = np.vectorize(psi)
        x= np.arange(0,L1,.001)
        y= vec_psi(x)
        plt.xlabel('x')
        plt.ylabel(r'$\mathrm{\psi}$')
        plt.plot(x,y)
        plt.show()
        
        
    if d==2:
        
        def psi(x,y):
            psi = (2/L1)**(1/2)*(np.sin(n1*pi*x)/L1)*(2/L2)**(1/2)*(np.sin(n2*pi*y)/L2)
            return psi
        
        x = np.linspace(0, L1, 30)
        y = np.linspace(0, L2, 30)

        X, Y = np.meshgrid(x, y)
        Z = psi(X, Y)
        
        plt.close('all')
        plt.clf()
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.contour3D(X, Y, Z, 50, cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel(r'$\mathrm{\psi}$');
        ax.view_init(40, 35)
        ax.set_title(r'$\mathrm{\psi(x,y)}$');
        plt.show()

    if d==3:
         
        def psiZ(i,z,line):
            z= (2/L1)**(1/2)*(np.sin(n1*pi*x)/L1)*(2/L2)**(1/2)*(np.sin(n2*pi*y)/L2)*(2/L3)**(1/2)*(np.sin(n3*pi*(0+0.01*i))/L3)
            ax.clear()
            ax.set_xlim3d([0.0, L1])
            ax.set_xlabel('X')
            
            ax.set_ylim3d([0.0, L2])
            ax.set_ylabel('Y')
            
            ax.set_zlim3d([0.0, L3])
            ax.set_zlabel(r'$\mathrm{\psi(x,y)}$')
            line= ax.contour3D(x, y, z, 50, cmap='viridis', edgecolor='none')
            return line

        plt.close('all')
        plt.clf()
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
            
        x = np.linspace(0,L1,100)
        y = np.linspace(0,L2,100)
        x,y = np.meshgrid(x,y)
        z = (2/L1)**(1/2)*(np.sin(n1*pi*x)/L1)*(2/L2)**(1/2)*(np.sin(n2*pi*y)/L2)
        line = ax.contour3D(x, y, z, 50, cmap='viridis', edgecolor='none')

        ani = animation.FuncAnimation(fig, psiZ, fargs=(z, line), interval=50, blit=False)
            
        ani.save('src/imgpython/cajaPlot.gif', dpi=300)
        
fCaja(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]) #d,n1,n2,n3,L1,L2,L3,M

#seems to work fine, times reported in data i have
#check again when plots are defined for the project 
#:)
