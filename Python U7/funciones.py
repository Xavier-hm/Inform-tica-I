# -*- coding: utf-8 -*-
from plots import plot_data
import csv
import numpy as np

def cargar_datos(archivo):
    """
    Carga datos de un archivo CSV.

    Parámetros:
    - archivo: Ruta del archivo a cargar
    
    Retorna:
    - cursos: Lista de nombres de cursos
    - documentos_estudiantes: Lista de documentos de estudiantes
    - notas: Lista de notas de cada estudiante
    """
    with open(archivo, 'r') as file:
        lineas = file.readlines()

    if len(lineas) < 3:
        raise ValueError("El archivo debe contener al menos tres líneas: cursos, documentos y notas.")
    
    #La primera línea contiene los nombres de los cursos
    cursos = lineas[0].strip().split(',')

    #La segunda linea contiene los documentos de los estudiantes
    documentos_estudiantes = lineas[1].strip().split(',')

    #Las líneas restantes contienen la nota de cada estudiante
    notas = [list(map(float, linea.strip().split(','))) for linea in lineas[2:]]

    if len(documentos_estudiantes) != len(notas):
        raise ValueError("La cantidad de documentos no coincide con la cantidad de registros de notas.")
    
    return cursos, documentos_estudiantes, notas

def eliminar_estudiante(documento, documentos, notas):
    """
    Elimina un estudiante de la lista de estudiantes y sus notas.
    
    Parámetros:
    - documento: Número de documento del estudiante a eliminar
    - documentos: Lista de documentos de estudiantes
    - notas: Lista de notas de estudiantes
    
    Retorna:
    - True si el estudiante fue eliminado, False si no se encontró
    """
    if documento in documentos:
        index = documentos.index(documento)
        documentos.pop(index)
        notas.pop(index)
        return True
    else:
        return False


def agregar_estudiante(documento, nuevas_notas, documentos_estudiantes, notas):
    """
    Agrega un nuevo estudiante con sus notas.
    
    Parámetros:
    - documento: Número de documento del nuevo estudiante
    - nuevas_notas: Lista de notas del nuevo estudiante
    - documentos_estudiantes: Lista de documentos de estudiantes
    - notas: Lista de notas de estudiantes
    """
    documentos_estudiantes.append(documento)
    notas.append(nuevas_notas)
    
def promedio_cursos(notas):
    """
    Calcula el promedio de cada curso.
    
    Parámetros:
    - notas: Lista de notas de todos los estudiantes
    
    Retorna:
    - Lista de promedios de cada curso
    """
    num_cursos = len(notas[0])  # Se asume que todos los estudiantes tienen el mismo número de cursos
    promedios = []
    
    for i in range(num_cursos):
        suma = 0
        cantidad = 0
        for estudiante in notas:
            nota = estudiante[i]
            if nota >= 0:  # Solo consideramos notas válidas
                suma += nota
                cantidad += 1
        
        if cantidad > 0:
            promedios.append(suma / cantidad)
        else:
            promedios.append(0)  # Si no hay notas válidas, el promedio será 0

    return promedios


def promedio_estudiantes(notas):
    """
    Calcula el promedio de notas de cada estudiante.
    
    Parámetros:
    - notas: Lista de notas de todos los estudiantes
    
    Retorna:
    - Lista de promedios de cada estudiante
    """
    promedios = []
    for estudiante in notas:
        notas_validas = [nota for nota in estudiante if nota >= 0]
        if notas_validas:
            promedio = sum(notas_validas) / len(notas_validas)
        else:
            promedio = 0
        promedios.append(promedio)
    return promedios
    
def menor_nota_estudiante(documento, documentos_estudiantes, notas):
    if documento in documentos_estudiantes:
        idx = documentos_estudiantes.index(documento)
        notas_estudiante = notas[idx]
        menor_nota = min([nota for nota in notas_estudiante if nota >= 0])
        curso_idx = notas_estudiante.index(menor_nota)
        return curso_idx, menor_nota
    else:
        return None, None
    
def tres_notas_mayores(curso_idx, documentos_estudiantes, notas):

    if curso_idx < 0 or curso_idx >= len(notas[0]):
        raise ValueError("El índice del curso no existe")

    curso_notas = [(notas[i][curso_idx], documentos_estudiantes[i]) for i in range(len(notas)) if notas[i][curso_idx] >= 0]
    
    
    n = len(curso_notas)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if curso_notas[j][0] > curso_notas[max_idx][0]:
                max_idx = j
        curso_notas[i], curso_notas[max_idx] = curso_notas[max_idx], curso_notas[i]
    
    return curso_notas[:3]
    


