#Algortimo para visualizar la cantidad de digitos de la serie Fibonacci que el usuario desee

n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci que desea ver: "))

num1 = 0

num2 = 1

print("Serie de Fibonacci: ")
print(num1)

if n > 1:
    print(num2)

contador = 3

while contador <= n:
    num_siguiente = num1 + num2
    print(num_siguiente)

    num1 = num2
    num2 = num_siguiente

    contador = contador + 1
