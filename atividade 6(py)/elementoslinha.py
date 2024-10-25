def soma_elementos_por_linha(matriz):
  soma_por_linha = []

  for linha in matriz:
    soma_por_linha.append(sum(linha))

  return soma_por_linha

matriz = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

resultado = soma_elementos_por_linha(matriz)
print("Soma dos elementos dde cada linha:", resultado)