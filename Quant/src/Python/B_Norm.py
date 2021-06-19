import math
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from scipy import integrate
import os
import sys

e= math.e
pi = math.pi

def Cnormalize():
    os.remove("/QClib/src/imgpython/normPlot.png") 

def Nnormalize(f):
    global constant
    sol= integrate.quad(lambda x: eval(str(f))**2,-np.inf,np.inf)
    sol1 = (1/(sol[0]**(1/2)))
    constant = round(sol1,7)
    return

Nnormalize(sys.argv[1])

def Gnormalize(fun): 
    def f(x):
        f = (eval(str(fun))/constant)**2
        return f

    vec_f = np.vectorize(f) 
    x= np.arange(-10,10,.1)
    y= vec_f(x)
    #plt.close('all')
    #plt.clf()
    plt.figure(figsize=(3,3)) 
    plt.plot(x,y)
    plt.savefig("QClib/src/imgpython/normPlot.png")    
    #plt.show()

Gnormalize(sys.argv[1])

print(constant)