#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:18:46 2021

@author: rafa
"""

import numpy as np
import math
from scipy import integrate
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import os
import time
import sys

e= math.e
pi = math.pi

#Parte real de los armónicos esféricos. 

#T es theta
#P es phi


#Función interna (no usar @eel.expose)
def fac(n):
    y= np.math.factorial(n)
    return y
def moman(l,m):

    plt.close('all')
    plt.clf()

    l=int(l)
    m=int(m)
    
    S= '((((2*l+1)/(4*pi))*(fac(l-abs(m))/fac(l+abs(m))))**1/2)'
    Sm= S.replace('m',str(m))
    Sm= Sm.replace('l',str(l))
    
    if l-abs(m)<0:
        return '|m| no puede ser mayor a l.'
        
    elif l<0:
        return 'l debe ser un número positivo y entero.'
    
    else:
        
        # w = sp.Symbol('w')
        # P= '((l/(2**l*fac(l)))*(1-w**2)**(abs(m)/2))*sp.diff((w**2-1)**l,w,l+abs(m))'
        # Pml= P.replace('l', str(l))
        # Pml= Pml.replace('m', str(m))
        
        # Pc= str(eval(Pml))
        # Pcos= Pc.replace('w','(np.cos(T))')
        
        # Y = Sm+ '*(' + Pcos + ')' #+ '*(np.cos(m*P))'
        # Yml= Y.replace('m',str(m))
        
        if (-1)**(l-abs(m))==1:
        
            c=[1]
            
            psi=''
            for i in range(0,(l-abs(m))+1):
                if (-1)**(i)==1:
                    c.append(0)
                    c.append(((i+abs(m))*(i+abs(m)+1)-l*(l+1))*c[i]/((i+1)*(i+2)))
                
                    psi= psi + str(c[i]) + '*np.cos(T)**' + str(i) + '+'
                    
            
            psi= '('+ psi + '0' + ')'
            psi= '(np.sin(T)**abs(m)*'+psi+')'
            psi= psi.replace('m',str(m))
            sol= integrate.quad(lambda T: eval(psi),0,pi)
            psi= psi+'/'+str(sol[0])
            
        
        
        if (-1)**(l-abs(m))==-1:
        
            c=[0,1]
            
            psi=''
            for i in range(1,(l-abs(m))+1):
                if (-1)**(i)==-1:
                    c.append(0)
                    c.append(((i+abs(m))*(i+abs(m)+1)-l*(l+1))*c[i]/((i+1)*(i+2)))
                
                    psi= psi + str(c[i]) + '*np.cos(T)**' + str(i) + '+'
                    
                
            psi= '('+ psi + '0' + ')'
            psi= '(np.sin(T)**abs(m)*'+psi+')'
            psi= psi.replace('m',str(m))
            sol= integrate.quad(lambda T: eval(psi),0,pi)
            psi= psi+'/'+str(sol[0])
            
            
        
        Yml= '('+psi+')' + '*np.cos(abs(m)*P)'
        Yml= Yml.replace('m',str(m))
        
        theta, phi = np.linspace(0, np.pi, 100), np.linspace(0, 2*np.pi, 100)
        T, P = np.meshgrid(theta, phi)
        R = abs(eval(Yml)) #NotSoSure
        X = R * np.sin(T) * np.cos(P)
        Y = R * np.sin(T) * np.sin(P)
        Z = R * np.cos(T)
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        plt.title(r'$Y_m^l(θ,φ)$'+' l= '+ str(l)+ '; m= '+str(m))
        
        
        import matplotlib.colors as mcolors
        
        cmap = plt.get_cmap('viridis_r')
        norm = mcolors.Normalize(vmin=Z.min(), vmax=Z.max())
        plot = ax.plot_surface(
            X, Y, Z, rstride=1, cstride=1, 
            facecolors=cmap(norm(Z)),
            linewidth=0, antialiased=False, alpha=0.5)
        
        plt.savefig('src/imgpython/momanPlot.png', dpi=300)
        
        Yml_string= Yml.replace('np.cos','cos')
        Yml_string= Yml_string.replace('T','θ')
        Yml_string= Yml_string.replace('P','φ')
        Yml_string= Yml_string.replace('np.sin','sin')
        Yml_string= Yml_string.replace('**','^')
        Yml_string= Yml_string.replace('**1','')
        Yml_string= Yml_string.replace('+0','')
        Yml_string= Yml_string.replace('+-','-')
        Yml_string= Yml_string.replace('abs({})'.format(str(m)),'[{}]'.format(str(m)))
        Yml_string= Yml_string + '^2'
    
    return Yml_string
        
inicio=time.time()   
moman(sys.argv[1],sys.argv[2])
fin=time.time()
print((inicio-fin)*1000)

#check again when plots are determined for the project
#seems fine so far 
#:/