#Ingrese el tamaño de la base del triangulo

base = int(input("Ingrese el tamaño del patron: "))

i = 1

while i <= base:
    j = 1

    while j <= base-i:
        print(" ", end="")
        j = j + 1

    j = 1

    while j <= i:
        print(j, " ", end="")
        j = j + 1

    print()

    i = i + 1




