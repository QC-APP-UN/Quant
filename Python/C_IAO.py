#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:04:29 2020

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
hbar= 1.054571628*10**-34


    

def cArmonico1D(v,a,f):

    plt.close('all')
    plt.clf()
    
    if f>=1:
        l= 0.0291181*f+1.55316
    else:
        l= 19.51951952*f+4.44444444e-3
    if (-1)**(v)==1:
        
        c=[1]
        
        psi=''
        for i in range(0,v+1):
            
            if (-1)**(i)==1:
                c.append(0)
                c.append(2*a*(i-v)*c[i]/((i+1)*(i+2)))
        
                psi= psi + str(c[i]) + '*x**' + str(i) + '+'
        
        psi= '('+ psi + '0' + ')'
        psi= 'e**((-a*x**2)/2)*'+psi
        
        psi=psi.replace('a',str(a))
        sol= integrate.quad(lambda x: eval(psi)**2,-np.inf,np.inf)
        def psiAr(x,a): 
            psin=eval(psi)/sol[0]
            return psin
        
        
        vec_psi = np.vectorize(psiAr)
        x= np.arange(-0.01/l,0.01/l,.00001)
        y= vec_psi(x,a)
        plt.plot(x,y)
        plt.show()
        
    if (-1)**(v)==-1:
        
        c=[0,1]
        
        psi=''
        for i in range(1,v+1):
            if (-1)**(i)==-1:
                c.append(0)
                c.append(2*a*(i-v)*c[i]/((i+1)*(i+2)))
            
                psi= psi + str(c[i]) + '*x**' + str(i) + '+'
        
        psi= '('+ psi + '0' + ')'
        psi= 'e**((-a*x**2)/2)*'+psi
        
        psi=psi.replace('a',str(a))
        sol= integrate.quad(lambda x: eval(psi)**2,-np.inf,np.inf)
        def psiAr(x,a): 
            psin=eval(psi)/sol[0]
            return psin
        
        
        vec_psi = np.vectorize(psiAr)
        x= np.arange(-0.01/l,0.01/l,.00001)
        y= vec_psi(x,a)
        plt.plot(x,y)
        plt.show()
        


