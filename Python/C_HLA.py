#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:02:08 2020
@author: davidarchilapena
"""

import numpy as np
import math
from matplotlib import pyplot as plt
from scipy import integrate
from mpl_toolkits import mplot3d
import sys

e= math.e
pi = math.pi

def moman(l,m):

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
        
        plt.close('all')
        plt.clf()
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
        
        plt.show()
        
def hid(n,l,m,Z):

    n=int(n)
    l=int(l)
    m=int(m)
    Z=int(Z)
    
    a= 1
    E= -(Z**2/n**2)*(1/2)#(qe**2/(8*pi*e0*a))
    #print(E)
    
    c=[1]
        
    psi=''
    for i in range(0,n-l+1):
        
        bN = (2*Z/(n*a))*(i+l+1-n)*c[i]/((i+1)*(i+2*l+2))
        c.append(bN)
            
        psi= psi + str(c[i]) + '*R**' + str(i) + '+'
     
    if psi != '':
        psi= '*('+ psi + '0' + ')'
    
    psi= 'e**(-Z*R/(n*a))*R**l'+ psi
        
    psi=psi.replace('l',str(l))
    psi=psi.replace('Z',str(Z))
    psi=psi.replace('n',str(n))
    psi=psi.replace('a',str(a))
    #print(psi)
    sol= integrate.quad(lambda R: eval(psi),0,np.inf)
    #print(sol)
    def psiHidR(R): 
        psin=eval(psi)/sol[0]
        return psin
    
    fig = plt.figure(figsize=(15,8))
    
    ax1= plt.subplot2grid((6, 16), (0, 0), colspan=8, rowspan=6)
    
    VpsiHidR = np.vectorize(psiHidR)
    R= np.arange(0,10*n,.1/n)
    y= VpsiHidR(R)
    ax1.set_xlabel('r')
    ax1.set_ylabel(r'$\Psi_R (r)$')
    ax1.set_title(r'n={} ; l= {}'.format(str(n),str(l)))
    ax1.plot(R,y)
    
    # plt.show()

    x = np.linspace(-10*n,10*n, 100)
    y = np.linspace(-10*n,10*n, 100)

    X, Y = np.meshgrid(x, y)
    Z = VpsiHidR((X**2+Y**2)**(1/2))
    

    ax2= plt.subplot2grid((6, 16), (0, 9),colspan=6, rowspan=3, projection='3d')
    
    ax2.contour3D(X, Y, Z, 50, cmap='viridis', edgecolor='none')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel(r'$\mathrm{\psi}$');
    ax2.view_init(40, 35)
    ax2.set_title(r'$\mathrm{\Psi_R(x,y)}$');
    
    
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
        
        
        ax3= plt.subplot2grid((6, 16), (3, 9),colspan=6, rowspan=3, projection='3d')
        
        plt.title(r'$Y_m^l(\theta,\phi)$'+' l= '+ str(l)+ '; m= '+str(m))
        
        
        import matplotlib.colors as mcolors
        
        cmap = plt.get_cmap('viridis_r')
        norm = mcolors.Normalize(vmin=Z.min(), vmax=Z.max())
        plot = ax3.plot_surface(
            X, Y, Z, rstride=1, cstride=1, 
            facecolors=cmap(norm(Z)),
            linewidth=0, antialiased=False, alpha=0.5)
        
        plt.show()
    
