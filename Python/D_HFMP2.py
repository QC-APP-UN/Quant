
'''
Author: Nicolas Daniel
Contributor: David Archila Peña
'''




import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#Definimos las variables y matrices que todo el programa va a usar
global T,NucA,NucB,H,S,vecS,autS,Xcanon,TT,G,C,P,Oldp,F,Fp,Cp,E,Za,Zb,TTMO

T = np.zeros([2,2])
NucA = np.zeros([2,2])
NucB = np.zeros([2,2])
H = np.zeros([2,2])
S = np.zeros([2,2])
vecS = np.zeros([2,2])
autS = np.zeros([2,2])
Xcanon = np.zeros([2,2])    
TT = np.zeros([2,2,2,2])
G = np.zeros([2,2])
C = np.zeros([2,2])
P = np.zeros([2,2])
Oldp = np.zeros([2,2])
F = np.zeros([2,2])
Fp = np.zeros([2,2])
Cp = np.zeros([2,2])
E = np.zeros([2,2])
HFx_axis = np.zeros(81)
HFener = np.zeros(81)
MP2x_axis = np.zeros(81)
MP2corr = np.zeros(81)
MP2ener = np.zeros(81)


Energy = 0.0
Delta = 0.0

#Definición de funciones
def S_int(A,B,Rab2):
  
    return (np.pi/(A+B))**1.5*np.exp(-A*B*Rab2/(A+B))
    
def T_int(A,B,Rab2):
  
    return A*B/(A+B)*(3.0-2.0*A*B*Rab2/(A+B))*(np.pi/(A+B))**1.5*np.exp(-A*B*Rab2/(A+B))

def V_int(A,B,Rab2,Rcp2,Zc):

    V = 2.0*np.pi/(A+B)*F0((A+B)*Rcp2)*np.exp(-A*B*Rab2/(A+B))
    return -V*Zc

def F0(t):

    if (t<1e-6):
        return 1.0-t/3.0
    else:
        return 0.5*(np.pi/t)**0.5*sp.erf(t**0.5)
    
def TwoE(A,B,C,D,Rab2,Rcd2,Rpq2):

    return 2.0*(np.pi**2.5)/((A+B)*(C+D)*np.sqrt(A+B+C+D))*F0((A+B)*(C+D)*Rpq2/(A+B+C+D))*np.exp(-A*B*Rab2/(A+B)-C*D*Rcd2/(C+D))

