def inverter_diagonal_principal(matriz):

  n = len(matriz)
  matriz_invertida = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(i+1, n):
      matriz_invertida[i][j] = matriz[j][i]
      matriz_invertida[j][i] = matriz[i][j]

  return matriz_invertida

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matriz_invertida = inverter_diagonal_principal(matriz)
print(matriz_invertida)