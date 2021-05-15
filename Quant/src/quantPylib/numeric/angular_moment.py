#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Nov 22 13:00:19 2020

Author: David Archila Pena
Contributor: Nicolas Gomez Castillo

"""

import numpy as np
import math
from scipy.integrate import quad
from sympy import *

e = math.e
pi = math.pi


# Real part of spherical harmonics

# T is theta
# P is phi

def fac(n):
    y = np.math.factorial(n)
    return y

