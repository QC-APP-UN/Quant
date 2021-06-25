#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reading SMILES

@author: davidarchilapena
"""

import numpy as np
import matplotlib.pyplot as plt
import sys


def spl(string):
    return [char for char in string]

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        g.append(el)
    yield g


def searchC(desc,i):
    
    k=i
    while desc[k].isdigit():
        k=k-1
        
    return k

def numberC(element):
    
    number=''
    chain= spl(element)
    for e in chain:
        if e.isdigit():
            number += e
    
    return int(number)

def smileToMatrix(SMILE):
    
    SMILE= SMILE.replace('C','c')
    desc = spl(SMILE) 
    
    m=0
    for i in range(len(desc)):
        
        x=desc[i]
        if x == 'c':
            
            desc[i] = 'c{}'.format(m)
            m+=1 
            
    #print(desc)
    
    n=0
    for s in desc:
        if s.startswith('c'):
            n=n+1
    # print(n)
    
    M=[]
    for i in range(n):
        s=[]
        for j in range(n):
            s.append(0)
        M.append(s.copy())
        
    # x=Symbol('x')
    #print(M)
    
    for i in range(len(M)):
        
        M[i][i]= 0
    
    #print(M)
    

    for i in range(len(desc)):
        
        if desc[i].isdigit():
            
            tag = desc[i]
            for j in range(i,len(desc)):
                if desc[j]== tag:
                    
                    if j!=i:
                        #print('Found tag {} in {} and {}'.format(tag,i,j))
                        
                        k1=searchC(desc,i)
                        m1= numberC(desc[k1])
                        
                        k2=searchC(desc,j)
                        m2= numberC(desc[k2])
                        
                        M[m1][m2]=1
                        M[m2][m1]=1
       

    desc2 = [y for y in desc if not (y.isdigit()\
                                   or y[0] == '-' and y[1:].isdigit())]

    
    b= len(listToString(desc2).split('('))
    branches= [[]]*b
    
    k=0
    for i in range(len(desc2)):
        
        if desc2[i]=='(':
            
            if desc2[i-1].startswith('c'):
                control= desc2[i-1]
            
            for j in range(i,len(desc2)):
                
                if desc2[j]==')':
                    
                    branches[k]= [control] + desc2[i+1:j].copy()
                    k=k+1
                    break
                    


    for i in range(b-1):      
        for element in branches[i][1:]:
            if element in desc2:
                desc2.remove(element)        
            
    for element in desc2:
        
        if element not in ['(',')']:
            
            branches[-1]+= [element]

    for element in branches:
        
        for i in range(1,len(element)):
            
            m1= numberC(element[i-1])
            m2= numberC(element[i])
            # print(m1)
            M[m1][m2]= 1
            M[m2][m1]= 1
    
    # print(branches)     
    return M                  
def huc(x):
    A=np.array(smileToMatrix(x))
    Vals, Coef = np.linalg.eig(A)

    idx = Vals.argsort()[::1]   
    Vals = Vals[idx]
    Coef = Coef[:,idx]
    for i in range(len(Coef)):
        Vals[i]=round(Vals[i],4)
        for j in range(len(Coef)):
            Coef[i][j]=round(Coef[i][j],3)
    Z=[]      
    for i in range(len(Coef)):
        Cof=(Coef[:,i])
        for k in range(len(Cof)):
            Z.append(str(r"$\phi$"+ str(i+1) +'='+''+','.join(map(str,Cof))))
            break
            np.delete(Cof)
            continue
    X=[]
    for i in range(len(Vals)):
        if i+1< len(Vals) and i-1 >=0:
            if Vals[i] == Vals[i+1]:
                X.append(-1)
            elif Vals[i-1] == Vals[i]:
                X.append(1)
            elif Vals[i] != Vals[i+1] and Vals[i-1] != Vals[i]:
                X.append(0)
        else:        
            X.append(0)
    plt.figure(figsize=(15,8))
    for i in range(len(Vals)):
        plt.subplot(1,2,1)
        Lin=[X[i]-0.25,X[i],X[i]+0.25]
        Y=[Vals[i],Vals[i],Vals[i]]
        plt.plot(Lin,Y,label=r"$\phi$"+str(i+1))
        plt.xlim(-2,2)
        plt.legend()
        Lin.clear()
        Y.clear()

   


    for i in range(len(Z)):
        plt.subplot(1,2,2)
        plt.text(0,i+0.1,str(Z[i]),fontsize=9)
        plt.axis('off')
        plt.ylim(0,len(Z))
    plt.show()

#huc(sys.argv[1])
                    

