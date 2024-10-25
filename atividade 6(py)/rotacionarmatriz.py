def rotacionar_90_graus(matriz):

  n = len(matriz)
  matriz_rotacionada = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      matriz_rotacionada[j][n-1-i] = matriz[i][j]

  return matriz_rotacionada

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matriz_rotacionada = rotacionar_90_graus(matriz)
print(matriz_rotacionada)