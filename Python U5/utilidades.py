# -*- coding: utf-8 -*-
import csv
import json
from datetime import datetime

def login():
    documento = input("Usuario: ")
    contrasena = input("Contrasena: ")
    limpiar_pantalla()


# Abrimos y leemos el archivo
    archivo = open('usuarios.csv', 'r')
    lineas = archivo.readlines()

# Se salta la primera línea que tiene los títulos y se revisa cada usuario

    for linea in lineas[1:]: # El [1:] es para saltar la primera línea
        # Quitamos espacios y saltos de línea con strip() y separamos por coma son split(',)
        
        datos = linea.strip().split(',')

        # Si encontramos el usuario y la contraseña

        if datos[0] == documento and datos[2] == contrasena:
            rol = datos[3].lower()
            archivo.close()
            print(f"¡Login exitoso! Bienvenido/a {datos[1]}")
            return rol
    archivo.close()
    print("Usuario o contraseña incorrectos")

    return None

def validar_documento(documento):
    '''
    Valida un número de documento. Debe contener 10 caracteres, todos numéricos.
    
    Argumentos:
        documento: string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    # verificamos que solo contenga números y tenga 10 caracteres
    if not documento.isdigit() or len(documento) != 10: # isdigit() se usa para verificar si todos los caracteres de una cadena son valores numéricos
        print("Error: El documento debe contener exactamente 10 números")
        return False
    
    archivo = open('usuarios.csv', 'r')

    for linea in archivo:
        datos = linea.strip().split(',')
        if datos[0] == documento: # El documento es el primer campo
            archivo.close()
            print("Error: Este documento ya está registrado")
            return False
    archivo.close()
    return True

def validar_nombre(nombre):
    '''
    Valida nombre válido (solo letras y espacios)
    Argumentos:
        nombre: String a validar
    return -> Boolean (True or False) si es valido o no
    '''
    # Quitamos espacios al inicio y final
    nombre = nombre.strip()

    # Verificamos que no esté vacio
    if len(nombre) == 0:
        print("Error: El nombre no puede estar vacío")
        return False
    
    # Verificamos que solo contenga letras y espacios
    for char in nombre:
        if not (char.isalpha() or char.isspace()): # isalpha() para verificar si todos los caracteres de una cadena son letras del alfabeto, en mayúsculas o minúsculas
            print("Error: El nombre solo puede contener letras y espacios") # isspace() se utiliza para determinar si todos los caracteres de una cadena son espacios en blanco
            return False
    return True

def validar_contrasena(contrasena):
    '''
    Valida la contraseña del usuario. Debe contener 4 caracteres.
    
    Argumentos:
        contraseña: string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    if len(contrasena) < 4:
        print("Error: La contraseña debe contener al menos 4 caracteres.")
        return False
    return True

def registrar_nuevo_usuario():
    print("\n === REGISTRO DE NUEVO USUARIO ===")

    # 1. Pedir y validar documento
    while True:
        documento = input("Ingrese el documento (10 números): ")
        if validar_documento(documento):
            break

    # 2. Pedir y validar nombre
    while True:
        nombre = input("Ingrese nombre completo: ")
        if validar_nombre(nombre):
            break

    # 3. Pedir y validar contraseña
    while True:
        contrasena = input("Ingrese contraseña (mínimo 4 caracteres): ")
        if not validar_contrasena(contrasena):
            continue # continue sirve para omitir el código restante en un bucle durante la iteración actual

        confirmacion = input("Confirme la contraseña: ")
        if contrasena != confirmacion:
            print("Error: Las contraseñas no coinciden")
            continue
        break

    # 4. Pedir y validar rol
    while True:
        print("\nSeleccione el rol:")
        print("1. Administrador")
        print("2. Operador")
        rol = input("Ingrese el número de opción (1 o 2): ")

        if rol == "1":
            rol = "Administrador"
            break
        elif rol == "2":
            rol = "Operador"
            break
        else:
            print("Error: Opción no válida")

    # 5. Guardar el usuario en el archivo
    archivo = open('usuarios.csv', 'a')

    #Escribir los datos del nuevo usuario
    archivo.write(f"{documento},{nombre},{contrasena},{rol}\n")
    archivo.close()

    print("\n¡Usuario registrado exitosamente!")
    print(f"Documento: {documento}")
    print(f"Nombre: {nombre}")
    print(f"Rol: {rol}")

