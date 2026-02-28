# Tarea: Matriz 5x5 con ingreso por consola
# Descripción: Programa que pide al usuario ingresar valores en una matriz 5x5,
# los almacena y los muestra organizados en forma de tabla.

# Crear una matriz de tamaño 5x5
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Pedir al usuario que ingrese los valores
print("Ingrese los valores para la matriz 5x5:")
print("-" * 40)

for fila in range(5):
    for columna in range(5):
        while True:
            try:
                valor = float(input(f"Ingrese el valor para la posición [{fila}][{columna}]: "))
                matriz[fila][columna] = valor
                break
            except ValueError:
                print("Error: Por favor ingrese un número válido.")

# Mostrar la matriz ingresada
print("\n" + "=" * 40)
print("Matriz ingresada:")
print("=" * 40 + "\n")

for fila in range(5):
    for columna in range(5):
        print(f"{matriz[fila][columna]:>8.2f}", end=" ")
    print()  # Saltar de línea después de cada fila

print("\n" + "=" * 40)
