#Algoritmo para calcular la cantidad de digitos en un número ingresado

num = int(input("Ingrese un número: "))

c = 0

while num >= 1:
    num = num/10
    c = c+1

print("El número ingresado tiene", c, "digitos")