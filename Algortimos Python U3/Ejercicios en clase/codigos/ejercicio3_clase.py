# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 09:35:14 2024

@author: Julian David
"""

"""
3. Implemente una función que haga lo mismo que el método replace de los objetos str.  
Esta debe recibir  tres argumentos: la cadena original, la sub-cadena a buscar y 
la sub-cadena a reemplazar. La función debe retornar la nueva cadena modificada.
"""

def replace_2(cadena_original, sub_cadena, cadena_r):
    
    if sub_cadena in cadena_original:
        index=cadena_original.find(sub_cadena)
        nueva_cadena= cadena_original[:index]+cadena_r+cadena_original[index+len(sub_cadena):]
        cadena_original=""
        return nueva_cadena
    else:
        print("La cadena a buscar no se encuentra en la cadena original")

a="Julian corre todas las tardes"
b="todas las"
c="todos los martes y jueves"

z=replace_2(a, b, c)
a2="Hola buen dia"
b2="buen"
c2="buenos"
i=replace_2(a2, b2, c2)

print(z)
print(i)