def cArmonico2D(v1,v2,a,f):

    plt.close('all')
    plt.clf()
    
    if f>=1:
        l= 0.0291181*f+1.55316
    else:
        l= 19.51951952*f+4.44444444e-3
    if (-1)**(v1)==1:
        
        c=[1]
        
        psi=''
        for i in range(0,v1+1):
            if (-1)**(i)==1:
                c.append(0)
                c.append(2*a*(i-v1)*c[i]/((i+1)*(i+2)))
            
                psi= psi + str(c[i]) + '*x**' + str(i) + '+'
        
        psi= '('+ psi + '0' + ')'
        psi= 'e**((-a*x**2)/2)*'+psi
        
        psi=psi.replace('a',str(a))
        sol= integrate.quad(lambda x: eval(psi)**2,-np.inf,np.inf)
        def psiAr1(x,a): 
            psin=eval(psi)/sol[0]
            return psin
        
        if (-1)**(v2)==1:
        
            c=[1]
            
            psi2=''
            for i in range(0,v2+1):
                if (-1)**(i)==1:
                    c.append(0)
                    c.append(2*a*(i-v2)*c[i]/((i+1)*(i+2)))
                
                    psi2= psi2 + str(c[i]) + '*x**' + str(i) + '+'
            
            psi2= '('+ psi2 + '0' + ')'
            psi2= 'e**((-a*x**2)/2)*'+psi2
            
            psi2=psi2.replace('a',str(a))
            sol= integrate.quad(lambda x: eval(psi2)**2,-np.inf,np.inf)
            def psiAr2(x,a): 
                psin=eval(psi2)/sol[0]
                return psin
            
        if (-1)**(v2)==-1:
        
            c=[0,1]
            
            psi2=''
            for i in range(1,v2+1):
                if (-1)**(i)==-1:
                    c.append(0)
                    c.append(2*a*(i-v2)*c[i]/((i+1)*(i+2)))
                
                    psi2= psi2 + str(c[i]) + '*x**' + str(i) + '+'
            
            psi2= '('+ psi2 + '0' + ')'
            psi2= 'e**((-a*x**2)/2)*'+psi2
            
            psi2=psi2.replace('a',str(a))
            sol= integrate.quad(lambda x: eval(psi)**2,-np.inf,np.inf)
            def psiAr2(x,a): 
                psin=eval(psi2)/sol[0]
                return psin
            

        def psiAr2D(x,y,a):
            psin= psiAr1(x,a)*psiAr2(y,a)
            
            return psin
        
        vec_psi = np.vectorize(psiAr2D)
        
        x = np.linspace(-0.01/l, 0.01/l, 50)
        y = np.linspace(-0.01/l, 0.01/l, 50)
        
        X, Y = np.meshgrid(x, y)
        Z = vec_psi(X, Y,a)
        

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.contour3D(X, Y, Z, 50, cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel(r'$\mathrm{\psi}$');
        ax.view_init(40, 35)
        ax.set_title(r'$\mathrm{\psi(x,y)}$');        
        plt.show()
        
    if (-1)**(v1)==-1:
        
        c=[0,1]
        
        psi=''
        for i in range(1,v1+1):
            if (-1)**(i)==-1:
                c.append(0)
                c.append(2*a*(i-v1)*c[i]/((i+1)*(i+2)))
            
                psi= psi + str(c[i]) + '*x**' + str(i) + '+'
        
        psi= '('+ psi + '0' + ')'
        psi= 'e**((-a*x**2)/2)*'+psi
        
        psi=psi.replace('a',str(a))
        sol= integrate.quad(lambda x: eval(psi)**2,-np.inf,np.inf)
        def psiAr1(x,a): 
            psin=eval(psi)/sol[0]
            return psin
        
        
        if (-1)**(v2)==1:
        
            c=[1]
            
            psi2=''
            for i in range(0,v2+1):
                if (-1)**(i)==1:
                    c.append(0)
                    c.append(2*a*(i-v2)*c[i]/((i+1)*(i+2)))
                
                    psi2= psi2 + str(c[i]) + '*x**' + str(i) + '+'
            
            psi2= '('+ psi2 + '0' + ')'
            psi2= 'e**((-a*x**2)/2)*'+psi2
            
            psi2=psi2.replace('a',str(a))
            sol= integrate.quad(lambda x: eval(psi2)**2,-np.inf,np.inf)
            def psiAr2(x,a): 
                psin=eval(psi)/sol[0]
                return psin
            
        if (-1)**(v2)==-1:
        
            c=[0,1]
            
            psi2=''
            for i in range(1,v2+1):
                if (-1)**(i)==-1:
                    c.append(0)
                    c.append(2*a*(i-v2)*c[i]/((i+1)*(i+2)))
            
                psi2= psi2 + str(c[i]) + '*x**' + str(i) + '+'
            
            psi2= '('+ psi2 + '0' + ')'
            psi2= 'e**((-a*x**2)/2)*'+psi2
            
            psi2=psi2.replace('a',str(a))
            sol= integrate.quad(lambda x: eval(psi2)**2,-np.inf,np.inf)
            def psiAr2(x,a): 
                psin=eval(psi2)/sol[0]
                return psin
            

        def psiAr2D(x,y,a):
            
            psin= psiAr1(x,a)*psiAr2(y,a)
            
            return psin
        
        vec_psi = np.vectorize(psiAr2D)
        
        x = np.linspace(-0.01/l, 0.01/l, 50)
        y = np.linspace(-0.01/l, 0.01/l, 50)
        
        X, Y = np.meshgrid(x, y)
        Z = vec_psi(X, Y,a)
        
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

def osar(d,f,v1,v2):

    d=int(d)

    m=float(9.10938291*10**(-31))


    v1=int(v1)
    v2=int(v2)
    
    a=2*pi*f*m/hbar
    if d ==1:
        cArmonico1D(v1,a,f)
    if d==2:
        cArmonico2D(v1,v2,a,f)
        
#osar(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])

osar(2,500,2,2)
        
