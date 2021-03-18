# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:10:27 2021
SESSION 2:EXERCISE 2
@author: Sara Fernández Arias UO269546
"""
import numpy as np
import matplotlib.pyplot as plt
#%%EXERCISE 1
def hornerVP(p,x):  
    quotient=np.zeros_like(p) #initialization of the vector quotient
    y=np.zeros_like(x)#in the previous example was reminder, now it's a vector.
    quotient[0]=p[0]#the first element does not change. 
    i=1#current index.We start in 1 since the first doensnt change.
    for j in x:#For each element of the vector x
       if(i<len(quotient)):#to avoid index out of bounds problems.
           quotient[i]=p[i]+ quotient[i-1]*j       
           #the reminder will be the last element of the quotient array , 
           y[i]=quotient[len(quotient)-1]#now we have to fill the vector y
           i+=1#increment the index.

    quotient=quotient[:-1]
  
    return quotient, y
    
#%%Function testing. Using polyval command.
p = np.array([1., -1, 2, -3, 5, -2])
x = np.linspace(-1,1)
c, y = hornerVP(p, x)
plt.figure()
plt.plot(x,np.polyval(p,x))
plt.title('Polynomial P')
plt.show()


r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
c, y = hornerVP(r, x)
plt.figure()
plt.plot(x,np.polyval(r,x))
plt.title('Polynomial R')
plt.show()