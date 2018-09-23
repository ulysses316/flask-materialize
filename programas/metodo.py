
# coding: utf-8

# In[ ]:


#Función para polinomios
def poli(x):
    y=pow(x,2)-(3*x)-4
    return(y)
#Programa principal
print ("Este programa encuentra una raíz, por el método de bisección")
xi=float(input(' Introduce el valor de xi '))
xs=float(input(' Introduce el valor de xs '))
error=float((input(' Introduce el error ')))
xa = (xi+xs)/2.0
while (abs(poli(xa)) > error):
    xa = (xi+xs)/2.0
    if poli(xi)*poli(xa) < 0.00:
        xs=xa
        signo="negativo"
        limite="superior"
    else: 
        xs=xa
        signo="positivo"
        limite="inferior"
print(xa)

