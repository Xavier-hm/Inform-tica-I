#Ingrese una oración para cambiar los espacios “ ” por un guión “-”

oracion = input("Ingrese una oración: ")

oracion_guiones = ""

for caracter in oracion:
    if caracter == " ":
        oracion_guiones += "-"
    else:
        oracion_guiones += caracter

print(oracion_guiones)