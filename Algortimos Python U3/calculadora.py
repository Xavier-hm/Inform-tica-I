#Algoritmo para procesar diferentes calculos entre dos números

a = float(input("Ingrese el valor A: "))

b = float(input("Ingrese el valor de B: "))

operador = int(input("Ingrese operador: ")) #Los operadores son: 1- Multiplicación, 2- Residuo A/B, 3- A^B, 4- Mayor de los dos números, 5- Salir

if operador == 1:
    multiplicacion = a * b
    print("El valor de la multiplicación es : ", multiplicacion)
elif operador == 2:
    residuo = a % b
    print("El valor del residuo es: ", residuo)
elif operador == 3:
    potencia = a ** b
    print("El valor de la potencia es: ", potencia)
elif operador == 4:
    if a > b:
        print("El mayor de los valores es: ", a)
    else:
        print("El mayor de los valoress es: ", b)
else:
    if operador == 5:
        print("Fin")
    else:
        while operador != 5:
            operador = int(input('Ingresa un valor para operador: '))
print("Fin")