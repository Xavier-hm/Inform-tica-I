"""
Desarrolle una función que reciba un string que contiene dos números enteros
separados por un guión y que retorne los dos números en variables tipo int.

Luego desarrolle un programa para determinar si los datos climáticos que hay
guardados en un archivo, tienen sospecha de error. En cada fila del archivo se
encuentra la cantidad de lluvia y de radiación solar en un mes, donde la
primera fila representa el mes pasado, la siguiente el mes antepasado y asi 
sucesivamente. Se considera que los datos tienen sospecha de error si se
cumple alguna de las siguientes condiciones:

- Que tanto la lluvia como la radiación siempre disminuyeron mes a mes.
- Que tanto la lluvia como la radiación siempre aumentaron mes a mes.

El programa debe pedir al usuario el nombre del archivo donde se encuentran
los datos y haciendo uso de la función desarrollada, imprimir en pantalla un
mensaje en caso de que se encuentre que hay sospecha de error en los datos. El
siguiente es un ejemplo del formato y los datos del archivo:

27-94
26-107
15-87
14-115
"""

def two_nums(line):
    pos_dash = line.find("-")
    rain = line [:pos_dash]
    rad = line[pos_dash+1:]
    return rain, rad

f_name = input("Ingrese el nombre del archivo: ")
data = open(f_name, "r")
c = 0
rain_rad_dec = True
for line in data:
    if line[-1] == "\n":
        line = line[:-1]
    thismonth_rain, thismonth_rad = two_nums(line)
    if c == 0:
        prev_rain = thismonth_rain
        prev_rad = thismonth_rad
    else:
        if not (thismonth_rain < prev_rain and thismonth_rad < prev_rad):
            rain_rad_dec = False
            break
    c = c + 1

if rain_rad_dec == True:
    print("Los datos tienen sospecha de error")