# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:18:28 2021

@author: Sara Fernández Arias
"""
import numpy as np
#%%Exercise 2
def bisection(f,a,b,tol=1e-6,maxiter=100):  
    err=np.inf #we start at infinite to make sure it enters the loop
    n=0#iteration counter.
    sol=0.
    while(n<100 and err>=tol):
   #stop when the max number of iterations(we start at 0!) is met or when the error is < than tol
        x=(a+b)/2# middle point value
        
        err=np.abs(x-sol)#absolute error
        if(f(a)*f(x)<0):
            #note that the multiplication of two points with the same sign cannot be negative.
            #BOLZANO:if the left subinterval has different signs at its endpoints , it contains at least zero            
            b=x
            
        elif(f(x)*f(b)<0):     
            
             #BOLZANO:if the right subinterval has different signs at its endpoints , it contains at least  zero            
            a=x
       
        sol=x#in case the stop criteria is met, the sol would be the current middle.
        n+=1#increment the counter.
    
    return sol, n;

#%% Function testing
#We obtained the following results from incremental search ;
#[[-0.7 -0.6], [ 0.8  0.9] [ 1.2  1.3]] those will be the intervals 
#to call the bisection method to 
f=lambda x: x**5 -3 *x**2+1.6 #x^5-(3x^2)+1.6
a=-0.7
b=-0.6

s,n=bisection(f,a,b)
print("sol-:",s, " iterations:",n)
a=0.8
b=0.9

s,n=bisection(f,a,b)
print("sol-:",s, " iterations:",n)


a=1.2
b=1.3

s,n=bisection(f,a,b)
print("sol-:",s, " iterations:",n)

