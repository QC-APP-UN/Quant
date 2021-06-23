import math
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from scipy import integrate

e= math.e
pi = math.pi

def nNormalize(f):
    sol= integrate.quad(lambda x: eval(str(f))**2,-np.inf,np.inf)
    sol1 = (1/(sol[0]**(1/2)))
    constant = round(sol1,7)
    return constant

def gNormalize(fun): 
    constant = nNormalize(fun)

    def f(x):
        f = (eval(str(fun))/constant)**2
        return f

    vec_f = np.vectorize(f) 
    x= np.arange(-10,10,.1)
    y= vec_f(x)
    plt.figure(figsize=(3,3))
    plt.title('Normalization Constant: ' + str(nNormalize(fun)))
    plt.plot(x,y)  
    plt.show()
    return constant

#gNormalize('e**(-x**2)')