def obtener_cantidad_cursos(estudiante):
    return estudiante[0]

def ordenar_promedios_estudiantes(documentos, notas):
    promedios = promedio_estudiantes(notas)
    estudiantes_promedios = list(zip(promedios, documentos))

    # Algoritmo de burbuja para ordenar estudiantes por promedio
    n = len(estudiantes_promedios)
    for i in range(n):
        for j in range(0, n-i-1):
            if estudiantes_promedios[j][0] < estudiantes_promedios[j+1][0]:
                estudiantes_promedios[j], estudiantes_promedios[j+1] = estudiantes_promedios[j+1], estudiantes_promedios[j]
    
    return estudiantes_promedios

def ordenar_estudiantes_por_cantidad_cursos(documentos_estudiantes, notas):
    cantidad_cursos = [sum(1 for nota in estudiante if nota >= 0) for estudiante in notas]
    estudiantes_cursos = list(zip(cantidad_cursos, documentos_estudiantes))

    # Algoritmo de selección para ordenar estudiantes por cantidad de cursos
    n = len(estudiantes_cursos)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if estudiantes_cursos[j][0] > estudiantes_cursos[max_idx][0]:
                max_idx = j
        estudiantes_cursos[i], estudiantes_cursos[max_idx] = estudiantes_cursos[max_idx], estudiantes_cursos[i]

    return estudiantes_cursos

def actualizar_archivo(archivo, cursos, documentos_estudiantes, notas):
    with open(archivo, 'w') as file:
        file.write(','.join(cursos) + '\n')
        file.write(','.join(documentos_estudiantes) + '\n')
        for estudiante in notas:
            file.write(','.join(map(str, estudiante)) + '\n')

def cargar_datos_historicos(archivo):
    """
    Carga datos históricos de matriculados desde un archivo CSV
    
    Parámetros:
    - archivo: Ruta del archivo CSV
    
    Retorna:
    - Lista de datos históricos y lista de años
    """
    datos = []
    years = []
    with open(archivo, 'r') as file:
        next(file)  # Saltar encabezado
        for linea in csv.reader(file):
            year = int(linea[0])
            estudiantes = int(linea[1])
            datos.append([year, estudiantes])
            years.append(year)
    return datos, years

def calcular_regresion_lineal(datos):
    """
    Calcula los parámetros de regresión lineal por tanteo
    
    Parámetros:
    - datos: Lista de datos históricos
    
    Retorna:
    - a, b: Parámetros de la regresión
    - mejor_mae: Error mínimo
    """
    mejor_mae = float('inf')
    mejor_a, mejor_b = 0, 0
    
    # Rango de prueba para a y b
    for a in np.linspace(0.1, 10, 500):
        for b in np.linspace(-10000, 50, 500):
            errores = []
            for x, y in datos:
                y_pred = a * x + b
                errores.append(abs(y - y_pred))
            
            mae = np.mean(errores)
            
            if mae < mejor_mae:
                mejor_mae = mae
                mejor_a = a
                mejor_b = b
    
    return mejor_a, mejor_b, mejor_mae

def predecir_matriculados(a, b, anio):
    """
    Predice número de matriculados para un año
    
    Parámetros:
    - a, b: Parámetros de regresión
    - anio: Año a predecir
    
    Retorna:
    - Número estimado de estudiantes
    """
    return round(a * anio + b)

def opcion_predecir_matriculados():
    """
    Opción del menú para predecir matriculados
    """
    # Cargar datos históricos
    datos, years = cargar_datos_historicos(archivo='hist_matriculados.csv')
    
    # Calcular regresión
    a, b, mae = calcular_regresion_lineal(datos)
    
    # Solicitar año de predicción
    while True:
        try:
            anio = int(input("Introduce un año futuro para predecir estudiantes: "))
            if anio <= max(years):
                print("El año debe ser mayor a los años históricos.")
                continue
            break
        except ValueError:
            print("Introduce un año válido.")
    
    # Calcular valores de regresión
    regression_line = [a * x + b for x in years]
    prediccion = predecir_matriculados(a, b, anio)
    
    # Preparar datos para graficar
    nuevos_datos = datos + [[anio, prediccion]]
    nuevos_years = years + [anio]
    
    # Graficar
    plot_data(nuevos_datos, regression_line + [prediccion], nuevos_years)
    
    # Mostrar resultados
    print(f"\nPredicción para {anio}: {prediccion} estudiantes")
    print(f"Error del modelo (MAE): {mae:.2f}")
    print(f"Ecuación de regresión: y = {a:.2f}x + {b:.2f}")









