# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:10:27 2021
SESSION 2:EXERCISE 1
@author: Sara Fernández Arias UO269546
"""
import numpy as np
import matplotlib.pyplot as plt
#%%EXERCISE 1
def horner(p,x0):  
    quotient=np.zeros_like(p) #initialization of the vector quotient
    remainder=0.
    quotient[0]=p[0]#the first element does not change.   
    for i in range(1,len(p)):                     
       quotient[i]=p[i]+ quotient[i-1]*x0
       
    #the reminder will be the last element of the quotient array , 
    reminder=quotient[len(quotient)-1]

    quotient=quotient[:-1]
  
    return quotient, reminder
    
#%%Function testing.
p0 = np.array([1.,2,1])
x0 = 1.
c, r = horner(p0, x0)
print('Q coefficients =  ', c)
print('P0(1) = ', r)

p1 = np.array([1., -1, 2, -3,  5, -2])
x1 = 1.
c, r = horner(p1, x1)
print('Q coefficients = ',c)
print('P1(1) = ',r)


p2 = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x2 = -1.
c, r = horner(p2, x2)
print('Q coefficients =  ', c)
print('P2(-1) = ', r)


