
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: David Archila Peña
"""


##############
# Libraries  #
##############

import sys 
import numpy as np
#import matplotlib.pyplot as plt
import math as m



def basis(string):
    coef = list(string.split('#'))
    
    for x in coef:
        x= float(x)
        
    return coef



def SBasis(argument):
    switcher = {
        'STO-1G': 1,
        'STO-2G': 2,
        'STO-3G': 3,
        'User Defined': 0,
       
    }
    print(switcher.get(argument, "Invalid Option"))
    return switcher.get(argument, "Invalid Option")

def HF_H2(b1,UdBS_D,UdBS_A,D):
    
    Basis1 = int(SBasis(b1)) #[1,2,3,0]
    
    Basis0 = [basis(UdBS_D),basis(UdBS_A)]
    
    D= float(D)

    ####################
    # Basis Set STO-1G #
    ####################
        
    
    D_1G=[1]
    A_1G=[0.270950]
    
    ####################
    # Basis Set STO-2G #
    ####################
        
    
    D_2G=[0.678914,0.430129]
    A_2G=[0.151623,0.851819]
    
    
    ####################
    # Basis Set STO-3G #
    ####################
        
    
    D_3G=[0.444635,0.154329,0.535328]
    A_3G=[0.168856,3.42525,0.623913]

    ####################
    # Basis Set Matrix #
    ####################
    
    B = [[Basis0],[D_1G,A_1G],[D_2G,A_2G],[D_3G,A_3G]]
    
    
    #################################
    # Gaussian Functions defintion  #
    #################################
    
    def G(Z,Ra,y): #Gaussian
        return (2*Z/np.pi)**.75*np.exp(-Z*(y-Ra)**2)
    
    
    def CGF(d1,a1,R1,y):
        
        suma=0
        for i in range(len(d1)):
            
            terSig= d1[i]*G(a1[i],R1,y)
            suma += terSig
        
        return suma
    
    
    ##################
    # Overlap Matrix #
    ##################
    
    
    ######################################################################
    # This calculation was done using Szabo Apendix A with coeffiecients #
    # sugested for STO-3G basis set.                                     #
    ######################################################################
    
    
    def S_CGF(c,d1,a1,D):
        
        R =[0,D]
        SM =np.zeros((c,c))
            
        for k in range(c):
            for l in range(c):
                
                if k==l:
                    n=0
                else:
                    n=1
                    
                suma=0
                for j in range(len(d1)):
                    for i in range(len(d1)):
                        N= (2*a1[j]/np.pi)**.75*(2*a1[i]/np.pi)**.75
                        I= (np.pi/(a1[j]+a1[i]))**1.5*np.exp(-a1[j]\
                            *a1[i]*(0-R[n])**2/(a1[j]+a1[i]))
                        S= d1[j]*d1[i]*N*I
                        suma += S
                
                SM[k][l] = suma
                
        return SM
    
    
    ##################
    # Hcore   Matrix #
    ##################
    
    def T_CGF(c,d,a,D):
        
        R =[0,D]
        TM =np.zeros((c,c))
            
        for k in range(c):
            for l in range(c):
                
                if k==l:
                    n=0
                else:
                    n=1
                
                suma=0
                for j in range(len(d)):
                    for i in range(len(d)):
                        N= (2*a[j]/np.pi)**.75*(2*a[i]/np.pi)**.75
                        I= (a[j]*a[i]/(a[j]+a[i]))*(3-2*a[j]*a[i]*(0-R[n])**2/(a[j]+a[i]))*\
                            (np.pi/(a[j]+a[i]))**1.5*\
                            np.exp(-a[j]*a[i]*(0-R[n])**2/(a[j]+a[i]))
                        T= d[j]*d[i]*N*I
                        suma += T
                
                TM[k][l] = suma
                
        return TM
    
    
    def F0(t):
        
        if t != 0:
            F0= 0.5*(np.pi/t)**0.5*m.erf(t**0.5)
        else:
            F0=1
        
        return F0
    
    def V_CGF1(c,d,a,D,Z):
        
        R =[0,D]
        RN=[0,D]
        VM1 =np.zeros((c,c))
            
        for k in range(c):
            for l in range(c):
                
                if k==l:
                    n=0
                else:
                    n=1
                
                suma=0
                for j in range(len(d)):
                    for i in range(len(d)):
                        RP= (a[j]*0+a[i]*R[n])/(a[j]+a[i])
                        N= (2*a[j]/np.pi)**.75*(2*a[i]/np.pi)**.75
                        I= -2*np.pi/(a[j]+a[i])*(Z)\
                            *np.exp(-a[i]*a[j]/(a[j]+a[i])*(0-R[n])**2)\
                            *F0((a[j]+a[i])*(RP-RN[k])**2.0)
                        V= d[j]*d[i]*N*I
                        suma += V
                
                VM1[k][l] = suma
                
        return VM1
    
    def V_CGF2(c,d,a,D,Z):
        
        R =[0,D]
        RN=[0,D]
        VM2 =np.zeros((c,c))
            
        for k in range(c):
            for l in range(c):
                
                if k==l:
                    n=0
                else:
                    n=1
                
                suma=0
                for j in range(len(d)):
                    for i in range(len(d)):
                        RP= (a[j]*0+a[i]*R[n])/(a[j]+a[i])
                        N= (2*a[j]/np.pi)**.75*(2*a[i]/np.pi)**.75
                        I= -2*np.pi/(a[j]+a[i])*(Z)\
                            *np.exp(-a[i]*a[j]/(a[j]+a[i])*(0-R[n])**2)\
                            *F0((a[j]+a[i])*(RP-RN[1-k])**2.0)
                        V= d[j]*d[i]*N*I
                        suma += V
                
                VM2[k][l] = suma
                
        return VM2
    
    
    
    ###########################
    # Results Printing Part 1 #
    ###########################
        
    
    print('###############################')
    print('# Basic HF Calculations on H2 #')
    print('###############################')
    print('')
    print('')
                
    SM = S_CGF(2,B[Basis1][0],B[Basis1][1],D)
    TM = T_CGF(2,B[Basis1][0],B[Basis1][1],D)
    VM1 = V_CGF1(2,B[Basis1][0],B[Basis1][1],D,1)
    VM2 = V_CGF2(2,B[Basis1][0],B[Basis1][1],D,1)
    
    print('##################')
    print('# Overlap Matrix #')
    print('##################')
    print('')
    print('')
    print(SM) # Overlap Matrix
    print('')
    print('')
    
    print('##############################')
    print('# Electronic Kinetic Energy  #')
    print('##############################')
    print('')
    print('')
    print(TM) # Electronic Kinetic Energy
    print('')
    print('')
    
    print('##################################')
    print('# Porential Energy of Electrons  #')
    print('##################################')
    print('')
    print('')
    
    print(VM1) # Potential energy e-N1
    print(VM2) # Potencial energy e-N2
    
    print('')
    print('')
    
    
    H_core= TM + VM1 + VM2
    
    print('##################################')
    print('# Core Matrix                    #')
    print('##################################')
    print('')
    print('')
    
    print(H_core) # Energy Matrix without electronic repulsion 
    
    print('')
    print('')
    
    ##########################
    # Two electron integrals #
    ##########################
    
    
    def TEI(d,a,D,I):
        
        R= [(I[0]-1)*D,(I[1]-1)*D,(I[2]-1)*D,(I[3]-1)*D]
        suma=0
        for k in range(len(d)):
            for l in range(len(d)):
                for j in range(len(d)):
                    for i in range(len(d)):
                        RP= (a[j]*R[0]+a[i]*R[1])/(a[j]+a[i])
                        RQ= (a[k]*R[2]+a[l]*R[3])/(a[k]+a[l])
                        
                        N= ((2*a[j]/np.pi)**.75*(2*a[i]/np.pi)**.75)\
                           *((2*a[k]/np.pi)**.75*(2*a[l]/np.pi)**.75)
                        I= 2*np.pi**2.5/((a[j]+a[i])*(a[k]+a[l])*(a[j]+a[i]+a[k]+a[l])**0.5)\
                           *np.exp(-a[i]*a[j]/(a[i]+a[j])*(R[0]-R[1])**2\
                                   -a[k]*a[l]/(a[k]+a[l])*(R[2]-R[3])**2)\
                           *F0((a[j]+a[i])*(a[k]+a[l])/(a[j]+a[i]+a[k]+a[l])*(RP-RQ)**2)
                        TEI= d[j]*d[i]*d[k]*d[l]*N*I
                        suma += TEI
                            
        return suma
    
    
    
    ############################
    # C matrix (Initial Guess) #
    ############################
    
    a= (2*(1+SM[0][1]))**(-0.5)
    b= (2*(1-SM[0][1]))**(-0.5)
    C= np.array([[a,b],
                 [a,-b]])
    
    
    
    ###############
    # Fock Matrix #
    ###############
    
    def F_CGF(c,S,H,D):
        
        F =np.zeros((c,c))
    
        for k in range(c):
            for l in range(c):
                
                suma=0
                for a in range(1): # N/2
                    for i in range(c):
                        for j in range(c):
                            I1= TEI(B[Basis1][0],B[Basis1][1],D,[k,l,j,i])
                            I2= TEI(B[Basis1][0],B[Basis1][1],D,[k,i,j,l])
                            suma+=C[i][a]*C[j][a]*(2*I1-I2)
                
                F[k][l] = H[k][l] + suma
                
        return F
    
    
    print('##################################')
    print('# Fock Matrix                    #')
    print('##################################') 
    print('')
    print('')
    
    FM=F_CGF(2,SM,H_core,1.4)
    print(FM)
    
    print('')
    print('')
    
    
    ####################
    # Rothan Equations #
    ####################
    
    
    e1 = (FM[0][0]+FM[0][1])/(1+SM[0][1]) 
    e2 = (FM[0][0]-FM[0][1])/(1-SM[0][1])
    
    print('##################################')
    print('# Orbital Energies               #')
    print('##################################') 
    print('')
    print('')
    
    
    print('H2 1s', e1)
    print('H2 2s', e2)
    
    print('')
    print('')
    
    
    ####################################
    # Charge Density Bond-Order Matrix #
    ####################################
    
    def P_CGF(c,C,S,H,D):
        
        P =np.zeros((c,c))
        
        for i in range(c):
            for j in range(c):
                
                suma=0
                for a in range(1):
                    suma = 2*C[i][a]*C[j][a]
                    
                P[i][j]=suma
        
        return P
    
    PM= P_CGF(2,C,SM,H_core,1.4)
    
    print('####################################')
    print('# Charge Density Bond-Order Matrix #')
    print('####################################') 
    print('')
    print('')
    
    print(PM)
    
    print('')
    print('')
    
    def E0(c,P,H,F):
        
        suma=0
        for i in range(c):
            for j in range(c):
                
                tersig= P[j][i]*(H[i][j]+F[i][j])
                suma += tersig
                
        E0= 0.5*suma
        
        return E0
    
    E0M= E0(2,PM,H_core,FM)
    ETOT= E0M+1/1.4
    
    print('Total Electronic Energy: ', E0M, ' Eh') #Electronic Energy
    print('Total Energy: ', ETOT, 'Eh') #Total Enegy
 
    
 
#HF_H2('STO-3G','0#0','0#0','1.4')
 
    