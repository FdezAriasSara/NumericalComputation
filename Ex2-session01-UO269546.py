# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:12:06 2021
-SESSION 1:EXERCISE 2-
@author: Sara Fernández Arias UO269546.
"""

import numpy as np
import matplotlib.pyplot as plt
#%%
#Numpy arrays allow operating simoultaneously on each element they contain.
#That way, we don't need to use an auxiliar for , nor to create an auxiliar array:
    
def funExp(x, tol, maxNumSum):
    eb=np.inf #error boundary-
    factorial=1
    i=0 
    polynomial=0
    while(eb>tol and i<maxNumSum):
        term =x**i/factorial #term to add to the polynomial.
        polynomial+=term #addition of the term to the polynomial.
        
        eb=np.max(abs(term)) #error boundary(last added term in abs value)
  
        factorial *=i+1 
        i+=1 
        #we add the aprox value computed to the array of values.
    return polynomial  #return of the array of the computed approx values.
#-----------------------------------------------
x=np.linspace(-1.,1.)#numpy array of values in range(-1,1), by default returns 
#50 evenly spaced numbers between the range proposed.

y=funExp(x,1.e-8, 100)#tol=1.e-8 and maxNumSum=100

#----------------FUNCTION PLOTTING-----------------
plt.figure()
plt.plot(x,np.exp(x), 'y', linewidth=5, label='f')
plt.plot(x, y,'b--', label="f approximation")#to see the overlapping.
plt.title("f approximation with McLaurin series")
plt.legend()
plt.show()
