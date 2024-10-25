def transpor_matriz(matriz):
    matriz_transposta = [list(linha) for linha in zip(*matriz)]
    return matriz_transposta

matriz = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

resultado = transpor_matriz(matriz)

print("Matriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz transposta:")
for linha in resultado:
    print(linha)