#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:22:20 2020

@author: davidarchilapena
"""

import eel

import numpy as np
from scipy import integrate
import math

eel.init('src')

e= math.e
pi = math.pi

@eel.expose
def orto(f1,f2):

    sol= integrate.quad(lambda x: eval(f1)*eval(f2),-np.inf,np.inf)
    print(sol[0])

    if sol[0]<0.0001:
        respuesta=  'Son Ortogonales'
    else:
        respuesta = 'No Ortogonales'

    return respuesta

eel.start('orto.html', port=8080)