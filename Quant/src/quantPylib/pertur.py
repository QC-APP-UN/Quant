#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:43:35 2020

@author: davidarchilapena
"""

import eel

import numpy as np
from scipy import integrate
import math
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
import os

eel.init('src')

e= math.e
pi = math.pi

#Primero perturbación de la caja.

@eel.expose
def clear():
    os.remove("src/imgpython/perturPlot.gif")
    plt.close('all')

is_manual = False

@eel.expose
def perturECaja(L,n,per,li,ls):
    
    L=float(L)
    n=float(n)
    
    psi0 = '(2/L)**(1/2)*np.sin(pi*x*b/L)'
    psi0 = psi0.replace('L',str(L))
    psi0 = psi0.replace('b',str(n))
    corr= psi0+'*('+per+')*'+psi0
    sol= integrate.quad(lambda x: eval(corr),eval(li),eval(ls))
    E1   = sol[0]
    En= (2*pi)**2*n**2/8
    return str(En+E1)

@eel.expose
def perturCaja(L,n,per,li,ls):
    
    L=float(L)
    n=float(n)

    plt.close('all')
    plt.clf()
    
    psi0= '(2/L)**(1/2)*np.sin(pi*x*b/L)'
    psi0 = psi0.replace('L',str(L))
    psi0 = psi0.replace('b',str(n))
    # if per.find('D')>0 or per.find('D**2')>0:
    #     psi0= psi0.replace('np.sin','sp.sin')
    #     per = per.replace('D','')
    #     x = sp.Symbol('x')
    #     psi0= str(sp.diff(eval(psi0),x))
    #     psi0= psi0.replace('cos','np.cos')
    #     psi0= psi0.replace('sin','np.sin')
    
    E1s=perturECaja(L,n,per,li,ls)
    En= (2*pi)**2*n**2/8
    E1= eval(E1s)-En
    suma = 0
    i=1
    Em=0
    sol=[100,0]
    while abs(sol[0]/(En-Em))>0.000001:
        
        i=i+1
        m=i
        if m != n:
            psiM='(2/L)**(1/2)*np.sin(pi*x*m/L)'
            psiM= psiM.replace("m",str(m))
            psiM= psiM.replace("L",str(L))
            corr= psiM+'*('+per+')*'+psi0
            sol= integrate.quad(lambda x: eval(corr),eval(li),eval(ls))
            Em= (2*pi)**2*m**2/8
            suma= suma+ sol[0]/(En-Em)
        
    plt.close('all')
    plt.clf()
    fig, ax = plt.subplots()

    t = np.arange(0.0, L, 0.001)
    initial_amp = 0
    s = (2/L)**(1/2)*np.sin(pi*t*m/L)
    l, = plt.plot(t, s, lw=2)
    plt.title(r'$\psi_r (x)$ ; $E_r$ =' + str(En+E1) +" ; n="+str(n))
    # ax = plt.axis([0,L,-2,2])
    
    axamp = plt.axes([0.25, .03, 0.50, 0.02])
    # Slider
    samp = Slider(axamp, 'λ', 0, 1, valinit=initial_amp)
    
    # Animation controls
     # True if user has taken control of the animation
    interval = 100 # ms, time between animation frames
    loop_len = 5.0 # seconds per loop
    scale = interval / 1000 / loop_len
    
    def update_slider(val):
        global is_manual
        is_manual=True
        update(val)
    
    def update(val):
        # update curve
        N= 1/(1+val*suma)
        l.set_ydata((1/N)*((2/L)**(1/2)*np.sin(pi*t*n/L)+val*suma*(2/L)**(1/2)*np.sin(pi*t*n/L)))
        # redraw canvas while idle
        fig.canvas.draw_idle()
    
    def update_plot(num):
        global is_manual
        if is_manual:
            return l, # don't change
    
        val = (samp.val + scale) % samp.valmax
        samp.set_val(val)
        is_manual = False # the above line called update_slider, so we need to reset this
        return l,
    
    
    
    # call update function on slider value change
    samp.on_changed(update_slider)
    
    ani = animation.FuncAnimation(fig, update_plot, interval=interval)
    
    my_writer=animation.PillowWriter(fps=20, codec='libx264', bitrate=2)
    
    ani.save("src/imgpython/perturPlot.gif", writer=my_writer, dpi=300)
    



#print(perturCaja(L,n,per,'0','0.5*L'))


#Función Interna
def cArmonico(v,a):

    plt.close('all')
    plt.clf()
    
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
        
        psi= psi + '/' + str(sol[0])
        
    return psi


@eel.expose
def perturEOs(v,a,per,li,ls):
    
    v=int(v)
    a=float(a)
    
    if ls == "inf":
        ls="np.inf"
        
    if li == "-inf":
        li="-np.inf"
    
    psi0 = cArmonico(v,a)
    corr= psi0+'*('+per+')*'+psi0
    sol= integrate.quad(lambda x: eval(corr),eval(li),eval(ls))
    E1   = sol[0]
    return E1


@eel.expose
def perturOs(v,a,per,li,ls):

    plt.close('all')
    plt.clf()
    
    v=int(v)
    a=float(a)
    
    if ls == "inf":
        ls="np.inf"
        
    if li == "-inf":
        li="-np.inf"
    
    psi0= cArmonico(v,a)
    # if per.find('D')>0 or per.find('D**2')>0:
    #     psi0= psi0.replace('np.sin','sp.sin')
    #     per = per.replace('D','')
    #     x = sp.Symbol('x')
    #     psi0= str(sp.diff(eval(psi0),x))
    #     psi0= psi0.replace('cos','np.cos')
    #     psi0= psi0.replace('sin','np.sin')
    
    E1=perturEOs(v,a,per,li,ls)
    
    suma = 0
    i=0
    sol=[100,0]
    m=0
    for i in range(1,70):
        
        # i=i+1
        m=i
        if v!= m: 
            
            psiM= cArmonico(m,a)
            corr= '('+psiM+')*('+per+')*('+psi0+')'
            sol= integrate.quad(lambda x: eval(corr),eval(li),eval(ls))
            suma= suma+sol[0]/(v-m)
        
    psi0graf= psi0.replace('x','t')
    print(psi0graf)
    
    Ev= v + 0.5

    plt.close('all')
    plt.clf()
    fig, ax = plt.subplots()

    t = np.arange(-10, 10, 0.001)
    initial_amp = 0
    N= 1/(1+1*suma)
    s=(1/N)*(eval(psi0graf)+1*suma*eval(psi0graf))
    l, = plt.plot(t, s, lw=2)
    plt.title(r'$\psi_r (x)$ ; $E_r$ =' + str(Ev+E1) +" ; v="+str(v))
    # ax = plt.axis([-10,10,-5,5])
    
    
    axamp = plt.axes([0.25, .03, 0.50, 0.02])
    # Slider
    samp = Slider(axamp, 'λ', 0, 1, valinit=initial_amp)
    
    # Animation controls
      # True if user has taken control of the animation
    interval = 100 # ms, time between animation frames
    loop_len = 5.0 # seconds per loop
    scale = interval / 1000 / loop_len
    
    def update_slider(val):
        global is_manual
        is_manual=True
        update(val)
    
    def update(val):
        # update curve
        t = np.arange(-10, 10, 0.001)
        N= 1/(1+val*suma)
        s=(1/N)*(eval(psi0graf)+val*suma*eval(psi0graf))
        l.set_ydata(s)
        # redraw canvas while idle
        fig.canvas.draw_idle()
    
    def update_plot(num):
        global is_manual
        if is_manual:
            return l, # don't change
    
        val = (samp.val + scale) % samp.valmax
        samp.set_val(val)
        is_manual = False # the above line called update_slider, so we need to reset this
        return l,
    
    
    
    # call update function on slider value change
    samp.on_changed(update_slider)
    
    ani = animation.FuncAnimation(fig, update_plot, interval=interval)
    
    my_writer=animation.PillowWriter(fps=20, codec='libx264', bitrate=2)
    
    ani.save("src/imgpython/perturPlot.gif", writer=my_writer, dpi=300)
        
    return str(Ev+E1)


# print(perturOs(0,1,per,'-inf','inf'))

eel.start('pertur.html', port=8100)