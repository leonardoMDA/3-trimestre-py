def matriz_eh_quadrada(matriz):
    for linha in matriz:
        if len(matriz) != len(linha):
           return False
        return True
    
matriz1 = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

matriz2 = [
 [1,2,3],
 [4,5,6]
]

print("A matriz1 é quadrada?", matriz_eh_quadrada(matriz1))
print("A matriz2 é quadrada?", matriz_eh_quadrada(matriz2))