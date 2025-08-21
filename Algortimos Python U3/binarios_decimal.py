#Con este algortimo pordrá convertir nímeros binarios a decimales

binario = int(input("Ingrese un número binario: "))

decimal = 0

posicion = 0

while binario > 0:
    digito = binario%10

    decimal = decimal + digito * (2**posicion)

    binario = binario // 10

    posicion = posicion + 1

print("El número decimal es: ", decimal)