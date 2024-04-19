import math

def calcular_circunferencia(radio):
    # Calcula la circunferencia utilizando la fórmula 2 * pi * radio
    circunferencia = 2 * math.pi * radio
    return circunferencia

def imprimir_resultado(radio, circunferencia):
    print(f"Para un radio de {radio}, la circunferencia es: {circunferencia:.6f}")

def main():
    # Valores de radio dados
    radios = [3, 8, 10]

    # Calcula la circunferencia para cada radio dado
    for radio in radios:
        circunferencia = calcular_circunferencia(radio)
        imprimir_resultado(radio, circunferencia)

if __name__ == "__main__":
    main()
