vetor = [0] * 5

for i in range(5):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

    print("Vetor preenchido:", vetor)

soma = sum(vetor)

media = soma / len(vetor)

print("A média dos elementos do vetor é:", media)