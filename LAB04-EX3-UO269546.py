# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:24:41 2021

@author: Sara Fernández Arias
"""

import numpy as np
import sympy as sym 
#%%Exercise 3 
def newton(f,df,x0,tol=1e-6,maxiter=100):
     sol=x0#INTIAL GUESS.
     err=np.inf#make sure the program enters the loop at least once.
     n=0#number of iterations
     while(n<100 and err>tol):
         x=sol-(f(sol)/df(sol))
         #Appliying the formula: replacing f with it's tangent. The coresponding zero , 
         #sol, will be computed as an aproximation. For that we use an initial guess 
         err=np.abs(x-sol)#computing the error
         sol=x
         n+=1
     return sol, n;#returning the zero found and the number of iterations taken to find it.
 
#%% Function testing
#We obtained the following results from incremental search ;
#[[-0.7 -0.6], [ 0.8  0.9] [ 1.2  1.3]] those will be the intervals 
#to call the Newton-Raphson's method to 
x=sym.Symbol('x',real =True)
f=x**5 -3*x**2+1.6 #x^5-(3x^2)+1.6
df=sym.diff(f,x)
#Lambdifying
f=sym.lambdify([x],f,'numpy')
df=sym.lambdify([x],df,'numpy')



a=-0.7
b=-0.6

s,n=newton(f,df,a)
print("sol-:",s, " iterations:",n)
a=0.8
b=0.9

s,n=newton(f,df,a)
print("sol-:",s, " iterations:",n)


a=1.2
b=1.3

s,n=newton(f,df,a)
print("sol-:",s, " iterations:",n)
