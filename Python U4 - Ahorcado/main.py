from ahorcado import *
# Juego de ahorcado

# Introduzca aqui las instrucciones para el juego
print("Este es el clasico juego del ahorcado\nTienes 8 intentos por ronda\nSolo tienes permitido usar espacios y letras (la ñ no esta disponible)")
# Despliegue de la entrada
printIntro('intro.txt')

# Variables globales
letrasIntentadas=''
numeroIntentos = 8
otraVez = 'y'

# Variables extras
palabrasAdivinadas = 0
palabrasIntentadas = 0

while otraVez == 'y':
	''' Inicio ciclo de nuevo juego '''
	# Selección del modo de juego (1: palabra secreta, 2: archivo)
	ModoDeJuego = input("**SELECCION DEL MODO DE JUEGO**\n1. Ingresar palabra secreta\n2. Seleccionar de un archivos\nSeleccione una opción: ")
	while True:
		if ModoDeJuego == "1":
			palabraSecreta = inputSecret()
			break

		elif ModoDeJuego == "2":
			palabras = loadWords("superHeroes.txt")
			separador = ","
			conta = countWords(palabras,separador)
			palabraSecreta = pickWord(palabras,separador)
			break
		
		else:
			ModoDeJuego = input("**SELECCION DEL MODO DE JUEGO**\n1. Ingresar palabra secreta\n2. Seleccionar de un archivos\nSeleccione una opción: ")
	
		
	# ...
	ban = 1 # Bandera que indica la culminación de una tanda de turnos
			# ya sea por que el usuario acierta o por que pierde
			
	# Impresión de las estadísticas (Numero de intentos, letras disponibles, palabra secreta (rayas))
	print("--------------------")
	print("Usted tiene ", numeroIntentos, "intentos disponibles")
	print("Letras disponibles: ", obtenerLetrasDisponibles(letrasIntentadas))
	print("Palabra secreta:", obtenerParteAdivinada(palabraSecreta, letrasIntentadas) )
	
	# ...
	while ban == 1:
		''' Inicio ciclo para adivinar la palabra oculta '''
		# Solicitud interactiva de letras
		letraIngresada = input("Por favor ingrese una letra teniendo en cuenta las letras disponibles: ")
		letraIngresada = letraIngresada.lower()
		
		# Verificación de la letra
		if letraIngresada in palabraSecreta and letraIngresada not in letrasIntentadas:
			print("Letra acertada")

		elif letraIngresada not in obtenerLetrasDisponibles(letrasIntentadas) and letraIngresada not in letrasIntentadas:
			print("Letra no disponible")

		elif verificarLetraIngresada(letraIngresada, letrasIntentadas):
			print("La letra ya fue ingresada, por favor intente con otra letra")

		elif letraIngresada not in palabraSecreta:
			print("Letra fallada")
			numeroIntentos = numeroIntentos - 1
		
		# Actualiza letras intentadas
		if not verificarLetraIngresada(letraIngresada, letrasIntentadas):
			letrasIntentadas = letrasIntentadas + letraIngresada
			
		
		# Impresión del estado del juego (Número de intentos, letras disponibles)
		print("--------------------")
		print("Usted tiene ", numeroIntentos, " disponibles")
		print("Letras disponibles: ", obtenerLetrasDisponibles(letrasIntentadas))
		print("Palabra secreta:", obtenerParteAdivinada(palabraSecreta, letrasIntentadas) )
		
		# Verificación de la condición de finalización del juego
		if palabraAdivinada(palabraSecreta,letrasIntentadas):
			ban = 0
			fin = True
		elif numeroIntentos == 0:
			ban = 0
			fin = False
		else:
			ban = 1
		
		# ...
		''' Fin ciclo para adivinar la palabra oculta '''
	palabrasIntentadas = palabrasIntentadas + 1
	if fin == True:
		print("Felicitaciones, la palabra secreta es:", palabraSecreta)	
		palabrasAdivinadas = palabrasAdivinadas + 1
	else:
		print(f"Has perdido, la palabra secreta era: {palabraSecreta}. Animo!")
	# Inicializar nuevamente las variables que crea necesario...
	letrasIntentadas=''
	numeroIntentos = 8
	# Solicitud de nuevo juego
	otraVez = input('Desea jugar otra vez (y/n): ')  
	otraVez = otraVez.lower()
	''' Fin ciclo de nuevo juego '''