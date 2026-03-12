def calcular_promedio(nota1, nota2):
    """Calcula y retorna el promedio de dos calificaciones."""
    promedio = (nota1 + nota2) / 2
    return promedio

if __name__ == "__main__":
    n1 = float(input("Ingrese la primera nota: "))
    n2 = float(input("Ingrese la segunda nota: "))

    resultado_final = calcular_promedio(n1, n2)

    print(f"El promedio final obtenido es: {resultado_final}")
