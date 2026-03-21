def calcular_promedio(nota1, nota2, nota3):
    promedio = round((nota1 + nota2 + nota3) / 3, 2)
    return promedio

if __name__ == "__main__":
    n1 = float(input("Ingrese la primera nota: "))
    n2 = float(input("Ingrese la segunda nota: "))
    n3 = float(input("Ingrese la tercera nota: "))

    resultado_final = calcular_promedio(n1, n2, n3)

    print(f"El promedio final obtenido es: {resultado_final}")