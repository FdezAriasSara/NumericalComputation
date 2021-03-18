# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:12:06 2021
-SESSION 1:EXERCISE 1-
@author: Sara Fernández Arias UO269546.
"""
import numpy as np
#%%
x0=-0.4# point to compute the approximate value to.
tol=1.e-8#tolerance value.(upper limit to the eb.)

maxNumSum=100 #maximum number of terms.

polynomial=0 
factorial=1
eb=np.inf
i=0 #iteration counter.
#The loop will iterate while the number of terms is < 100
#and the error boundary is greater than the tolerance value.

#If the error boundary is LESS than te tolerance, we want the loop
#to STOP!.
while(eb>tol and i<maxNumSum):
    term =x0**i/factorial #term to add to the polynomial.
    polynomial+=term #addition of the term to the polynomial.
    
    eb=np.abs(term) #error boundary(last added term in abs value)
  
    factorial *=i+1 
    i+=1 
return polynomial

#PRINTS.
print('Function value in -0.4      = ',np.exp(-0.4))
print('Approximation value in -0.4 = ', polynomial)
print('Number of iterations        = ', i)
