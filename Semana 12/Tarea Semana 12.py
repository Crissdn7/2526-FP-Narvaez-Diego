asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("=== SISTEMA DE RESERVA DE ASIENTOS ===\n")
print("Ingrese fila (0 a 2):")
f = int(input())

print("Ingrese columna (0 a 3):")
c = int(input())

if f < 0 or f > 2 or c < 0 or c > 3:
    print("\nError: Fila debe estar entre 0 y 2, columna entre 0 y 3")
elif asientos[f][c] == 1:
    print(f"\nError: El asiento en fila {f}, columna {c} ya está reservado")
else:
    asientos[f][c] = 1
    print(f"\nAsiento en fila {f}, columna {c} reservado exitosamente")

print("\n=== ESTADO DE LA SALA ===\n")
print("  Columna: 0 1 2 3")
print("  " + "-" * 9)

for i in range(3):
    print(f"Fila {i} |", end=" ")
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()

print("\n(0 = libre, 1 = reservado)")

