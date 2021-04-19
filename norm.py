import math
from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate
import os
import sys

global result

e= math.e
pi = math.pi

result=0
gauss = "e**-( ((x-1)**2) /2)"

def Cnormalize():
    os.remove("src/imgpython/normPlot.png")

def Gnormalize(f):
    sol= integrate.quad(lambda x: eval(f),-np.inf,np.inf)
    
    fun=f
    def f(x):
        f = eval(fun)/sol[0]
        return f

    vec_f = np.vectorize(f)
    x= np.arange(-10,10,.1)
    y= vec_f(x)
    plt.close('all')
    plt.clf()
    plt.plot(x,y)
    #plot=plt.savefig("src/imgpython/normPlot.png")
    return

def Nnormalize(f):
    global StringSol
    sol= integrate.quad(lambda x: eval(str(f))**2,-np.inf,np.inf)
    StringSol= str(1/(sol[0]**(1/2))) 
    return

Nnormalize(gauss)
Gnormalize(gauss)

print(StringSol)

#Gnormalize(sys.argv[1])
#Nnormalize(sys.argv[1])