def Intgrl(N,R,Zeta1,Zeta2,Za,Zb):
    
    global S12,T11,T12,T22,V11A,V12A,V22A,V11B,V12B,V22B,V1111,V2111,V2121,V2211,V2221,V2222
     
    S12 = 0.0
    T11 = 0.0
    T12 = 0.0
    T22 = 0.0
    V11A = 0.0
    V12A = 0.0
    V22A = 0.0
    V11B = 0.0
    V12B = 0.0
    V22B = 0.0
    V1111 = 0.0
    V2111 = 0.0
    V2121 = 0.0
    V2211 = 0.0
    V2221 = 0.0
    V2222 = 0.0
    
    R2 = R*R
    
    Coeff = np.array([[1.00000,0.0000000,0.000000],
                      [0.678914,0.430129,0.000000],
                      [0.444635,0.535328,0.154329]])
    
    Expon = np.array([[0.270950,0.000000,0.000000],
                      [0.151623,0.851819,0.000000],
                      [0.109818,0.405771,2.227660]])
    
    D1 = np.zeros([3])
    A1 = np.zeros([3])
    D2 = np.zeros([3])
    A2 = np.zeros([3])
    
    for i in range(N):
        A1[i] = Expon[N-1,i]*(Zeta1**2) #Exponente
        D1[i] = Coeff[N-1,i]*((2.0*A1[i]/np.pi)**0.75) #Norm
        A2[i] = Expon[N-1,i]*(Zeta2**2)
        D2[i] = Coeff[N-1,i]*((2.0*A2[i]/np.pi)**0.75)
    
    for i in range(N):
        for j in range(N):
            Rap = A2[j]*R/(A1[i]+A2[j])
            Rap2 = Rap**2
            Rbp2 = (R-Rap)**2
            S12 = S12 + S_int(A1[i],A2[j],R2)*D1[i]*D2[j]
            T11 = T11 + T_int(A1[i],A1[j],0.0)*D1[i]*D1[j]
            T12 = T12 + T_int(A1[i],A2[j],R2)*D1[i]*D2[j]
            T22 = T22 + T_int(A2[i],A2[j],0.0)*D2[i]*D2[j]
            V11A = V11A + V_int(A1[i],A1[j],0.0,0.0,Za)*D1[i]*D1[j]
            V12A = V12A + V_int(A1[i],A2[j],R2,Rap2,Za)*D1[i]*D2[j]
            V22A = V22A + V_int(A2[i],A2[j],0.0,R2,Za)*D2[i]*D2[j]
            V11B = V11B + V_int(A1[i],A1[j],0.0,R2,Zb)*D1[i]*D1[j]
            V12B = V12B + V_int(A1[i],A2[j],R2,Rbp2,Zb)*D1[i]*D2[j]
            V22B = V22B + V_int(A2[i],A2[j],0.0,0.0,Zb)*D2[i]*D2[j]
    
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    Rap = A2[i]*R/(A2[i]+A1[j])
                    Rbp = R - Rap
                    Raq = A2[k]*R/(A2[k]+A1[l])
                    Rbq = R - Raq
                    Rpq = Rap - Raq
                    Rap2 = Rap*Rap
                    Rbp2 = Rbp*Rbp
                    Raq2 = Raq*Raq
                    Rbq2 = Rbq*Rbq
                    Rpq2 = Rpq*Rpq
                    V1111 = V1111 + TwoE(A1[i],A1[j],A1[k],A1[l],0.0,0.0,0.0)*D1[i]*D1[j]*D1[k]*D1[l]
                    V2111 = V2111 + TwoE(A2[i],A1[j],A1[k],A1[l],R2,0.0,Rap2)*D2[i]*D1[j]*D1[k]*D1[l]
                    V2121 = V2121 + TwoE(A2[i],A1[j],A2[k],A1[l],R2,R2,Rpq2)*D2[i]*D1[j]*D2[k]*D1[l]
                    V2211 = V2211 + TwoE(A2[i],A2[j],A1[k],A1[l],0.0,0.0,R2)*D2[i]*D2[j]*D1[k]*D1[l]
                    V2221 = V2221 + TwoE(A2[i],A2[j],A2[k],A1[l],0.0,R2,Rbq2)*D2[i]*D2[j]*D2[k]*D1[l]
                    V2222 = V2222 + TwoE(A2[i],A2[j],A2[k],A2[l],0.0,0.0,0.0)*D2[i]*D2[j]*D2[k]*D2[l]
    return 

def Colect(N,R,Zeta1,Zeta2,Za,Zb):

    global Xcanon
#Matriz Cinética
    T[0,0] = T11
    T[0,1] = T12
    T[1,0] = T12
    T[1,1] = T22
    
#Matriz nuclear A
    NucA[0,0] = V11A
    NucA[0,1] = V12A
    NucA[1,0] = V12A
    NucA[1,1] = V22A
    
#Matriz nuclear B
    NucB[0,0] = V11B
    NucB[0,1] = V12B
    NucB[1,0] = V12B
    NucB[1,1] = V22B
    
# Matriz de HCore
    H[0,0] = T11+V11A+V11B
    H[0,1] = T12+V12A+V12B
    H[1,0] = H[0,1]
    H[1,1] = T22+V22A+V22B

# Matriz de Overlap
    S[0,0] = 1.0
    S[0,1] = S12
    S[1,0] = S12
    S[1,1] = 1.0
    
