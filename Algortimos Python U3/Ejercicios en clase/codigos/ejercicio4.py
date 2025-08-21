# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:03:59 2024

@author: Julian David
"""

"""
. Haga una función que reciba un string de números positivos separados por guiones y que
 retorne True si hay algún número repetido en la secuencia, o False en caso contrario.
045-102-102-324 -> True
32-0041-033-049 -> False
526-095-035-014 -> False
Haga luego un programa en Python que le pida al usuario el nombre de un archivo y 
haciendo uso de la función anterior, diga cuántas líneas tiene el archivo y cuántas
 de ellas contienen secuencias con números repetidos .
Los números del archivo se encuentran separados únicamente por guiones como se muestra
 en el ejemplo. 

Nota: Desarrolle el programa sin utilizar listas, pero recuerde que puede utilizar el 
método string.find(c) que retorna la primera posición donde se encuentre el carácter c en 
la cadena string.
"""

def num_repetidos(linea):
    num_repetidos='-' #-054-4-224-
    repetidos=False
    aux=''
    for index in linea:
        #range(len(linea)): # 0-len(linea)
        #caracter=linea[index]
        caracter=index
        if caracter!='-':
            aux=aux+caracter
        if caracter=='-' or index==len(linea)-1:
            if '-'+aux+'-' in num_repetidos:  #-4-   -234-44555-6
                repetidos=True
                break
            num_repetidos=num_repetidos+aux+'-'
            aux=''
    return repetidos

def num_repetidos2(linea):
    num_repetidos='-' #-054-4-224-
    repetidos=False
    aux=''
    while len(linea)>0:
        ind=linea.find('-')
        numero=linea[:ind]
        if '-'+numero+'-' in num_repetidos:
            repetidos=True
            linea=''
            break
        else:
            if ind!=-1: #la funcion str.find() retorna -1 cuando no encuentra el caracter, que en nuestro caso seria en el final de la linea,
                linea=linea[ind+1:len(linea)]
            else: linea='' 
            num_repetidos=num_repetidos+numero+'-'
    return repetidos
            


num_repetidos("032-041-033-049")

nombre=input("Dame el nombre del archivo: ")
num_lin=0
rep1=0
rep2=0
data=open(nombre,'r')
data=data.readlines()
for lin in data: #itera linea por linea el archivo
    num_lin=num_lin+1
    if num_repetidos(lin):
        rep1=rep1+1
    if num_repetidos2(lin):
        rep2=rep2+1

print('El archivo tiene ', num_lin, ' lineas en total')
print('El numero de lineas con num repetidos es igual a ', rep1, ' ',rep2)

    