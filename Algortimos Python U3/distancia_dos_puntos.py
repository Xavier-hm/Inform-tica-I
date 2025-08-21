#Este algoritmo le permitirá calcular la distancia entre dos punto del plano cartesiano

x1 = int(input("Ingrese el valor de x1: "))

x2 = int(input("Ingrese el valor de x2: "))

y1 = int(input("Ingrese el valor de y1: "))

y2 = int(input("Ingrese el valor de y2: "))

print("Coordenadas del punto 1: " "(", x1, ",", y1, ")" " Coordenadas del punto 2: " "(" ,x2, "," ,y2, ")")

distancia = (x2-x1)**2 + (y2-y1)**2

distancia = distancia**0.5

print("La distancia entre los puntos 1 y 2 es: ", distancia)