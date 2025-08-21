# -*- coding: utf-8 -*-

from funciones import *
archivo = 'notas_estudiantes.csv'
archivo_matriculados = 'hist_matriculados.csv'
cursos = []
documentos_estudiantes = []
notas = []


print("Menú Principal:")
print("1. Eliminar estudiante")
print("2. Agregar estudiante")
print("3. Promedio de estudiantes")
print("4. Promedio de cursos")
print("5. Tres notas mayores")
print("6. Menor nota de estudiante")
print("7. Ordenar promedios estudiantes")
print("8. Ordenar estudiantes por cantidad de cursos")
print('9. Predecir estudiantes matriculados')
print('10. Salir')
print()

cursos, documentos_estudiantes, notas = cargar_datos(archivo)

while True:
    opcion = input("Selecciona una opción: ")     
    
    if opcion == '1':
        documento = input("Introduce el número de documento del estudiante a eliminar: ")
        if eliminar_estudiante(documento, documentos_estudiantes, notas):
            actualizar_archivo(archivo, cursos, documentos_estudiantes, notas)
            print("Estudiante eliminado correctamente.")
        else:
            print("Estudiante no encontrado.")
        
    elif opcion == '2':
        documento = input("Introduce el número de documento del nuevo estudiante: ")
        nuevas_notas = list(map(float, input("Introduce las notas del estudiante separadas por comas: ").split(',')))
        agregar_estudiante(documento, nuevas_notas, documentos_estudiantes, notas)
        actualizar_archivo(archivo, cursos, documentos_estudiantes, notas)
        print("Estudiante agregado correctamente.")
        
    elif opcion == '3':
        promedios = promedio_estudiantes(notas)
        for doc, prom in zip(documentos_estudiantes, promedios):
            print(f"Estudiante {doc}: Promedio {prom:.2f}")
        
    elif opcion == '4':
        promedios = promedio_cursos(notas)
        for curso, prom in zip(cursos, promedios):
            print(f"Curso {curso}: Promedio {prom:.2f}")

        
    elif opcion == '5':
        curso = input("Introduce el nombre del curso: ")
        if curso in cursos:
            curso_idx = cursos.index(curso)
            try:
                mejores = tres_notas_mayores(curso_idx, documentos_estudiantes, notas)
                for nota, doc in mejores:
                    print(f"Estudiante {doc}: Nota {nota}")
            except IndexError as e:
                print(str(e))
        else:
            print("Curso no encontrado.")
        
    elif opcion == '6':
        documento = input("Introduce el número de documento del estudiante: ")
        curso_idx, menor_nota = menor_nota_estudiante(documento, documentos_estudiantes, notas)
        if curso_idx is not None:
            print(f"El curso con la menor nota es {cursos[curso_idx]} con una nota de {menor_nota}")
        else:
            print("Estudiante no encontrado.")
        
    elif opcion == '7':
        estudiantes_promedios = ordenar_promedios_estudiantes(documentos_estudiantes, notas)
        for prom, doc in estudiantes_promedios:
            print(f"Estudiante {doc}: Promedio {prom:.2f}")
        
    elif opcion == '8':
        estudiantes_cursos = ordenar_estudiantes_por_cantidad_cursos(documentos_estudiantes, notas)
        for cant, doc in estudiantes_cursos:
            print(f"Estudiante {doc}: Cantidad de cursos {cant}")

    elif opcion == '9':
        opcion_predecir_matriculados()
    
    elif opcion == '10':
        break
