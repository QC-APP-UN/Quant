#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:47:02 2020

@author: davidarchilapena
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import sys

"""
Entradas
"""
"""-------------------------------------------------------------------------"""


#E1=0
#E2=1 

"""-------------------------------------------------------------------------"""


def numerovN2(k,E1,E2):

    plt.close('all')
    plt.clf()

    E1= float(E1)
    E2= float(E2)
    
    eLimSUP=E2
    eLimINF=E1
    
    """
    Funciones Internas de Usuario.
    """
    """-------------------------------------------------------------------------"""
    Pot= str(k)+'*x**2'
    def Psi(E,Pot,x0):
        def V(x):
            V= eval(Pot)
            return V
        
        #Correcciónes con polinomios Lagrange para gráficar en
        #el intervalo correcto.
        if E<=50.5:
            CL= 4.06-0.06*E
        elif E==0.5:
            CL= 5.5
        else:
            CL= 5.41-0.021*E
        
        x=[-(2*E)**(0.5)-CL]
        m= 17000
        s= (-2*x[0])/m
        g1=[0,0]
        p1=[0,0]
        
        
        p1[0]=0.0
        p1[1]=0.00001
        x.append(x[0]+s)
        g1[0]=2*V(x[0]) -2*E
        g1[1]=2*V(x[1]) -2*E
        s2=(s**2)/12
        
        for i in range(1,m+1,1):
            x.append(x[i]+s)
            g1.append(2*V(x[i+1])-2*E)
            p1.append((-p1[i-1]+2*p1[i]+10*g1[i]*p1[i]*s2+g1[i-1]*p1[i-1]*s2)/(1-g1[i+1]*s2))
        
        if x0==1:
            return p1[m]
        else:
            return p1
    
    def PsiI(E,Pot):
        
        
        def V(x):
            V= eval(Pot)
            return V
        
        
        #Correcciónes con polinomios Lagrange para gráficar en
        #el intervalo correcto.
        if E<=50.5:
            CL= 4.06-0.06*E
        elif E==0.5:
            CL= 5.5
        else:
            CL= 5.41-0.021*E
        
        x=[-(2*E)**(0.5)-CL]
        m= 17000
        s= (-2*x[0])/m
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
        
    print(E1)
    if abs(E1-eLimSUP)<0.0001 or abs(E1-eLimINF)<0.0001 :
        print("No hay energías reducidas en el intervalo")
        response = "No hay energías reducidas en el intervalo"
    else:
        PsiI(E1,Pot)
        response= str(E1)

    return response


"""-------------------------------------------------------------------------"""  

#numerovN2(sys.argv[1],sys.argv[2],sys.argv[3])

