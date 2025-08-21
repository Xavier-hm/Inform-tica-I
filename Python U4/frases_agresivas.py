"""
En un archivo de texto plano está almacenado un listdo de 
expresiones extremadamente agresivas (una por cada linea del
archivo) que son usadas para identificar y sancionar usuarios de
una red social. Haga una función que reciba el nombre del archivo
y una frase en una cadena de caracteres. La función debe retornar
True en caso de encontrar la frase en el archivo o False en caso
contario

Haga un programa principal que le pida al usuario el nombre del
archivo y luego repetidamente le pida frases para verificar
(invocando la función) si son consideradas expresiones
extremadamente agresivas o no. Si el usuario ingresa una X, el
programa mostrará en pantalla la cantidad de frases que resultaron
extremadamente agresivas y terminará.
"""

def frase_agresiva(nombre_archivo, frase):
    ar = open(nombre_archivo, "r")
    for linea in ar:
        if linea[-1] == "\n":
            if frase == linea [:-1]:
                return True
        else:
            if frase == linea:
                return True
    
    return False

nombre = input("Ingrese el nombre del archivo: ")
frase = input("Ingrese una frase a verificar: ")

c = 0

while frase != "x":
    res = frase_agresiva(nombre, frase)
    if res == True:
        c = c + 1
    frase = input("Ingrese una frase a verificar: ")

if c == 0:
    print("No ingresaste frases agresivas")
elif c == 1:
    print("Ingresaste", c, "frase agresiva")
else:
    print("ingresaste", c, "frases agresivas")

