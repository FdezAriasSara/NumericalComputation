# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:57:20 2021

@author: Sara Fernández Arias UO269546
"""
import numpy as np
#%% Exercise 1
def incrementalSearch(f,a,b,n):
    intervals = np.zeros((n,2))#initialization of intervals matrix.
    dx=(b-a)/n#length of the intervals to evaluate
    x=np.arange(a,b+1,dx)#array with the points that will delimit the intervals
    c=0#interval counter 
    for i in range(0,n):      
      
        #First  iteration [a,dx]... last [dxn,b]
        if (f(x[i]) * f(x[i+1]) < 0):
            #By bolzanos theorem , if the sign of the function is different 
            #between the interval limits a & b-> there exists at least a root in (a,b)
           intervals[c] = x[i:i+2]#we add the interval that has a root into the interval array.
           c+=1#we update the number of subintervals with at least a root.
        
    
    intervals=intervals[:c,:]#to remove empty spaces 
    return intervals
#%% Function testing
f=lambda x: x**5 -3 *x**2+1.6 #x^5-(3x^2)+1.6
a=-1
b=1.5
n=25
result=incrementalSearch(f,a,b,n)
print("Intervals that contain f1 zeros : \n",result)

f=lambda x: (x+2)*np.cos(2*x) #(x+2)cos(2x)
a=0
b=10
n=100
result=incrementalSearch(f,a,b,n)
print("Intervals that contain f2 zeros : \n",result)
