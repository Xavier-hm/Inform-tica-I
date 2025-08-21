# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:10:41 2024

@author: nicko
"""
from funciones import*
archivo= 'notas_estudiantes.csv'
codigos_cursos, documentos_estudiantes, notas = cargar_datos(archivo)

def ordenar_promedios_estudiantes(documentos, notas):
    promedios = promedio_estudiantes(notas)
    estudiantes_promedios = list(zip(promedios, documentos))

    # Algoritmo de burbuja para ordenar estudiantes por promedio
    n = len(estudiantes_promedios)
    iteraciones = 0
    for i in range(n):
        for j in range(0, n-i-1):
            iteraciones += 1  # Incrementar el contador en cada iteración
            if estudiantes_promedios[j][0] < estudiantes_promedios[j+1][0]:
                estudiantes_promedios[j], estudiantes_promedios[j+1] = estudiantes_promedios[j+1], estudiantes_promedios[j]

    print(f"Iteraciones en ordenar_promedios_estudiantes: {iteraciones}")

def ordenar_estudiantes_por_cantidad_cursos(documentos_estudiantes, notas):
    cantidad_cursos = [sum(1 for nota in estudiante if nota >= 0) for estudiante in notas]
    estudiantes_cursos = list(zip(cantidad_cursos, documentos_estudiantes))

    # Algoritmo de selección para ordenar estudiantes por cantidad de cursos
    n = len(estudiantes_cursos)
    iteraciones = 0
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            iteraciones += 1  # Incrementar el contador en cada iteración
            if estudiantes_cursos[j][0] > estudiantes_cursos[max_idx][0]:
                max_idx = j
        estudiantes_cursos[i], estudiantes_cursos[max_idx] = estudiantes_cursos[max_idx], estudiantes_cursos[i]

    print(f"Iteraciones en ordenar_estudiantes_por_cantidad_cursos: {iteraciones}")

def merge_sort(arr, key, contador):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        contador = merge_sort(left_half, key, contador)
        contador = merge_sort(right_half, key, contador)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            contador += 1  # Incrementar contador en cada comparación
            if left_half[i][key] > right_half[j][key]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            contador += 1  # Incrementar contador en cada comparación
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            contador += 1  # Incrementar contador en cada comparación
            arr[k] = right_half[j]
            j += 1
            k += 1

    return contador

def ordenar_promedios_estudiantes_optimizada(documentos, notas):
    contador = 0  # Inicializar el contador
    promedios = promedio_estudiantes(notas)
    estudiantes_promedios = list(zip(promedios, documentos))

    # Aplicar Merge Sort en estudiantes_promedios basado en el promedio (índice 0)
    contador = merge_sort(estudiantes_promedios, 0, contador)
    
    print(f"Iteraciones en ordenar_promedios_estudiantes_optimizada: {contador}")
    

def ordenar_estudiantes_por_cantidad_cursos_optimizada(documentos_estudiantes, notas):
    contador = 0  # Inicializar el contador
    cantidad_cursos = [sum(1 for nota in estudiante if nota >= 0) for estudiante in notas]
    estudiantes_cursos = list(zip(cantidad_cursos, documentos_estudiantes))

    # Aplicar Merge Sort en estudiantes_cursos basado en la cantidad de cursos (índice 0)
    contador = merge_sort(estudiantes_cursos, 0, contador)
    
    print(f"Iteraciones en ordenar_estudiantes_por_cantidad_cursos_optimizada: {contador}")
print(ordenar_promedios_estudiantes_optimizada(documentos_estudiantes, notas))    
print(ordenar_promedios_estudiantes(documentos_estudiantes, notas))
print(ordenar_estudiantes_por_cantidad_cursos_optimizada(documentos_estudiantes, notas))
print(ordenar_estudiantes_por_cantidad_cursos(documentos_estudiantes, notas))