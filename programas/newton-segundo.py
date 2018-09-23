
# coding: utf-8

# In[2]:


from __future__ import division 
from sympy import *
from scipy import *
from numpy import sqrt, sin, cos, pi
import sys

x, y, z, t = symbols('x y z t') 
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing(use_unicode=True)

pol = input("introduzca la funcion del plano: ")
poli= str(pol)
polis=sympify(poli)
deris= polis.diff(x)
deriss= deris.diff(x)


#Programa principal
print ("Método de Newton-Raphson")
x=float(input('Introduce el valor de inicio '))

erroru=float(input('Introduce el error '))
raiz=[ ]
raiz.insert(0,0)
i=0
error=1
deri= str(deriss)
deri=eval(deri)
derbi=float(deri)
while abs(error) > erroru:
    er=error
    poli= str(polis)
    
    poli=eval(poli)

    x1=x-(poli/derbi)
    raiz.append(x1)
    i=i+1
    x=x1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print (x)
  
        
print (x)

