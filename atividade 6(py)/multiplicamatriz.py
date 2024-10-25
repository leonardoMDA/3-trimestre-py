def multiplicar_matrizes(matriz1, matriz2):
 
  linhas_m1, colunas_m1 = len(matriz1), len(matriz1[0])
  linhas_m2, colunas_m2 = len(matriz2), len(matriz2[0])

  if colunas_m1 != linhas_m2:
    raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")

  resultado = [[0 for _ in range(colunas_m2)] for _ in range(linhas_m1)]

  for i in range(linhas_m1):
    for j in range(colunas_m2):
      for k in range(colunas_m1):
        resultado[i][j] += matriz1[i][k] * matriz2[k][j]

  return resultado


matriz_a = [[1, 2, 3],
            [4, 5, 6]]

matriz_b = [[7, 8],
            [9, 10],
            [11, 12]]

resultado = multiplicar_matrizes(matriz_a, matriz_b)
print(resultado)