def is_mutant(adn):
    # Verificar si los caracteres son válidos
    for sequence in adn:
        if not all(char in 'ATCG' for char in sequence):
            raise ValueError("Error en la secuencia de ADN.")

    # Contador de secuencias mutantes encontradas
    contador_mut = 0

    # Convertir el arreglo de Strings en una matriz de caracteres
    matriz_adn = [list(row) for row in adn]

    # Buscar secuencias en la matriz_adn
    for i in range(len(matriz_adn)):
        for j in range(len(matriz_adn)):
            if (j in [0, 1, 2] and check_horizontal(matriz_adn, i, j)):
                contador_mut += 1
            if (i in [0, 1, 2] and check_vertical(matriz_adn, i, j)):
                contador_mut += 1
            if check_diagonal(matriz_adn, i, j):
                contador_mut += 1
            if check_anti_diagonal(matriz_adn, i, j):
                contador_mut += 1

            if contador_mut > 1:
                return True

    return False


def check_horizontal(matriz_adn, fila, col):
    if col > len(matriz_adn) - 4:
        return False
    return matriz_adn[fila][col] == matriz_adn[fila][col + 1] == matriz_adn[fila][col + 2] == matriz_adn[fila][col + 3]


def check_vertical(matriz_adn, fila, col):
    if fila > len(matriz_adn) - 4:
        return False
    return matriz_adn[fila][col] == matriz_adn[fila + 1][col] == matriz_adn[fila + 2][col] == matriz_adn[fila + 3][col]


def check_diagonal(matriz_adn, fila, col):
    if col > len(matriz_adn) - 4 or fila > len(matriz_adn) - 4:
        return False
    return matriz_adn[fila][col] == matriz_adn[fila + 1][col + 1] == matriz_adn[fila + 2][col + 2] == matriz_adn[fila + 3][col + 3]


def check_anti_diagonal(matriz_adn, fila, col):
    if col < 3 or fila > len(matriz_adn) - 4:
        return False
    return matriz_adn[fila][col] == matriz_adn[fila + 1][col - 1] == matriz_adn[fila + 2][col - 2] == matriz_adn[fila + 3][col - 3]


# Permitir al usuario ingresar las secuencias de ADN
adn = []
print("--------------------------------------------------------------------")
print()
print("Ingrese las secuencias de ADN (6 secuencias, cada una de 6 caracteres de A, T, C, G):")
print()
print("--------------------------------------------------------------------")
print()
for i in range(6):
    while True:
        secuencia = input(f"Secuencia {i+1}: ").upper()
        if len(secuencia) != 6 or not all(char in 'ATCG' for char in secuencia):
            print(
                "Secuencia inválida. Debe ser de 6 caracteres y solo contener A, T, C, G.")
        else:
            adn.append(secuencia)
            break
print()
print("¿Es mutante?:", is_mutant(adn))
print()
print("--------------------------------------------------------------------")

# Prueba del código con un caso positivo
adn_positivo = [
    "ATGCGA",
    "CAGTGC",
    "TTATGT",
    "AGAAGG",
    "CCCCTA",
    "TCACTG"
]
print("--------------------------------------------------------------------")
print()
print("¿Es mutante? (Caso prueba True):", is_mutant(adn_positivo))

# Prueba del código con un caso negativo
adn_negativo = [
    "ATGCGA",
    "CAGTGC",
    "TTATTT",
    "AGACGG",
    "GCGTCA",
    "TCACTG"
]
print("--------------------------------------------------------------------")
print()
print("¿Es mutante? (Caso prueba False):", is_mutant(adn_negativo))
print()
print("--------------------------------------------------------------------")
print("Fin del programa")
print("--------------------------------------------------------------------")
