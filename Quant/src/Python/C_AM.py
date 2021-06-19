#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Nov 22 13:00:19 2020

Author: David Archila Pena
Contributor: Nicolas Gomez Castillo
"""
import sys
import numpy as np
import math
from scipy.integrate import quad
from sympy import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

# Enable LaTEX compilation
plt.rcParams['text.usetex'] = True

e = math.e
pi = math.pi


# For export data to java
# np.set_printoptions(threshold=sys.maxsize)

# Real part of spherical harmonics

# T is theta
# P is phi

def fac(n):
    y = np.math.factorial(n)
    return y


def angular_momentum(l, m):
    l = int(l)
    m = int(m)

    function = '((((2*l+1)/(4*pi))*(fac(l-abs(m))/fac(l+abs(m))))**1/2)'
    function_m = function.replace('m', str(m))
    function_m = function_m.replace('l', str(l))
    if l - abs(m) < 0:
        return 'The absolut value of m is greater than l'
    elif l < 0:
        return 'l must be a positive integer number'
    else:
        if (-1) ** (l - abs(m)) == 1:
            c = [1]
            psi = ''
            for i in range(0, (l - abs(m)) + 1):
                if (-1) ** i == 1:
                    c.append(0)
                    c.append(((i + abs(m)) * (i + abs(m) + 1) - l * (l + 1)) * c[i] / ((i + 1) * (i + 2)))
                    psi = psi + str(c[i]) + '*np.cos(T)**' + str(i) + '+'

            psi = '(' + psi + '0' + ')'
            psi = '(np.sin(T)**abs(m)*' + psi + ')'
            psi = psi.replace('m', str(m))
            sol = quad(lambda T: eval(psi), 0, pi)
            psi = psi + '/' + str(sol[0])

        if (-1) ** (l - abs(m)) == -1:
            c = [0, 1]
            psi = ''
            for i in range(1, (l - abs(m)) + 1):
                if (-1) ** i == -1:
                    c.append(0)
                    c.append(((i + abs(m)) * (i + abs(m) + 1) - l * (l + 1)) * c[i] / ((i + 1) * (i + 2)))
                    psi = psi + str(c[i]) + '*np.cos(T)**' + str(i) + '+'

            psi = '(' + psi + '0' + ')'
            psi = '(np.sin(T)**abs(m)*' + psi + ')'
            psi = psi.replace('m', str(m))
            sol = quad(lambda T: eval(psi), 0, pi)
            psi = psi + '/' + str(sol[0])

        Yml = '(' + psi + ')' + '*np.cos(abs(m)*P)'
        Yml = Yml.replace('m', str(m))

        theta, phi = np.linspace(0, np.pi, 100), np.linspace(0, 2 * np.pi, 100)
        T, P = np.meshgrid(theta, phi)

        R = abs(eval(Yml))  # NotSoSure
        X = R * np.sin(T) * np.cos(P)
        Y = R * np.sin(T) * np.sin(P)
        Z = R * np.cos(T)

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        # plt.title(r'$Y_m^l(\tetha,\phi)$'+' l= '+ str(l)+ '; m= '+str(m))
        plt.title(r'$Y_m^l(\theta,\phi)' + '\ \ \ \ l= ' + str(l) + ';\ m= ' + str(m) + '$')

        import matplotlib.colors as mcolors

        cmap = plt.get_cmap('viridis_r')
        norm = mcolors.Normalize(vmin=Z.min(), vmax=Z.max())
        ax.plot_surface(
            X, Y, Z, rstride=1, cstride=1,
            facecolors=cmap(norm(Z)),
            linewidth=0, antialiased=False, alpha=0.5)

        T = Symbol('T')
        P = Symbol('P')

        Yml_string = Yml.replace('np.cos', 'cos')
        Yml_string = Yml_string.replace('np.sin', 'sin')
        Yml_string = Yml_string.replace('abs({})'.format(str(m)), '({})'.format(str(m)))
        Yml_string = '(' + Yml_string + ')^2'
        Yml_string = str(latex(simplify(Yml_string)))
        Yml_string = Yml_string.replace('T', r'\theta')
        Yml_string = Yml_string.replace('P', r'\phi')
        plt.title('$' + Yml_string + '$') #+ '\ \ \ \ l= ' + str(l) + ';\ m= ' + str(m) + '$')
        plt.show()
    return Yml_string
