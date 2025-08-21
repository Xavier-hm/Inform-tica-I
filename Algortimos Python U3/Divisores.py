#Algoritmo para calcular los divisores del número ingresado

x = int(input("Ingresar un número: "))

c = 145

while c <= x:
    if x%c == 0:
        print("Es divisible por: ", c)
    
    c = c+1
