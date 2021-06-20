#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:40:47 2021

@author: davidarchilapena
"""


"""
This program creates and compares Gaussian type basis sets for S orbtials.
"""

"""
Inputs and Outputs Description.

Inputs: basis set selection (2)
Outputs: Comparision graph

"""


"""
Libraries
"""

from sys import *

import numpy as np


"""
User Functions
"""

def basis(string):
    coef = list(string.split())
    return coef

###########
# Inputs  #
###########


Basis1 = sys.argv[1]
Basis2 = sys.argv[2]

BasisO = [basis(sys.argv[3]),basis(sys.argv[4])]

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

####################
# Basis Set STO-1G #
####################
    

D_1G=[0.444635]
A_1G=[0.168856]

####################
# Basis Set STO-2G #
####################
    

D_2G=[0.444635,0.154329]
D_3G=[0.168856,3.42525]


####################
# Basis Set STO-3G #
####################
    

D_3G=[0.444635,0.154329,0.535328]
A_3G=[0.168856,3.42525,0.623913]

