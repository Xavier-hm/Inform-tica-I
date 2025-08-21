#Algortimo para verificar la seguridad de una contraseña siguiendo las siguientes condiciones:
#Su longitud debe estar entre 8 y 20 caracteres.
# Debe incluir letras, números.
# Debe incluir al menos uno de los siguientes caracteres especiales:
#!, ”, #, $, %, &, /, (, ), =, ?, +, *
# No debe ser palíndroma.

password = input(">>Ingrese una contraseña valida: ")

es_valida = True

if len(password) < 8 or len(password)> 20:
    print("Longitud correcta: ERROR")
    es_valida = False
else:
    print("Longitud correcta: OK")

tiene_numero = False
tiene_letra = False

for char in password:
    if char in "0123456789":
        tiene_numero = True
    if char in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz":
        tiene_letra = True

if tiene_letra and tiene_numero:
    print("Incluye letras y números: OK")
else:
    print("Incluye letras y números: ERROR")

for caracter in password:
    if caracter in "!,=?+*%/#":
        print("Incluye caracteres especiales: OK")
        break
else:
    print("Incluye caracteres especiales: ERROR")
    es_valida = False

password_clean = password.lower()

if password_clean == password_clean[::-1]:
    print("No es palíndroma: ERROR")
    es_valida = False
else:
    print("No es palíndroma: OK")

if es_valida:
    print("La contraseña se ha creado satisfactoriamente!!!")
else:
    print("La contraseña no cumple con todos los requisitos!!!")