# Definición de X
    DiagS(S)
    smum = np.diag(1/(np.diagonal(np.sqrt(autS)))) #s^-1/2
    Smum = np.matmul(vecS,(np.matmul(smum,vecS.T)))  #S^-1/2
    Xcanon = (np.matmul(vecS,smum))
    
# Matriz coulombica y de intercambio
    TT[0,0,0,0] = V1111
    TT[1,0,0,0] = V2111
    TT[0,1,0,0] = V2111
    TT[0,0,1,0] = V2111
    TT[0,0,0,1] = V2111
    TT[1,0,1,0] = V2121
    TT[0,1,1,0] = V2121
    TT[1,0,0,1] = V2121
    TT[0,1,0,1] = V2121
    TT[1,1,0,0] = V2211
    TT[0,0,1,1] = V2211
    TT[1,1,1,0] = V2221
    TT[1,1,0,1] = V2221
    TT[1,0,1,1] = V2221
    TT[0,1,1,1] = V2221
    TT[1,1,1,1] = V2222

def SCF(N,R,Zeta1,Zeta2,Za,Zb,G):
   
    global C,E,Energytot #Los necesito para el cálculo post hartree-fock
    
    Crit = 1e-11 # Criterio de convergencia
    Maxit = 250 # Número máximo de iteraciones
    Iter=0
    
    ######## Paso 1. El guess inicial corresponde a P=0 ########
    ## El primer calculo se hará sin repulsiones electrónicas ##
    P = np.zeros([2,2])
    
    Energy = 0.0
   
    # Se confirma que se este entre el numero máximo de iteraciones y se imprime
    while (Iter<Maxit):
        Iter += 1
#        print(chr(27)+"[4;31m"+"Iteración"+chr(27)+"[0;m",Iter)
        
        ######## Paso 2. Calcular la matriz de Fock ########
        ###### Formamos la parte bielectrónica con P #######
        G = np.zeros([2,2]) # Definimos la matriz bielectrónica G
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        G[i,j]=G[i,j]+P[l,k]*(TT[i,j,k,l]-0.5*TT[i,l,k,j])

        # Sumamos HCore y G para obtener la matriz de Fock
        F = H+G
        
        # Se calcula la energía electrónica
        Energy = np.sum(0.5*P*(H+F))
        
#        print('Electronic energy = ',Energy)
        
        ######## Paso 3. Calculamos F' (remember S^-1/2 is X and S^1/2 is X.T) ########
        G  = np.matmul(F,Xcanon)
        Fp = np.matmul(Xcanon.T,G)
        
        ######## Paso 4. Diagonalización para encontrar el autovalor ########
        DiagFp(Fp)

        ######## Paso 5. Calculamos los coeficientes de los orbitales moleculares ########
        # Transform eigen vectors to get matrix C
        C = np.matmul(Xcanon,Cp)
        
        ######## Paso 6. Calculamos la nueva matriz de densidad P ########
        Oldp = np.array(P) #Guardamos la anterior matriz P
        P= np.zeros([2,2])
        
        for i in range(2): #Creamos la nueva matriz P
            for j in range(2):
                for k in range(1):
                    P[i,j] += 2.0*C[i,k]*C[j,k] #K solo es 1 porque vamos hasta la mitad de #e

        ######## Paso 7. Verificamos el criterio de convergencia ########
        Delta = 0.0
        # Se hace una suma de cuadrados y se divide por el numero de elementos en la matriz P
        Delta = (P-Oldp)
        Delta = np.sqrt(np.sum(Delta**2)/4.0)
#        print("Delta",Delta)
#        print()
        
        if (Delta<Crit):
            Energytot = Energy+Za*Zb/R #Sumamos Eelec y Enuc
#            print()
#            print(chr(27)+"[4;31m"+"Calculation converged with electronic energy:"+chr(27)+"[0;m",Energy,"Hartrees")
#            print(chr(27)+"[4;31m"+"Calculation converged with total energy:"+chr(27)+"[0;m",Energytot,"Hartrees")
#            print()
            
            break
                                        
