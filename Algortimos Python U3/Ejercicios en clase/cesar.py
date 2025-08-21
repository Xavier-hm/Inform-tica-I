k = int(input("Ingrese la clave de Cesar: "))
msg = input("Ingrese el mensaje a encriptar: ")

abc = "abcdefghijklmnopqrstuvwxyz"

for letra in msg:
    if not (letra in abc):
        print(" ", end="")
        continue
    c = 0
    for letra_abc in abc:
        if letra == letra_abc:
            break
        c = c + 1

    if c + k >= len(abc):
        print(abc[c+k - len(abc)], end="")
    else:
        print(abc[c+k], end="")
