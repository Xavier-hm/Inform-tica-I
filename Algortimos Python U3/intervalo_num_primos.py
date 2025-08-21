#Algoritmo para imprimir un determinado intervalo de números primos

inicio = int(input("Ingrese el número inicial del intervalo: "))

final = int(input("Ingrese el número final del intervalo: "))

num = inicio

while num <= final:
    esPrimo = True
    if num <= 1:
        esPrimo = False
    else:
        divisor = 2
        while divisor < num and esPrimo:
            if num % divisor == 0:
                esPrimo = False
            
            divisor = divisor + 1
    
    if esPrimo:
        print(num)
    
    num = num + 1