# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:25:11 2021
Exercise3
@author: Sara fernández arias UO269546
"""
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision = 2)   # only two decimals
np.set_printoptions(suppress = True) # do not use exponential format
#%%

def triangular(Ar,b):
        rt = np.copy(Ar)
        bt = np.copy(b) 
        r,c=Ar.shape  
          
        for i in range(0,c):   
         
             # f will be the number we'll have to multiply row i, in order to make the element in row i+1=0-
           f=Ar[i+1][0]/Ar[i][1]
            # obtaining  0 under the main diagonal[element in At[i+1][i]=0]
           rt[i+1][0]=  Ar[i+1][0]-f*( Ar[i][1])
           bt[i+1]=bt[i+1]-f*(bt[i])#matrix b changes as well.
            #changes in the next element of the main diagonal due to the modification of that row in order to obtain 0 below main diagonal.
           rt[i+1][1]= Ar[i+1][1]- f*(Ar[i][2])
         
            
           
        return rt,bt#returning the result of the triangularization
    
def back_subs(At, bt):
    x=np.zeros_like(bt)#vector to return
    n1=len(bt)-1 # -1 since we start from the greatest index , to avoid out of bounds exception
    n2=-1#since we need the k to reach value 0
    for k in range(n1,n2,-1):#solving the equations from the bottom to the top

        if(k==n1):#Xn1=bt[n1]/At[n1][n1]
            x[k]=bt[k]/At[k][1]
            
        else:
            x[k]=(bt[k]-(At[k][2]*x[k+1]))/At[k][1]
     
    return x
    
#%% Testing


print('------------DATA------------')
n=7
Ar = np.zeros((n,3))
Ar[:,0] = np.concatenate((np.array([0]),np.ones((n-1),)))
Ar[:,1] = np.ones((n),)*3
Ar[:,2] = np.concatenate((np.ones((n-1),),np.array([0])))

b = np.arange(n,2*n)*1.

print("Ar:",Ar)
print("b:",b)
print('------------ TRIANGULAR SYSTEM------------')

At,bt= triangular(Ar,b)
print("At:",At)
print('------------SOLUTION------------')
x=back_subs(At,bt)
print("x:",x)
#-------------------------------------------------------------
print('------------DATA------------')
n = 8

np.random.seed(3)
Ar = np.zeros((n,3))
Ar[:,1] = np.random.rand(n)
Ar[:,0] = np.concatenate((np.array([0]),np.random.rand(n-1)))
Ar[0:n-1,2] = Ar[1:n,0]

b = np.random.rand(n)

print("Ar:",Ar)
print("b:",b)
print('------------ TRIANGULAR SYSTEM------------')

At,bt= triangular(Ar,b)
print("At:",At)
print('------------SOLUTION------------')
x=back_subs(At,bt)
print("x:",x)
