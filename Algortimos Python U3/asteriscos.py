filas = int(input("Ingrese el número de filas para la piramide: "))

i = 1

while i <= filas:
    espacio = 1
    while espacio <= filas-i:
        print(" ", end="")
        espacio = espacio+1
    
    j = 1
    while j<=i:
        print("*", end="")
        j = j+1
    
    print()

    i = i+1


