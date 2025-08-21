#Escriba un carácter (es decir, un string de longitud 1) y determine si
#el carácter es vocal, consonante o un dígito. Además, para las vocales y consonantes determine
#si es mayúscula o minúscula.

caracter = input("Escriba un caracter: ")

if caracter in "aeiou":
    print("Vocal - Minúscula")
elif caracter in "AEIOU":
    print("Vocal - Mayúscula")
elif caracter in "bcdfghjklmnñpqrstvwxyz":
    print("Consonante - Minúscula")
elif caracter in "BCDFGHJKLMNÑPQRSTVWXYZ":
    print("Consonante - Mayúscula")
elif caracter in "0123456789":
    print("Dígito")
else:
    print("-")
