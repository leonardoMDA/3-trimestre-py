def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
        return soma
matriz = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
resultado = soma_matriz(matriz)
print("A soma de todos os elementos é:", resultado)