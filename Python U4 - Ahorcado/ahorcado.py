def printIntro(fileName):
    '''
    Firma:
        (string) -> ()
    
    Sinopsis:
        función que imprime el contenido de un archivo en pantalla, en este 
		caso, el mensaje de bienvenida al juego

    Entradas y salidas:
        - inputFile: Nombre del archivo que contiene la presentación del juego
        - returns: None, solo imprime el archivo leído en pantalla
        
    Ejemplos de uso:
        
        >>> printIntro("intro.txt")
        ___  _                             _             +---+ 
       / _ \| |                           | |            |   | 
      / /_\ \ |__   ___  _ __ ___ __ _  __| | ___        O   |    
      |  _  | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \      /|\  |    
      | | | | | | | (_) | | | (_| (_| | (_| | (_) |     / \  |
      \_| |_/_| |_|\___/|_|  \___\__,_|\__,_|\___/           |  
                                                      =========
    '''

    archivo = open(fileName)
    for linea in archivo:
        print(linea,end="")
    archivo.close()
    

def inputSecret():
    '''
    Firma:
        () -> (string)
    
    Sinopsis:
        Función que solicita al usuario la palabra secreta
        
    Entradas y salidas:
        - inputs: None
        - returns: string con la palabra secreta ingresada por el usuario
        
    Ejemplos de uso:
        
        >>> p = inputSecret()
        Ingrese la palabra o frase oculta: UdeA
        
        >>> print(p)
        UdeA 
    '''

    pSec = input("Ingrese la palabra o frase oculta: ")
    pSec = pSec.lstrip()
    pSec = pSec.rstrip()
    pSec = pSec.lower()
    
    palabraCorrecta = 0
    while pSec != None:        
        for letra in pSec:
            if not letra in "abcdefghijklmnopqrstuvwxyz ":
                palabraCorrecta = 1
        if palabraCorrecta == 0:
            return pSec
        else:
            pSec = input("Ingrese una palabra o frase con caracteres permitidos: ")
            pSec = pSec.lstrip()
            pSec = pSec.rstrip()
            pSec = pSec.lower()
            palabraCorrecta = 0


def loadWords(fileName):
    '''
    Firma:
        (string) -> (string)
        
    Sinopsis:
        Función que solicita el nombre de un archivo cualquiera y devuelve una cadena 
        de caracteres con su contenido
        
    Entradas y salidas:
        - filename: string que contiene el nombre del archivo con las palabras secretas
        - returns: string con todas las palabras secretas
        
    Ejemplos de uso:
        >>> loadWords("superHeroes.txt")
        'capitan centella, capitan planeta, batman, superman, robin, mujer maravilla, aquaman, flash,
        cyborg, capitan marciano, linterna verde,flash gordon, liga de la justicia, defensores de la 
        tierra, el fantasma, spider man, hulk, thor, iron man, los vengadores, robocop, terminator, 
        capitan america, hombre hormiga, la avispa, goku, vegeta, gohan, piccolo, trunks, spawn, 
        tintin, ghost rider, blade, tortugas ninja, soldado del invierno, el castigador, 
        el predicador, leonidas, kick ass, el comediante, el chapulin colorado, wolverine,
        flecha verde, el profesor super o, los autobots, robin hood\n'
        
    '''

    palabras = open(fileName)
    palabras = palabras.read()    
    
	# Cadena retornada
    return palabras

def countWords(palabras,separador):
    '''
    Firma:
        (string,string) -> (int)
        
    Sinopsis:
        Función que cuenta la cantidad de palabras disponibles en una cadena
        
    Entradas y salidas:
        - palabras: Conjunto de palabras o frases separadas por un delimitador
        - separador: Delimitador que separa una palabra o frase de otra dentro de la cadena de entrada (palabras)
        - returns: cantidad de palabras secretas
        
    Ejemplos de uso:
        >>> materias = 'español,calculo,geometria vectorial,geometria euclidiana'
        >>> countWords(materias,',')
        4
        
        >>> countWords('gallo-gallina','-')
        2
        '''
    if palabras[-1] != separador:
        palabras = palabras + separador
    conta = 0
    for letra in palabras:
        if letra == separador:
            conta = conta + 1

	# Retorno de la cantidad de palabras	
    return conta   
   
