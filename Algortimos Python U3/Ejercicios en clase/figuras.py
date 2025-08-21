N = int(input("Ingrese el número de filas para la piramide: "))

num_esp = 3
num_ast = 1

print()

num_esp = N-1
num_ast = 1

for i in range(N):
    for i in range(num_esp):
        print(" ", end="")

    for i in range(num_ast):
        print("*", end="")
    
    print()

    #print(num_esp, ":", num_ast)
    num_esp = num_esp - 1
    num_ast = num_ast + 1
