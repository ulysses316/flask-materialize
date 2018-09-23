
# coding: utf-8

# In[7]:


import numpy as np
import scipy as sc
import sys  
    
print ("-----gauss jordan-----")
c1=int(input("Matriz de NxN:  "))
r1=c1
Matriz= np.zeros((r1,c1)) 
proyeccion= np.identity(r1).astype(int) 
ortogonal= np.array((0,c1)) 
ortonormal= np.zeros((r1,c1)) 


print("introduzca los elementos de la Matriz")
for r in range (0,r1):
    for c in range (0,c1):
            Matriz [r,c]=input("elemento " +str(r+1)+ ","+str(c+1)+"; ")
    
print("introduzca los elementos de la Matriz")
for r in range (0,c1):
    ortogonal [r]=input("elemento " +str(r+1)+ ","+str(c+1)+"; ")

    
          
          
        


print("-----Matriz oiginal------")
print(Matriz)
print(ortogonal)

print("-----Gauss Jordan------")
print(proyeccion)
print (np.linalg.solve(Matriz, ortogonal))


# 2###### 
