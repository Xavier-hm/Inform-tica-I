sentence = input("Ingrese una frase: ")
char = input("Ingrese un caracter: ")

#Encontrar, find
"""
c = 0
while c < len(sentence):
    if sentence[c] == char:
        print(c, end=" ")
        break
    c = c + 1
"""
i = 0

while i < len(sentence):
    c = sentence[i:].find(char)
    if c == -1:
        break
    print(i + c, end=" ")
    i = i + c + 1

print()

#c = sentence.find(char)

#print("La posición del caracter es: ", c)

#Contar, count
"""
c = 0
k = 0

while c < len(sentence):
    if sentence[c] == char:
        k = k + 1
    c = c + 1
"""
k = sentence.count(char)

print("El caracter ", char, "está ", k, " veces en el texto." )