def DiagS(A):
# Resuelve la ecuación de valores propios: A*U = U*D
    global vecS,autS
    values, vectors = np.linalg.eigh(A)   
    vecS = vectors #U
    diagVAL = np.diag(values)
    autS = diagVAL #D 
    return

def DiagFp(A):
# Resuelve la ecuación de valores propios: A*U = U*D
    global Cp,E
    values, vectors = np.linalg.eigh(A)   
    Cp = vectors
    diagVAL = np.diag(values)
    E = diagVAL     
    return

def HFCALC(N,R,Zeta1,Zeta2,Za,Zb,G):
    
    # Calcula las integrales
    Intgrl(N,R,Zeta1,Zeta2,Za,Zb)
    # Crea las matrices de integrales
    Colect(N,R,Zeta1,Zeta2,Za,Zb)
    # Cálculo SCF
    SCF(N,R,Zeta1,Zeta2,Za,Zb,G)
    return

def MP2(C,TT,E):
#Me da la energía de correlación de MP2
    global EMP2
    TTMO = np.zeros((2,2,2,2)) 
    for i in range(0,2):  
            for j in range(0,2):  
                for k in range(0,2):  
                    for l in range(0,2):  
                        for m in range(0,2):  
                            for n in range(0,2):  
                                for o in range(0,2):  
                                    for p in range(0,2):  
                                        TTMO[i,j,k,l] += C[m,i]*C[n,j]*C[o,k]*C[p,l]*TT[m,n,o,p]
    
    Nelec = 2
    
    integs=np.zeros((4,4,4,4))  
    for p in range(1,5):  
        for q in range(1,5):  
            for r in range(1,5):  
                for s in range(1,5):  
                    value1 = TTMO[(p+1)//2 -1,(r+1)//2 -1,(q+1)//2 -1,(s+1)//2 -1] * (p%2 == r%2) * (q%2 == s%2)  
                    value2 = TTMO[(p+1)//2 -1,(s+1)//2 -1,(q+1)//2 -1,(r+1)//2 -1] * (p%2 == s%2) * (q%2 == r%2) 
                    integs[p-1,q-1,r-1,s-1] = value1 - value2


    fs = np.zeros((4))  
    for i in range(0,4):
        dE = np.diagonal(E)
        fs[i] = dE[i//2]
    
    EMP2 = 0.0  
    for i in range(0,Nelec):  
        for j in range(0,Nelec):  
            for a in range(Nelec,4):  
                for b in range(Nelec,4):  
                    EMP2 += 0.25*integs[i,j,a,b]*integs[i,j,a,b]/(fs[i] +fs[j] -fs[a] - fs[b])
    return               

###### CÁLCULO ######

def HF_MP2(Z1,Z2,Za,Zb):

    Zeta1 = float(Z1)
    Zeta2 = float(Z2)
    Za = float(Za)
    Zb = float(Zb)
      
    for s in range(81): #Para el H2
        R=0.3+s*0.1
        N = 3 
        
        HFCALC(N,R,Zeta1,Zeta2,Za,Zb,G)
        HFx_axis[s] = R
        HFener[s] = Energytot #Matriz de energías HF
        MP2(C,TT,E)
        MP2x_axis[s] = R
        MP2corr[s] = EMP2 #Matriz de Ecorrelacion MP2
        
    MP2ener = HFener + MP2corr#Matriz de energía final MP2
    
    plt.figure(figsize=(3,3))
    plt.plot(HFx_axis,HFener,label="HF")
    plt.plot(MP2x_axis,MP2ener,label="MP2")
    plt.legend()
    plt.show()


    print("Values for H2 Molecule:")
    print()
    print("Distances (A.U):")
    print(HFx_axis)
    print("HF Energy:")
    print(HFener)
    print("MP2 Corrected Energy:")
    print(MP2corr)
    print()


HF_MP2(1,1,1,1)

