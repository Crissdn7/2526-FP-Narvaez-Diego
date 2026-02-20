# Tarea: Matriz y creación de cuenta en GitHub
# Parte 1: Programa con matriz

# Declarar una matriz de 3x3 con números enteros
matriz = [
    [2, 4, 6],#0
    [1, 3, 5],#1
    [7, 8, 9] #2
    #0 #1 #2
]

print("Valores de la matriz 3x3:")
print("-" * 20)

for i in range(3):
    for j in range(3):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")

print("\n" + "-" * 20)
print("Matriz en formato de tabla:")
print("-" * 20)

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()