def listar_usuarios():
    """Muestra la lista de usuarios y retorna la lista de datos"""
    usuarios = []
    archivo = open('usuarios.csv', 'r')
    # Saltamos la línea de títulos
    next(archivo) # devuelve el siguiente elemento del iterador que se incluye como primer argumento

    print("\n=== LISTA DE USUARIOS ===")
    numero = 1
    for linea in archivo:
        datos = linea.strip().split(',')
        usuarios.append(datos)
        print(f"{numero}. Documento: {datos[0]}")
        print(f"    Nombre: {datos[1]}")
        print(f"    Rol: {datos[3]}")
        print("-" * 30)
        numero += 1

    archivo.close()
    return usuarios

def editar_usuario():
    print("\n=== EDITAR USUARIO ===")

    # 1. Mostrar lista de usuarios y obtener selección
    usuarios = listar_usuarios()
    if not usuarios:
        return
    
    while True:
        try: # para capturar y manejar excepciones que ocurren durante la ejecución de un programa
            seleccion = int(input("\nIngrese el número del usuario a editar: "))
            if 1 <= seleccion <= len(usuarios):
                break
            else:
                print("Error: Número de usuario no válido")
        except ValueError:
            print("Error: Debe ingresar un número")

    # Obtener datos del usuario seleccionado
    usuario = usuarios[seleccion - 1]
    documento = usuario[0] # El documento no se puede editar
    nombre_actual = usuario[1]
    contrasena_actual = usuario[2]
    rol_actual = usuario[3]

    # 2. Editar nombre
    print(f"\nNombre actual: {nombre_actual}")
    while True:
        nuevo_nombre = input("Ingrese el nuevo nombre (o Enter para mantener el actual): ")
        if nuevo_nombre == "":
            nuevo_nombre = nuevo_nombre
            break
        if validar_nombre(nuevo_nombre):
            break

    # 3. Editar contraseña
    print(f"\nContraseña actual: {contrasena_actual}")
    while True:
        nueva_contrasena = input("Ingrese la nueva contraseña (o Enter para mantener la actual): ")
        if nueva_contrasena == "":
            nueva_contrasena = contrasena_actual
            break
            
        if not validar_contrasena(nueva_contrasena):
            continue
            
        confirmacion = input("Confirme la nueva contraseña: ")
        if nueva_contrasena != confirmacion:
            print("Error: Las contraseñas no coinciden")
            continue
        break

    # 4. Editar rol
    print(f"\nRol actual: {rol_actual}")
    while True:
        print("\nSeleccione el nuevo rol:")
        print("1. Administrador")
        print("2. Operador")
        print("3. Mantener rol actual")
        
        opcion_rol = input("Ingrese el número de opción: ")
        
        if opcion_rol == "1":
            nuevo_rol = "Administrador"
            break
        elif opcion_rol == "2":
            nuevo_rol = "Operador"
            break
        elif opcion_rol == "3":
            nuevo_rol = rol_actual
            break
        else:
            print("Error: Opción no válida")

    # 5. Guardar los cambios
    # Primero leemos todo el archivo
    archivo = open('usuarios.csv', 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    # Abrimos el archivo para escribir
    archivo = open('usuarios.csv', 'w')
    # Escribimos la línea de títulos
    archivo.write(lineas[0])
    
    # Escribimos todas las líneas, actualizando el usuario editado
    for i, linea in enumerate(lineas[1:], 1):
        datos = linea.strip().split(',')
        if datos[0] == documento:
            # Esta es la línea del usuario que estamos editando
            archivo.write(f"{documento},{nuevo_nombre},{nueva_contrasena},{nuevo_rol}\n")
        else:
            # Las demás líneas las escribimos sin cambios
            archivo.write(linea)

    archivo.close()
    
    print("\n¡Usuario actualizado exitosamente!")
    print(f"Documento: {documento}")
    print(f"Nuevo nombre: {nuevo_nombre}")
    print(f"Nuevo rol: {nuevo_rol}")

def eliminar_usuario():
    """
    Función que permite eliminar un usuario del sistema.
    
    La función hace lo siguiente:
    1. Muestra la lista de usuarios
    2. Pide seleccionar cuál eliminar
    3. Pide confirmación
    4. Elimina el usuario del archivo CSV
    
    No permite:
    - Eliminar el último administrador
    - Eliminar el último usuario del sistema
    """
    print("\n=== ELIMINAR USUARIO ===")
    
    # Mostrar la lista de usuarios numerada
    usuarios = listar_usuarios()
    
    # Si no hay usuarios, terminar
    if not usuarios:
        print("No hay usuarios para eliminar")
        return
    
    # Pedir y validar el número de usuario a eliminar
    while True:
        seleccion = input("\nIngrese el número del usuario a eliminar (0 para cancelar): ")
        
        # Verificar si quiere cancelar
        if seleccion == "0":
            print("Operación cancelada")
            return
        
        # Verificar que sea un número válido
        if not seleccion.isdigit():
            print("Por favor ingrese un número válido")
            continue
        
        seleccion = int(seleccion)
        
        # Verificar que el número esté en el rango de usuarios
        if seleccion < 1 or seleccion > len(usuarios):
            print(f"Por favor ingrese un número entre 1 y {len(usuarios)}")
            continue
            
        break
    
    # Obtener el usuario seleccionado
    usuario_elegido = usuarios[seleccion - 1]
    
    # Verificar que no sea el último usuario
    if len(usuarios) == 1:
        print("Error: No se puede eliminar el último usuario del sistema")
        return
    
    # Verificar que no sea el último administrador
    if usuario_elegido[3].lower() == "administrador":
        # Contar cuántos administradores hay
        cantidad_admins = 0
        for usuario in usuarios:
            if usuario[3].lower() == "administrador":
                cantidad_admins += 1
        
        if cantidad_admins == 1:
            print("Error: No se puede eliminar el último administrador")
            return
    
    # Mostrar datos del usuario a eliminar y pedir confirmación
    print(f"\nUsuario seleccionado:")
    print(f"Documento: {usuario_elegido[0]}")
    print(f"Nombre: {usuario_elegido[1]}")
    print(f"Rol: {usuario_elegido[3]}")
    
    confirmar = input("\n¿Está seguro de eliminar este usuario? (s/n): ")
    if confirmar.lower() != "s":
        print("Operación cancelada")
        return
    
    # Eliminar el usuario del archivo
    # 1. Leer todo el archivo
    archivo = open('usuarios.csv', 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    # 2. Escribir todo de nuevo, menos el usuario eliminado
    archivo = open('usuarios.csv', 'w')
    archivo.write(lineas[0])  # Escribir la primera línea (encabezados)
    
    for linea in lineas[1:]:  # Para cada línea excepto la primera
        datos = linea.strip().split(',')
        # Si no es el usuario a eliminar, escribir la línea
        if datos[0] != usuario_elegido[0]:
            archivo.write(linea)
            
    archivo.close()
    
    print(f"\nUsuario {usuario_elegido[1]} eliminado exitosamente")

def validar_nombre_estacion(nombre):
    """
    Valida que el nombre de la estación no esté vacío y solo contenga caracteres válidos.
    
    Args:
        nombre (str): Nombre de la estación a validar
        
    Returns:
        bool: True si el nombre es válido, False si no lo es
    """
    # Quitar espacios al inicio y final
    nombre = nombre.strip()
    
    # Verificar que no esté vacío
    if len(nombre) == 0:
        print("Error: El nombre no puede estar vacío")
        return False
        
    return True

def obtener_ultimo_codigo():
    """
    Obtiene el último código usado en el archivo de estaciones.
    
    Returns:
        int: El último código usado (0 si no hay estaciones)
    """
    archivo = open('estaciones.csv', 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    if len(lineas) <= 1:  # Si solo está el encabezado o está vacío
        return 0
        
    # Obtener el último código
    ultima_linea = lineas[-1].strip().split(',')
    return int(ultima_linea[0])

def crear_estacion():
    """
    Permite crear una nueva estación.
    - Genera un código automático
    - Pide y valida el nombre de la estación
    - Guarda la estación en el archivo CSV
    """
    print("\n=== CREAR ESTACIÓN ===")
    
    # Generar nuevo código
    ultimo_codigo = obtener_ultimo_codigo()
    nuevo_codigo = ultimo_codigo + 1
    
    # Pedir y validar nombre
    while True:
        nombre = input("Ingrese el nombre de la estación: ")
        if validar_nombre_estacion(nombre):
            break
    
    # Guardar la nueva estación
    archivo = open('estaciones.csv', 'a')
    archivo.write(f"{nuevo_codigo},{nombre}\n")
    archivo.close()
    
    print("\n¡Estación creada exitosamente!")
    print(f"Código: {nuevo_codigo}")
    print(f"Nombre: {nombre}")

def listar_estaciones():
    """
    Muestra la lista de estaciones y retorna la lista de datos.
    
    Returns:
        list: Lista donde cada elemento es una lista con [codigo, nombre]
    """
    estaciones = []
    archivo = open('estaciones.csv', 'r')
    # Saltamos la línea de títulos
    next(archivo)
    
    print("\n=== LISTA DE ESTACIONES ===")
    numero = 1
    for linea in archivo:
        datos = linea.strip().split(',')
        estaciones.append(datos)
        print(f"{numero}. Código: {datos[0]}")
        print(f"   Nombre: {datos[1]}")
        print("-" * 30)
        numero += 1
    
    archivo.close()
    return estaciones

def editar_estacion():
    """
    Permite editar el nombre de una estación existente.
    - Muestra la lista de estaciones
    - Permite seleccionar una estación
    - Permite modificar el nombre manteniendo el código
    - Guarda los cambios en el archivo
    """
    print("\n=== EDITAR ESTACIÓN ===")
    
    # Obtener lista de estaciones
    estaciones = listar_estaciones()
    
    # Verificar si hay estaciones
    if len(estaciones) == 0:
        print("No hay estaciones registradas")
        return
    
    # Pedir selección de estación
    while True:
        seleccion = input("\nIngrese el número de la estación a editar (0 para cancelar): ")
        
        # Verificar si quiere cancelar
        if seleccion == "0":
            print("Operación cancelada")
            return
            
        # Verificar que sea un número
        if not seleccion.isdigit():
            print("Por favor ingrese un número válido")
            continue
            
        seleccion = int(seleccion)
        
        # Verificar que esté en el rango
        if seleccion < 1 or seleccion > len(estaciones):
            print(f"Por favor ingrese un número entre 1 y {len(estaciones)}")
            continue
            
        break
    
    # Obtener estación seleccionada
    estacion = estaciones[seleccion - 1]
    
    # Mostrar datos actuales
    print(f"\nEstación seleccionada:")
    print(f"Código: {estacion[0]}")
    print(f"Nombre actual: {estacion[1]}")
    
    # Pedir y validar nuevo nombre
    while True:
        nuevo_nombre = input("\nIngrese el nuevo nombre: ")
        if validar_nombre_estacion(nuevo_nombre):
            break
    
    # Guardar los cambios
    archivo = open('estaciones.csv', 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    archivo = open('estaciones.csv', 'w')
    # Escribir encabezado
    archivo.write(lineas[0])
    
    # Escribir datos actualizados
    for linea in lineas[1:]:
        datos = linea.strip().split(',')
        if datos[0] == estacion[0]:
            archivo.write(f"{estacion[0]},{nuevo_nombre}\n")
        else:
            archivo.write(linea)
    
    archivo.close()
    
    print(f"\n¡Estación actualizada exitosamente!")
    print(f"Código: {estacion[0]}")
    print(f"Nuevo nombre: {nuevo_nombre}")

def eliminar_estacion():
    """
    Permite eliminar una estación del registro, siempre y cuando no tenga registros asociados.
    
    1. Muestra la lista de estaciones
    2. Pide al usuario seleccionar una estación a eliminar
    3. Verifica que no tenga registros asociados
    4. Elimina la estación del archivo CSV
    """
    print("\n=== ELIMINAR ESTACIÓN ===")
    
    # Obtener lista de estaciones
    estaciones = listar_estaciones()
    
    # Verificar si hay estaciones
    if len(estaciones) == 0:
        print("No hay estaciones registradas")
        return
    
    # Pedir selección de estación
    while True:
        seleccion = input("\nIngrese el número de la estación a eliminar (0 para cancelar): ")
        
        # Verificar si quiere cancelar
        if seleccion == "0":
            print("Operación cancelada")
            return
            
        # Verificar que sea un número
        if not seleccion.isdigit():
            print("Por favor ingrese un número válido")
            continue
            
        seleccion = int(seleccion)
        
        # Verificar que esté en el rango
        if seleccion < 1 or seleccion > len(estaciones):
            print(f"Por favor ingrese un número entre 1 y {len(estaciones)}")
            continue
        
        # Obtener la estación seleccionada
        estacion = estaciones[seleccion - 1]
        
        # Verificar que no tenga registros asociados
        if tiene_registros_asociados(estacion[0]):
            print(f"La estación '{estacion[1]}' tiene registros asociados, no se puede eliminar.")
            continue
        
        break
    
    # Eliminar la estación del archivo CSV
    archivo = open('estaciones.csv', 'r')
    lineas = archivo.readlines()
    archivo.close()
    
    archivo = open('estaciones.csv', 'w')
    archivo.write(lineas[0])  # Escribir la primera línea (encabezados)
    
    for linea in lineas[1:]:
        datos = linea.strip().split(',')
        if datos[0] != estacion[0]:
            archivo.write(linea)
    
    archivo.close()
    
    print(f"\n¡Estación '{estacion[1]}' eliminada exitosamente!")

def tiene_registros_asociados(codigo_estacion):
    """
    Verifica si una estación tiene registros asociados en el archivo de registros.
    
    Args:
        codigo_estacion (str): Código de la estación a verificar
        
    Returns:
        bool: True si tiene registros asociados, False en caso contrario
    """
    with open('registros.json', 'r') as archivo:
        registros = json.load(archivo)
    
    return str(codigo_estacion) in registros

def depurar_registros():
    """
    Función que compara dos archivos de registros climáticos y muestra:
    1. Los registros que aparecen en ambos archivos
    2. Todos los registros únicos sin duplicados
    """
    # Paso 1: Leer los archivos JSON
    # Leer archivo original
    with open('registros.json', 'r') as archivo1:
        registros_1 = json.load(archivo1)
    
    # Leer archivo versión 2
    with open('registros_v2.json', 'r') as archivo2:
        registros_2 = json.load(archivo2)
    
    # Paso 2: Crear listas para almacenar los registros
    registros_lista_1 = []  # Lista para registros del primer archivo
    registros_lista_2 = []  # Lista para registros del segundo archivo
    
    # Paso 3: Extraer los registros del primer archivo
    for estacion in registros_1:
        for medicion in registros_1[estacion]:  # PM10, PM25, etc
            for fecha in registros_1[estacion][medicion]:
                # Guardar cada registro como una tupla con su información
                registro = (estacion, medicion, fecha,str(registros_1[estacion][medicion][fecha]))
                registros_lista_1.append(registro)
    
    # Paso 4: Extraer los registros del segundo archivo
    for estacion in registros_2:
        for medicion in registros_2[estacion]:
            for fecha in registros_2[estacion][medicion]:
                registro = (estacion, medicion, fecha, str(registros_2[estacion][medicion][fecha]))
                registros_lista_2.append(registro)
    
    # Paso 5: Convertir las listas a conjuntos para usar operaciones de conjuntos
    conjunto_1 = set(registros_lista_1)
    conjunto_2 = set(registros_lista_2)
    
    # Paso 6: Encontrar registros comunes (intersección)
    registros_comunes = conjunto_1.intersection(conjunto_2)
    
    # Paso 7: Encontrar todos los registros únicos (unión)
    todos_registros = conjunto_1.union(conjunto_2)
    
    # Paso 8: Mostrar los resultados
    
    # Mostrar registros comunes
    print("\n=== REGISTROS QUE APARECEN EN AMBOS ARCHIVOS ===")
    if len(registros_comunes) == 0:
        print("No hay registros comunes")
    else:
        for registro in registros_comunes:
            print(f"\nEstación: {registro[0]}")
            print(f"Tipo de medición: {registro[1]}")
            print(f"Fecha: {registro[2]}")
            print(f"Valores: {registro[3]}")
    
    # Mostrar todos los registros únicos
    print("\n=== TODOS LOS REGISTROS SIN DUPLICADOS ===")
    if len(todos_registros) == 0:
        print("No hay registros")
    else:
        for registro in todos_registros:
            print(f"\nEstación: {registro[0]}")
            print(f"Tipo de medición: {registro[1]}")
            print(f"Fecha: {registro[2]}")
            print(f"Valores: {registro[3]}")
            
    input("\nPresione Enter para continuar...")

def seleccionar_estacion():
    print("\n=== SELECCIONAR ESTACIÓN ===")
    
    # Obtener lista de estaciones
    estaciones = listar_estaciones()
    
    # Verificar si hay estaciones
    if len(estaciones) == 0:
        print("No hay estaciones registradas")
        return None
    
    # Pedir selección de estación
    while True:
        seleccion = input("\nIngrese el número de la estación (0 para cancelar): ")
        
        # Verificar si quiere cancelar
        if seleccion == "0":
            print("Operación cancelada")
            return None
            
        # Verificar que sea un número
        if not seleccion.isdigit():
            print("Por favor ingrese un número válido")
            continue
            
        seleccion = int(seleccion)
        
        # Verificar que esté en el rango
        if seleccion < 1 or seleccion > len(estaciones):
            print(f"Por favor ingrese un número entre 1 y {len(estaciones)}")
            continue
            
        break
    
    # Obtener la estación seleccionada
    estacion_seleccionada = estaciones[seleccion - 1]
    
    print(f"\nEstación seleccionada: {estacion_seleccionada[1]} (Código {estacion_seleccionada[0]})")
    return estacion_seleccionada

def mostrar_mediciones(estacion):
    print(f"\n=== MEDICIONES PARA LA ESTACIÓN {estacion[1]} ===")
    
    # Cargar registros desde el archivo JSON
    with open('registros.json', 'r') as archivo:
        registros = json.load(archivo)

    # Verificar si la estación tiene registros
    if str(estacion[0]) in registros:
        estacion_registros = registros[str(estacion[0])]
        tabla = []
        encabezado = ['Fecha', 'PM10', 'PM25', 'Temperatura', 'Humedad']

        # Crear un diccionario para consolidar las mediciones por fecha
        mediciones_por_fecha = {}

        # Recorrer cada variable y sus fechas asociadas
        for variable, fechas in estacion_registros.items():
            for fecha, valores in fechas.items():
                if fecha not in mediciones_por_fecha:
                    mediciones_por_fecha[fecha] = {}
                # Si los valores existen, tomar el primero de la lista; de lo contrario, 'ND'
                mediciones_por_fecha[fecha][variable] = valores[0] if valores else 'ND'

        # Construir las filas para la tabla
        for fecha in sorted(mediciones_por_fecha.keys()):
            fila = [fecha]
            for variable in ['PM10', 'PM25', 'Temperatura', 'Humedad']:
                valor = mediciones_por_fecha[fecha].get(variable, 'N/A')
                # Convertir '-999' a 'ND' para la visualización
                fila.append("ND" if valor == -999 else valor)
            tabla.append(fila)

        # Imprimir la tabla
        imprimir_tabla(tabla, [20, 10, 10, 10, 10], encabezado)
    else:
        print(f"No hay registros disponibles para la estación {estacion[1]} (Código {estacion[0]}).")



def ingresar_mediciones(estacion):
    print(f"\n=== INGRESAR MEDICIONES PARA LA ESTACIÓN {estacion[1]} ===")
    
    # Cargar variables del archivo JSON
    with open('variables.json', 'r') as archivo:
        variables = json.load(archivo)['variables']
    
    # Obtener fecha actual
    fecha = datetime.now().strftime('%Y-%m-%d')
    
    # Inicializar un diccionario para almacenar las mediciones de cada variable
    mediciones = {}
    for variable, config in variables.items():
        while True:
            valor_str = input(f"Ingrese el valor de {variable} ({config['unidades']}): ")
            if valor_str.lower() == 'nd':
                valor = -999
                break
            try:
                valor = float(valor_str)
                if config['minimo'] <= valor <= config['maximo']:
                    break
                else:
                    print(f"Error: El valor debe estar entre {config['minimo']} y {config['maximo']} {config['unidades']}")
            except ValueError:
                print("Error: Debe ingresar un número válido o 'ND'")
        mediciones[variable] = valor

    # Cargar registros del archivo JSON
    with open('registros.json', 'r') as archivo:
        registros = json.load(archivo)
    
    # Asegurar que la estación exista en los registros
    if str(estacion[0]) not in registros:
        registros[str(estacion[0])] = {}
    
    # Actualizar registros para cada variable
    for variable, valor in mediciones.items():
        # Asegurar que la variable exista en los registros de la estación
        if variable not in registros[str(estacion[0])]:
            registros[str(estacion[0])][variable] = {}
        
        # Agregar o actualizar la lista de mediciones para la fecha
        if fecha not in registros[str(estacion[0])][variable]:
            registros[str(estacion[0])][variable][fecha] = []
        
        registros[str(estacion[0])][variable][fecha].append(valor)

    # Guardar los registros actualizados
    with open('registros.json', 'w') as archivo:
        json.dump(registros, archivo, indent=4)
    
    print("\n¡Mediciones ingresadas exitosamente!")

def mostrar_estadisticas(fecha_inicio, fecha_fin, variables):
    """
    Muestra las estadísticas (máximo, mínimo, promedio) de las variables seleccionadas
    en el período de tiempo indicado.
    """
    print("\n=== ESTADÍSTICAS ===")
    print(f"Periodo: {fecha_inicio} - {fecha_fin}")

    # Cargar registros desde el archivo JSON
    with open('registros.json', 'r') as archivo:
        registros = json.load(archivo)

    # Iterar por cada variable seleccionada
    for variable in variables:
        print(f"\nVariable: {variable}")

        valores = []
        maximos = []
        minimos = []

        # Recorrer todas las estaciones
        for estacion, datos in registros.items():
            # Comprobar si la variable existe en los datos de la estación
            if variable in datos:
                # Recorrer las fechas de la variable
                for fecha, lista_valores in datos[variable].items():
                    if fecha_inicio <= fecha <= fecha_fin:
                        for valor in lista_valores:  # Considerar cada valor en la lista
                            if valor != -999:  # Ignorar valores no disponibles
                                valores.append((valor, estacion, fecha))
                                # Verificar máximos
                                if not maximos or valor > maximos[0][0]:
                                    maximos = [(valor, estacion, fecha)]
                                elif valor == maximos[0][0]:
                                    maximos.append((valor, estacion, fecha))
                                # Verificar mínimos
                                if not minimos or valor < minimos[0][0]:
                                    minimos = [(valor, estacion, fecha)]
                                elif valor == minimos[0][0]:
                                    minimos.append((valor, estacion, fecha))

        # Mostrar estadísticas si hay valores
        if valores:
            maximo_valor = maximos[0]
            minimo_valor = minimos[0]
            promedio = sum(v[0] for v in valores) / len(valores)
            print(f"\n  Máximo: {maximo_valor[0]} en estación {maximo_valor[1]} el {maximo_valor[2]}")
            print(f"  Mínimo: {minimo_valor[0]} en estación {minimo_valor[1]} el {minimo_valor[2]}")
            print(f"  Promedio: {promedio:.2f}")
        else:
            print("  No hay datos disponibles para esta variable en el rango de fechas especificado.")

    input("\nPresione Enter para continuar...")



def guardar_estadisticas(fecha_inicio, fecha_fin, variables):
    """
    Guarda las estadísticas (máximo, mínimo, promedio) de las variables seleccionadas
    en el período de tiempo indicado en el archivo 'Estadisticas.txt'.
    """
    print("\n=== GUARDANDO ESTADÍSTICAS EN ARCHIVO ===")

    # Abrir el archivo para escritura
    with open('Estadisticas.txt', 'w') as archivo:
        archivo.write(f"Periodo: {fecha_inicio} - {fecha_fin}\n\n")

        # Cargar registros desde el archivo JSON
        with open('registros.json', 'r') as registros_file:
            registros = json.load(registros_file)

        # Iterar por cada variable seleccionada
        for variable in variables:
            archivo.write(f"Variable: {variable}\n")
            
            valores = []
            maximos = []
            minimos = []

            # Recorrer todas las estaciones
            for estacion, datos in registros.items():
                # Comprobar si la variable existe en los datos de la estación
                if variable in datos:
                    # Recorrer las fechas de la variable
                    for fecha, lista_valores in datos[variable].items():
                        if fecha_inicio <= fecha <= fecha_fin:
                            for valor in lista_valores:  # Procesar cada valor en la lista
                                if valor != -999:  # Ignorar valores no disponibles
                                    valores.append((valor, estacion, fecha))
                                    # Verificar máximos
                                    if not maximos or valor > maximos[0][0]:
                                        maximos = [(valor, estacion, fecha)]
                                    elif valor == maximos[0][0]:
                                        maximos.append((valor, estacion, fecha))
                                    # Verificar mínimos
                                    if not minimos or valor < minimos[0][0]:
                                        minimos = [(valor, estacion, fecha)]
                                    elif valor == minimos[0][0]:
                                        minimos.append((valor, estacion, fecha))

            # Escribir estadísticas si hay valores
            if valores:
                maximo_valor = maximos[0]
                minimo_valor = minimos[0]
                promedio = sum(v[0] for v in valores) / len(valores)
                archivo.write(f"  Máximo: {maximo_valor[0]} en estación {maximo_valor[1]} el {maximo_valor[2]}\n")
                archivo.write(f"  Mínimo: {minimo_valor[0]} en estación {minimo_valor[1]} el {minimo_valor[2]}\n")
                archivo.write(f"  Promedio: {promedio:.2f}\n\n")
            else:
                archivo.write("  No hay datos disponibles para esta variable en el rango de fechas especificado.\n\n")

    print("Estadísticas guardadas en el archivo 'Estadisticas.txt'.")
    input("\nPresione Enter para continuar...")

def validar_fecha(fecha):
    """
    Valida si una fecha tiene el formato YYYY-MM-DD y si es una fecha válida.

    Parámetros:
        fecha_str (str): La fecha en formato de cadena.

    Retorna:
        bool: True si la fecha es válida y está en formato correcto, False en caso contrario.
    """
    try:
        # Intentamos convertir la cadena a una fecha con el formato especificado
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        # Si ocurre un error, la fecha no cumple el formato o no es válida
        return False

def limpiar_pantalla():
    '''
    Imprime varias líneas en blanco, para dar la ilusión 
    de limpiar la pantalla
    '''
    print('\n'*20)

def imprimir_tabla(tabla, ancho, encabezado=None):  
    ''' 
    Imprime en pantalla un tabla con los datos pasados, ajustado a los tamaños deseados.
    
    Argumentos:
        tabla: Lista que representa la tabla. Cada elemento es una fila
        ancho: Lista con el tamaño deseado para cada columna. Si se especifica
            un entero, todas las columnas quedan de ese tamaño
        encabezado: Lista con el encabezado de la tabla
    '''
    def dividir_fila(ancho,sep='-'):
        '''
        ancho: Lista con el tamaño de cada columna
        se: Caracter con el que se van a formar las líneas que 
            separan las filas
        '''
        linea = ''
        for i in range(len(ancho)):
            linea += ('+'+sep*(ancho[i]-1))
        linea = linea[:-1]+'+'
        print(linea)
        
    def imprimir_celda(texto, impresos, relleno):
        '''
        texto: Texto que se va a colocar en la celda
        impresos: cantidad de caracteres ya impresos del texto
        relleno: cantidad de caracteres que se agregan automáticamente,
            para separar los textos del borde de las celda.
        '''        
        # Imprimir celda
        if type(texto) == type(0.0):
            #print(texto)
            texto = '{:^7.2f}'.format(texto)
            #print(type(texto), texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n',' ').replace('\t',' ')
        if impresos+relleno < len(texto):
            print(texto[impresos:impresos+relleno],end='')
            impresos+=relleno
        elif impresos >= len(texto):
            print(' '*(relleno),end='')
        else:
            print(texto[impresos:], end='')
            print(' '*(relleno-(len(texto) - impresos)),end='')
            impresos = len(texto)
        return impresos
    
    def imprimir_fila(fila):
        '''
        fila: Lista con los textos de las celdas de la fila
        '''
        impresos = []   
        alto = 1
        for i in range(len(fila)):
            impresos.append(0)
            if type(fila[i]) == type(0.0):
                texto = '{:7.2f}'.format(fila[i])
            else:
                texto = str(fila[i])
            alto1 = len(texto)//(ancho[i]-4)
            if len(texto)%(ancho[i]-4) != 0:
                alto1+=1
            if alto1 > alto:
                alto = alto1
        for i in range(alto):
            print('| ',end='')
            for j in range(len(fila)):
                relleno = ancho[j]-3
                if j == len(fila)-1:
                    relleno = ancho[j] -4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' |')
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' | ',end='')   
    if not len(tabla) > 0:
        return
    if not type(tabla[0]) is list:
        return
    ncols = len(tabla[0])
    if type(ancho) == type(0):
        ancho = [ancho+3]*ncols 
    elif type(ancho) is list:
        for i in range(len(ancho)):
            ancho[i]+=3
    else:
        print('Error. El ancho debe ser un entero o una lista de enteros')
        return
    assert len(ancho) == ncols, 'La cantidad de columnas no coincide con los tamaños dados'
    ancho[-1] += 1
    if encabezado != None:
        dividir_fila(ancho,'=')
        imprimir_fila(encabezado)
        dividir_fila(ancho,'=')
    else:
        dividir_fila(ancho)
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)