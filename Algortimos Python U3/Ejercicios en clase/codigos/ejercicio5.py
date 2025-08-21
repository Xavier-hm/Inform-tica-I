# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:19:17 2024

@author: Julian David
"""
"""Según la teoría de números, un número abundante es aquel cuya suma de sus divisores propios
 (excluyendo el propio número) es mayor que el número mismo. Por ejemplo, el número 12 es
 abundante porque la suma de sus divisores propios (1, 2, 3, 4 y 6) es 16, que es mayor que 12.
 

Se le solicita desarrollar un programa que permita al usuario ingresar N números enteros 
positivos y determine si es abundante o no. Además, el programa debe guardar el resultado 
en un archivo de texto llamado "SalidaAbundantes.txt", indicando si los números son abundantes
 o no.
"""
def num_abundante(num): 
    if num>0:
        suma_div=0
        for n in range(1,num): # 1 2 3 4 5 ...11
            if num%n==0:
                suma_div=suma_div+n
        if suma_div>num:
            return True
        else: return False
    
#print(num_abundante(12))
#print(num_abundante(4))

print("Ingrese los numeros al programa, para terminar escriba -")
while True:
    a=input("Ingrese el numero: ")
    if a=='-': break
    else:
        a=int(a)
        datos=open('SalidaAbundantes.txt','a')
        if num_abundante(a):
            datos.write(str(a)+' es un numero abundante \n')
        else: 
            datos.write(str(a)+' no es un numero abundante \n')
            
            #julian.santamaria@udea.edu.co
        
    
    


        
        