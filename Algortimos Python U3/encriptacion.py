#Algoritmo para encriptar mensajes

#Solicitar mensaje al usuario
msg = input("Ingresa mensaje: ")

#Inicializamos una variable para almacenar el mensaje a encriptar
msg_encriptado = ""

#Inicializamos dos variables para almacenar los caracteres pares e impares
pares = ""
impares = ""

#Inicializamos una variable para formar la palabra actual
palabra_actual = ""

#Se crea un ciclo para recorrer el mensaje

for indice in range(len(msg)):
    char = msg[indice]
    #Si se encuentra un espacio o se llega al final del mensaje, procesamos la palabra
    if char == ' ' or indice == len(msg) - 1:
        #Si es el último carácter y no es un espacio, se añade a la palabra actual
        if char != ' ':
            palabra_actual += char
        #Procesar la palabra actual
        for i in range(len(palabra_actual)):
            letra = palabra_actual[i]
            #Verificamos si el carácter es uan vocal y la cambiamos por su respectiva posición
            if letra == 'a':
                letra = '1'
            elif letra == 'e':
                letra = '2'
            elif letra == 'i':
                letra = '3'
            elif letra == 'o':
                letra = '4'
            elif letra == 'u':
                letra = '5'
            #Si el índice es par, añadimos el carácter a la cadena de pares
            if i % 2 == 0:
                pares += letra
            else:
                #Si el indice es impar, añadimos el carácter a la cadena de impares
                impares += letra
        msg_encriptado += pares + impares + " "
        #Reiniciamos las variables para la siguiente palabra
        palabra_actual = ""
        pares = ""
        impares = ""
    else:
        #Si no es un espacio, se añade el carácter a la palabra actual
        palabra_actual += char
#Mostrar el mensaje encriptado
print("Mensaje encriptado: ", msg_encriptado)