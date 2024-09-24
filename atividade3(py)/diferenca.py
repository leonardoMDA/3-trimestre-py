vetor = [0] * 5

for i in range(5):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

maior = vetor[0]
menor = vetor[0]

for elemento in vetor:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento

diferenca = maior - menor

print("A diferença entre o maior e o menor valor do vetor é", diferenca)
