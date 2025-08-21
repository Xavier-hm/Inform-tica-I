# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:06:20 2024

@author: Julian David
"""

"""
Implemente una función que haga lo mismo que el método replace de los objetos str. 
 Esta debe recibir  tres argumentos: la cadena original, la sub-cadena a buscar y 
 la sub-cadena a reemplazar. La función debe retornar la nueva cadena modificada.
"""

def replace_2(original,buscar,reemplazar):
    nueva_cadena=''
    if buscar in original:
        for i in range(len(original)):
           if original[i:i+len(buscar)]==buscar:
               nueva_cadena=original[:i]+reemplazar+original[i+len(buscar):]
               original=nueva_cadena
            
    else:
        print('No se encontro la cadena')
        
        
        
    return nueva_cadena

a='hola soy julian'
b='julian'
c='marco'
print(replace_2(a,b,c))

print(replace_2('hola soy julian','julian','marco'))
print(replace_2('hola soy julian','o','_'))
print(replace_2('hola soy julian','+','_'))