def pickWord(palabras,separador):
    '''
    Firma:
        (string,string) -> (string)
        
    Sinopsis:
        Función que permite seleccionar una palabra o frase secreta correspondiente a una posicion 
        dada de un conjunto de palabras separadas por un delimitador.  
    
    Entradas y salidas:
        - palabras: Conjunto de palabras o frases secretas separadas por un delimitador
        - separador: Delimitador que separa una palabra o frase secreta de otra
        - returns: Palabra o frase de la posiciónon elegida
        
    Ejemplos de uso:
        >>> x = 'homero_marge_bart_lisa_maggie' 
        >>> pickWord(x,'_')
        'homero'
        
        >>> palabra = pickWord('marcos, lucas, mateo, juan',',')
        >>> print(palabra)
        'mateo'
        
    '''
    
    import random
    numerorandom = random.randint(0,countWords(palabras,separador)-1)
    contador = 0
    if palabras[-1] != separador:
        palabras = palabras + separador
    palabra = ""
    for letra in palabras:
        if letra == separador:
            if contador == numerorandom:
                # Eliminación de espacios de la palabra...
                palabra = palabra.lstrip()
                palabra = palabra.rstrip()
                palabra = palabra.lower()
    
                # Retorno de la palabra elegida
                return palabra
            contador = contador + 1
            palabra = ""
        else:
            palabra = palabra + letra

def obtenerParteAdivinada(palabraSecreta,letrasIntentadas):
    '''
    Firma:
        (string,string) -> (string)
        
    Sinopsis:
        Imprime la parte de la cadena que ha sido adivinada.  
        
    Entradas y salidas:
        - palabraSecreta: string, palabra que el usuario esta adivinando
        - letrasIntentadas: string, letras intentadas por el usuario para adivinar la palabra
        - returns: string, compuesto de letras y caracteres raya bajo que representan las letras aun no adivinadas
        
    Ejemplos de uso:
        >>> palabraSecreta = 'perro'
        >>> letrasIntentadas = 'aeiousp'
        >>> print obtenerParteAdivinada(palabraSecreta, letrasIntentadas)
        'p e _ _ o'
        
        >>> obtenerParteAdivinada('frodo', '')
        '_ _ _ _ _'  
        
    '''

    pPrint = ""
    for letra in palabraSecreta:
        if letra in letrasIntentadas:
            pPrint = pPrint + " " + letra
        else:
            pPrint = pPrint + " _"

    # Retorno de la palabra elegida
    return pPrint      
    
def obtenerLetrasDisponibles(letrasIntentadas):
    '''
    Firma:
        (string) -> (string)
        
    Sinopsis:
        Devuelve las letras que no se han empleado en los turnos.  
        
    Entradas y salidas:
        - letrasIntentadas: string, letras intentadas por el usuario para adivinar la palabra
        - returns: string, compuesto de letras que no han sido ingresado
        
    Ejemplos de uso:
        >>> letrasIntentadas = 'abfs'
        >>> print obtenerLetrasDisponibles(letrasIntentadas)
        cdeghijklmnopqrtuvwxyz
    
    '''

    import string
    resto = ""
    for letra in string.ascii_lowercase+" ":
        if letra not in letrasIntentadas:
            resto = resto + letra        
	# Retorno de las letras del alfabeto que aun no han sido usadas
    return resto

def verificarLetraIngresada(letra,letrasIntentadas):
    '''
    Firma:
        (string,string) -> (bool)
        
    Sinopsis:
        Devuelve True si la letra ingresada se encuentra dentro del string de letras intentadas.  
        
    Entradas y salidas:
        - letra: Letra a verificar
        - letrasIntentadas: String con las letras a comparar
        - returns: La función devuelve False si la letra no se encuentra en ninguna de la 
        lista. En caso contrario, devuelve True.
    
    Ejemplos de uso:
        >>> letrasIntentadas = 'abfs'
        >>> verificarLetraIngresada('z',letrasIntentadas)
        False
        
        >>> verificarLetraIngresada('x','vwxyz')
        True
        
    '''
    
    # Desarrolle el cuerpo de la función aquí... 
    if letra in letrasIntentadas:
        return True
    else:
        return False
    
def palabraAdivinada(palabra,letrasIntentadas):
    '''
    Firma:
        (string,string) -> (bool)
        
    Sinopsis:
        Determina si con las letras ingresadas se puede formar la palabra secreta.
        
    Entradas y salidas:
        - palabra: Palabra o frase a verificar
        - letrasIntentadas: String con las letras a comparar
        - returns: Devuelve True si todas las letras de palabra se encuentran en letrasIntentadas, False en caso contrario.

    Ejemplos de uso:
        >>> palabraAdivinada('bilbo','bsnlio')
        True
        
        >>> palabraAdivinada('karman','cam')
        False
        
    '''
    numletrasenpalabra = 0
    numletrasenletrasintentadas = 0
    for letra in palabra:
        numletrasenpalabra = numletrasenpalabra + 1

    for letra in palabra:
        if letra in letrasIntentadas:
            numletrasenletrasintentadas = numletrasenletrasintentadas + 1

    if numletrasenletrasintentadas == numletrasenpalabra:
       return True
    else:
        return False
