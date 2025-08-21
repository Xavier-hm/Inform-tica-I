#Algoritmo para calcular la hipotenusa de un triangulo rectangulo

c_opuesto = float(input("Ingresar el  valor del cateto opuesto: "))

c_adyacente = float(input("Ingresar el valor del cateto adyacente: "))

hipotenusa = c_opuesto**2 + c_adyacente**2

hipotenusa = hipotenusa**0.5

print("El valor de la hipotenusa es igual a: ", hipotenusa)