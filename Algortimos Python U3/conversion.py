#Algoritmo para convertir velocidades en mph a km/h y a m/s 

mph = int(input("Ingrese su velocidad en mph: "))

km = mph * 1609
ms = km * 1000/(3600)


print(mph, "mi/h equivalen a ", km, "km/h y a ", ms, "m/s.")