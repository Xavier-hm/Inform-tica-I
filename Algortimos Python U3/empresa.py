#Algoritmo para calcular el salario semanal del usuario de acuerdo al numero de horas trabjadas y a la sucursal a la que pertenece

horas = int(input("Ingrese el número de horas trabajadas: "))

sucursal = input("Ingrese el nombre de la sucursal donde trabaja: ") #Las sucursales son A y B (debe elegir alguna de las dos)

if sucursal == "A":
    if horas <= 40:
        salarioA = (horas*10)
    else:
        horas_extras = horas - 40
        salarioA = (40*10)+(horas_extras*20)
    print("Su salario semanal son: ", salarioA)
else:
    if horas <= 45:
        salarioB = (horas*12)
    else:
        horas_extras = horas - 45
        salarioB =(45*12)+(horas_extras*25)
    print("Su salario semanal son: ", salarioB)
