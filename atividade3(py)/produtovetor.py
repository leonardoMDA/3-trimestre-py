vetor = [0] * 4

for i in range(4):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))


produto = 1

for elemento in vetor:
    produto *= elemento

print("O produto dos elementos do vetor é:", produto)