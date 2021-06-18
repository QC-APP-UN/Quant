#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:51:27 2021

@author: rafa
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.special import lpmv
from scipy.special import sph_harm
import matplotlib.colors as mcolors


pi=np.pi
cos=np.cos
sin=np.sin
sqrt=np.sqrt
theta=np.linspace(0,pi,100)
phi=np.linspace(0,2*pi,100)

def carte(r,theta,phi):
    x = r* sin(theta)* cos(phi)
    y = r* sin(theta)* sin(phi)
    z = r* cos(theta)
    return x,y,z

def Polar(l,m,x):
    PAL=lpmv(m,l,cos(x))
    plt.polar(phi,abs(PAL))
    plt.title('Visualizing the Spherical Harmonics $Y_m^l(θ)$'+' l= '+ str(l)+ '; m= '+str(m))
    plt.show()
    
def Spher(l,m,x,y):
    x, y = np.meshgrid(x, y)
    Y=sph_harm(abs(m), l, x, y)
    if m<0:
        Y=((-1)**m)*sqrt(2)*Y.img
    elif m>0:
        Y=((-1)**m)*sqrt(2)*Y.real
    else:
        Y=sph_harm(0,l,x,y)
    ()
    x,y,z=carte(abs(Y),x, y)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x,y,z,rstride=2,cstride=2)
    plt.title(r'$Y_m^l(θ,φ)$'+' l= '+ str(l)+ '; m= '+str(m))
    cmap = plt.get_cmap('viridis_r')
    norm = mcolors.Normalize(vmin=z.min(), vmax=z.max())
    plot = ax.plot_surface(x,y,z, rstride=1, cstride=1,facecolors=cmap(norm(z)),linewidth=0, antialiased=False,alpha=0.5)
                    
