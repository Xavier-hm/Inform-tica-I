N = int(input("Ingrese el número de filas para la piramide: "))

num_esp = (N-2)*2 + 1
num_ast = 1

for i in range(N):
    for i in range(num_ast):
        print("*", end="")

    for i in range(num_esp):
        print(" ", end="")

    if num_esp < 1:
        num_ast = num_ast - 1

    for i in range(num_ast):
        print("*", end="")
    
    print()

    num_esp = num_esp - 2
    num_ast = num_ast + 1