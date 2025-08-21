import json
import csv
from datetime import datetime, timedelta
from utilidades import *

while True:
    limpiar_pantalla()
    print("\n=== SISTEMA DE MONITOREO CLIMÁTICO ===")
    print("1. Usuario Registrado")
    print("2. Usuario Visitante")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    limpiar_pantalla()

    if opcion == "1":
        rol = login()
        if rol == "administrador":
            while True:
                print("\n=== MENÚ ADMINISTRADOR ===")
                print("1. Gestionar Estaciones")
                print("2. Gestionar Usuarios")
                print("3. Depurar registros")
                print("4. Volver al menú principal")

                opcion = input("Elija una opción (1-4): ")

                if opcion == "1":
                    while True:
                        print("\n=== GESTIONAR ESTACIONES ===")
                        print("1. Crear Estación")
                        print("2. Editar Estación")
                        print("3. Eliminar Estación")
                        print("4. Regresar")

                        opcion = input("Seleccione una opción: ")

                        if opcion == "1":
                            crear_estacion()
                        elif opcion == "2":
                            editar_estacion()
                        elif opcion == "3":
                            eliminar_estacion()
                        elif opcion == "4":
                            break
                        else:
                            print("Seleccione una opción valida")
                elif opcion == "2":
                    while True:
                        print("\n=== GESTIONAR USUARIOS ===")
                        print("1. Crear Usuario")
                        print("2. Editar Usuario")
                        print("3. Eliminar Usuario")
                        print("4. Regresar")
                        
                        opcion = input("Seleccione una opción: ")
                        
                        if opcion == "1":
                            registrar_nuevo_usuario()
                        elif opcion == "2":
                            editar_usuario()
                        elif opcion == "3":
                            eliminar_usuario()
                        elif opcion == "4":
                            break
                        else:
                            print("Opción no válida. Por favor elija 1, 2 o 3")
                elif opcion == "3":
                    depurar_registros()
                else:
                    print("Ingrese una opción valida")
        elif rol == "operador":
            while True:
                print("\n=== MENÚ OPERADOR ===")
                print("1. Seleccionar estación")
                print("2. Volver al menú principal")

                opcion = input("Elija una opción (1-2): ")

                if opcion == "1":
                    estacion_seleccionada = seleccionar_estacion()
                    if estacion_seleccionada:
                        while True:
                            print("\n=== OPCIONES PARA LA ESTACIÓN ===")
                            print("1. Mostrar mediciones")
                            print("2. Ingresar mediciones")
                            print("3. Volver al menú operador")
                    
                            opcion_estacion = input("Elija una opción (1-3): ")
                    
                            if opcion_estacion == "1":
                                mostrar_mediciones(estacion_seleccionada)
                            elif opcion_estacion == "2":
                                ingresar_mediciones(estacion_seleccionada)
                            elif opcion_estacion == "3":
                                break
                            else:
                                print("Opción no válida. Intente de nuevo.")
                else:
                    print("Opción no válida. Intente de nuevo")

    elif opcion == "2":
            print("\n=== VISUALIZAR ESTADÍSTICAS ===")

    # Obtener lista de variables disponibles
    with open('variables.json', 'r') as archivo:
        variables = json.load(archivo)['variables']

    # Pedir selección de periodo de tiempo
    while True:
        print("\nSeleccione el periodo de tiempo a evaluar:")
        print("1. Últimos 7 días")
        print("2. Últimos 30 días")
        print("3. Elegir fechas manualmente")

        opcion_periodo = input("Ingrese el número de opción (1-3): ")

        if opcion_periodo == "1":
            fecha_inicio = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
            fecha_fin = datetime.now().strftime('%Y-%m-%d')
            break
        elif opcion_periodo == "2":
            fecha_inicio = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            fecha_fin = datetime.now().strftime('%Y-%m-%d')
            break
        elif opcion_periodo == "3":
            while True:
                fecha_inicio = input("Ingrese la fecha de inicio (yyyy-mm-dd): ")
                if validar_fecha(fecha_inicio):
                    break
            while True:
                fecha_fin = input("Ingrese la fecha de fin (yyyy-mm-dd): ")
                if validar_fecha(fecha_fin):
                    break
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    # Pedir selección de variables
    print("\nSeleccione las variables a analizar:")
    for i, (variable, config) in enumerate(variables.items(), 1):
        print(f"{i}. {variable} ({config['unidades']})")
    
    variables_seleccionadas = []
    while True:
        seleccion = input("Ingrese los números de las variables separados por comas (0 para finalizar): ")
        if seleccion == "0":
            break
        try:
            opciones = [int(x) for x in seleccion.split(',')]
            for opcion in opciones:
                if 1 <= opcion <= len(variables):
                    variables_seleccionadas.append(list(variables.keys())[opcion-1])
                else:
                    print(f"Opción {opcion} no válida. Intente de nuevo.")
            break
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

    # Pedir modo de visualización
    while True:
        print("\nSeleccione el modo de visualización:")
        print("1. Visualizar por pantalla")
        print("2. Guardar en archivo de texto")

        opcion_visualizacion = input("Ingrese el número de opción (1-2): ")

        if opcion_visualizacion == "1":
            mostrar_estadisticas(fecha_inicio, fecha_fin, variables_seleccionadas)
            break
        elif opcion_visualizacion == "2":
            guardar_estadisticas(fecha_inicio, fecha_fin, variables_seleccionadas)
            break
        else:
            print("Opción no válida. Intente de nuevo.")






