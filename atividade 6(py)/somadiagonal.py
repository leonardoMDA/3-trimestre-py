def soma_diagonal_principal(matriz):

  soma = 0
  n = len(matriz) 

  for i in range(n):
    soma += matriz[i][i]

  return soma


matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

resultado = soma_diagonal_principal(matriz)
print(resultado) 