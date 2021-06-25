#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:27:10 2020

@author: davidarchilapena
"""

"""IMPORTANTE: Necesita una guía de uso."""

import matplotlib.pyplot as plt
import numpy as np
import sys

"""
Método de Numerov.
Este programa emplea el método de numerov para un potencial dado.
"""


def numerovN2(n,R,E1,E2,xi,xf):

    plt.close('all')
    plt.clf()
    
    n= str(n)
    R= str(R)
    E1= float(E1)
    E2= float(E2)
    xi= float(xi)
    xf= float(xf)

    eLimSUP=E2
    eLimINF=E1
    
    """
    Funciones Internas de Usuario.
    """
    """-------------------------------------------------------------------------"""
    Pot= R+'*x**'+n
    def Psi(E,Pot,x0):
        def V(x):
            V= eval(Pot)
            return V
        
        #Correcciónes con polinomios Lagrange para gráficar en
        #el intervalo correcto.
        # if E<=50.5:
        #     CL= 4.06-0.06*E
        # elif E==0.5:
        #     CL= 5.5
        # else:
        #     CL= 5.41-0.021*E
        
        x=[-(2*E)**(0.5)]
        m= 20000
        s= (-2*x[0])/m
        g=[0,0]
        p=[0,0]
        
        
        p[0]=0.0
        p[1]=0.00001
        x.append(x[0]+s)
        g[0]=2*V(x[0]) -2*E
        g[1]=2*V(x[1]) -2*E
        s2=(s**2)/12
        
        for i in range(1,m+1,1):
            x.append(x[i]+s)
            g.append(2*V(x[i+1])-2*E)
            p.append((-p[i-1]+2*p[i]+10*g[i]*p[i]*s2+g[i-1]*p[i-1]*s2)/(1-g[i+1]*s2))
        
        if x0==1:
            return p[m]
        else:
            return p
    
    def PsiI(E,Pot):
        
        
        def V(x):
            V= eval(Pot)
            return V
        
        
        x=[xi] #Este es el intervalos para graficar
        m= 2000
        s= (xf-xi)/m
        g=[0,0]
        p=[0,0]
        
        
        p[0]=0.0
        p[1]=0.00001
        x.append(x[0]+s)
        g[0]=2*V(x[0]) -2*E
        g[1]=2*V(x[1]) -2*E
        s2=(s**2)/12
        
        for i in range(1,m,1):
            x.append(x[i]+s)
            g.append(2*V(x[i+1])-2*E)
            p.append((-p[i-1]+2*p[i]+10*g[i]*p[i]*s2+g[i-1]*p[i-1]*s2)/(1-g[i+1]*s2))
        
        plt.close('all')
        plt.clf()
        plt.plot(x,p)   
        plt.title('Er='+str(E))
        plt.show()
    
    """-------------------------------------------------------------------------"""
    
    
    """
    Programa
    """
    """-------------------------------------------------------------------------"""
    
    wpsi = True
    while wpsi :
    
        E3 = (E1+E2)/2
        if np.sign(Psi(E3,Pot,1)) == np.sign(Psi(E1,Pot,1)): 
           E1=E3
        else:
           E2=E3
           
        if abs(E1-E2)<0.0001:
            wpsi = False
        
    #print(E1)
    if abs(E1-eLimSUP)<0.0001 or abs(E1-eLimINF)<0.0001 :
        print(",ERROR,There are no reduced energies in the range")
        response= "No hay energías reducidas en el intervalo"
    else:
        PsiI(E1,Pot)
        response= str(E1)

    return response

"""-------------------------------------------------------------------------"""  
#El truco puede estar en usar los límites como condición para decidir si es
#o no un buen valor de energía.

#numerovN2(2,1,0,1,0,2)
