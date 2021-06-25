#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:40:47 2021

Author: David Archila Peña
"""


"""
This program creates and compares Gaussian type basis sets for S orbtials.
"""

"""
Inputs and Outputs Description.

Inputs: A. basis set selection (2)
        B. User defined Basis Set (optional)
Outputs: Comparision graph

"""


"""
Libraries
"""

import sys 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

import matplotlib.colors as mcolors

"""
User Functions
"""

def basis(string):
    coef = list(string.split('#'))
    
    for x in coef:
        x= float(x)
        
    return coef



def SBasis(argument):
    switcher = {
        'STO-1G': 1,
        'STO-2G': 2,
        'STO-3G': 3,
        'User Defined': 0,
       
    }
    return (switcher.get(argument, "Invalid Option"))


#################################
# Gaussian Functions defintion  #
#################################

def G(Z,Ra,r): #Gaussian
    return (2*Z/np.pi)**.75*np.exp(-Z*(r-Ra)**2)


def CGF(d,a,R,r):
    
    suma=0
    for i in range(len(d)):
        
        terSig= d[i]*G(a[i],R,r)
        suma += terSig
    
    return suma



def BS_H(b1,b2,UdBS_D,UdBS_A):


    ###########
    # Inputs  #
    ###########+
        
    
    Basis1 = SBasis(b1) #[1,2,3,0]
    Basis2 = SBasis(b2) #[1,2,3,0]
    
    Basis0 = [basis(UdBS_D),basis(UdBS_A)]
    
    
    
    ####################
    # Basis Set STO-1G #
    ####################
        
    
    D_1G=[1]
    A_1G=[0.270950]
    
    ####################
    # Basis Set STO-2G #
    ####################
        
    
    D_2G=[0.678914,0.430129]
    A_2G=[0.151623,0.851819]
    
    
    ####################
    # Basis Set STO-3G #
    ####################
        
    
    D_3G=[0.444635,0.154329,0.535328]
    A_3G=[0.168856,3.42525,0.623913]
    
    
    
    
    ####################
    # 2D Graph         #
    ####################
    
    r = np.linspace(0, 5, 100)
    
    if Basis1 != 0:
        D1 = eval('D_{}G'.format(Basis1))
        A1 = eval('D_{}G'.format(Basis1))
        Lab1 = 'STO-{}G'.format(Basis1)
    else:
        D1 = Basis0[0]
        A1 = Basis0[1]
        Lab1 = 'User Defined Basis'
        
    if Basis2 != 0:
        D2 = eval('D_{}G'.format(Basis2))
        A2 = eval('D_{}G'.format(Basis2))
        Lab2 = 'STO-{}G'.format(Basis2)
    else:
        D2 = Basis0[0]
        A2 = Basis0[1]
        Lab2 = 'User Defined Basis'
    
    
    fig = plt.figure(figsize=(15,8))
    
    ax1= plt.subplot2grid((6, 16), (0, 0), colspan=8, rowspan=6)
    
    ax1.plot(r,CGF(D1,A1,0,r),c='blue',label=Lab1)
    ax1.plot(r,CGF(D2,A2,0,r),c='purple',label=Lab2)
    ax1.legend()
    ax1.set_xlabel('r')
    ax1.set_ylabel(r'$\phi_{1s} (r)$')
    ax1.set_title(r'Basis Set Comparison')
    ax2= plt.subplot2grid((6, 16), (0, 9),colspan=3, rowspan=3, projection='3d')
    
    x, y = np.linspace(-5, 5, 50), np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = CGF(D1,A1,0,X**2+Y**2)
    
    ax2.contourf(X, Y, Z,100, zdir='z', offset=0,cmap='afmhot')
    
    cmap = plt.get_cmap('viridis_r')
    norm = mcolors.Normalize(vmin=Z.min(), vmax=Z.max())
    plot = ax2.plot_surface(
        X, Y, Z, rstride=1, cstride=1, 
        facecolors=cmap(norm(Z)),
        linewidth=0, antialiased=False, alpha=0.5)
    
    ax2.set_xlabel(r'x')
    ax2.set_ylabel(r'y')
    ax2.set_zlabel(r'$\phi_{1s} (x,y)$')
    ax2.set_title(r'{}'.format(Lab1))
    
    ax3= plt.subplot2grid((6, 16), (0, 13),colspan=3, rowspan=3, projection='3d')
    
    x, y = np.linspace(-5, 5, 50), np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = CGF(D2,A2,0,X**2+Y**2)
    
    ax3.contourf(X, Y, Z,100, zdir='z', offset=0,cmap='afmhot')
    
    cmap = plt.get_cmap('viridis_r')
    norm = mcolors.Normalize(vmin=Z.min(), vmax=Z.max())
    plot = ax3.plot_surface(
        X, Y, Z, rstride=1, cstride=1, 
        facecolors=cmap(norm(Z)),
        linewidth=0, antialiased=False, alpha=0.5)
    ax3.set_xlabel(r'x')
    ax3.set_ylabel(r'y')
    ax3.set_zlabel(r'$\phi_{1s} (x,y)$')
    ax3.set_title(r'{}'.format(Lab2))
    
    
    ax4= plt.subplot2grid((6, 16), (3, 9),colspan=3, rowspan=3, projection='3d')
    
    x, y, z = np.linspace(-5, 5, 15), np.linspace(-5, 5, 15), np.linspace(-5, 5, 15)
    X, Y, Z = np.meshgrid(x, y, z)
    density = CGF(D1,A1,0,X**2+Y**2+Z**2)
    
    plot= ax4.scatter(X, Y, Z, s=density*50,c=density)
    ax4.set_xlabel(r'x')
    ax4.set_ylabel(r'y')
    ax4.set_zlabel(r'z')
    
    
    cb4= fig.colorbar(plot,orientation='horizontal',fraction=0.03, pad=0.2)
    cb4.set_label('$\phi_{1s} (x,y,z)$')
    
    ax5= plt.subplot2grid((6, 16), (3, 13),colspan=3, rowspan=3, projection='3d')
    
    x, y, z = np.linspace(-5, 5, 15), np.linspace(-5, 5, 15), np.linspace(-5, 5, 15)
    X, Y, Z = np.meshgrid(x, y, z)
    density = CGF(D2,A2,0,X**2+Y**2+Z**2)
    
    plot= ax5.scatter(X, Y, Z, s=density*50,c=density)
    ax4.set_xlabel(r'x')
    ax4.set_ylabel(r'y')
    ax4.set_zlabel(r'z')
    
    cb5= fig.colorbar(plot,orientation='horizontal',fraction=0.03, pad=0.2)
    cb5.set_label('$\phi_{1s} (x,y,z)$')
    
    fig.canvas.set_window_title('STO Radial Functions: Hydrogen Basis Set Comparison')
    
    
    plt.show()
        
    
#BS_H('STO-1G','STO-2G',"0#0","0#0")
