# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:25:11 2021

@author: Sara fernández arias UO269546
"""
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision = 2)   # only two decimals
np.set_printoptions(suppress = True) # do not use exponential format
#%%Funtion definition.

def triangular(A,b):
        At = np.copy(A)
        bt = np.copy(b) 
        dig=len(At) #number of elements in main diagonal        
        for i in range(0,dig-1):            
             # f will be the number we'll have to multiply row i, in order to make the element in row i+1=0-
            f=At[i+1][i]/At[i][i]
            # obtaining  0 under the main diagonal[element in At[i+1][i]=0]
            At[i+1][i]=  At[i+1][i]-f*( At[i][i])
            bt[i+1]=bt[i+1]-f*(bt[i])#matrix b changes as well.
            #changes in the next element of the main diagonal due to the modification of that row in order to obtain 0 below main diagonal.
            At[i+1][i+1]= At[i+1][i+1]- f*(At[i][i+1])
         
            
           
        return At,bt#returning the result of the triangularization 
    
#%% plotting.
print('------------DATA------------')
n = 7 

A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1) 
A = A1 + A2 + A2.T 

b = np.arange(n,2*n)*1.
print("A:",A)
print("b:",b)
print('------------ TRIANGULAR SYSTEM------------')
At,bt= triangular(A,b)
print("A:",At)
print("b:",bt)
print('------------DATA------------')
n=8
np.random.seed(3)
A1 = np.diag(np.random.rand(n))
A2 = np.diag(np.random.rand(n-1),1)
A = A1 + A2 + A2.T 

b = np.random.rand(n)
print("A:",A)
print("b:",b)
print('------------ TRIANGULAR SYSTEM------------')
At,bt= triangular(A,b)
print("A:",At)
print("b:",bt)



