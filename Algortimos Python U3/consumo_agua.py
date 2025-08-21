#Este algortimo le permitirá saber el valor a pagar respecto a su consumo de agua

agua = int(input("Ingresar la cantidad de agua consumida en metros cubicos: "))

estrato = int(input("Ingrese su estrato: "))

if agua > 13:
    total = (agua*9)+50

elif agua > 10:
    total = (agua*5)+50

else:
    total = (agua*6)+50

if estrato < 3:
    total = total - (total*0.2)
    print("El valor total a pagar es : ", total)

else: 
    print("El valor total a pagar es : ", total)