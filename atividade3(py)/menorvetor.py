vetor = [0] * 3

for i in range(3):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

    print("Vetor preenchido:", vetor)

menor = vetor[0]

for i in range(1, 3):
    if vetor[i] < menor:
        menor = vetor[i]

print("O menor valor do vetor é:", menor)