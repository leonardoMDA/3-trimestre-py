vetor = [0] * 5

for i in range(5):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

    print("Vetor preenchido:", vetor)

contador_pares = 0

for elemento in vetor:
    if elemento % 2 == 0:
        contador_pares += 1

print("A quantidade de elementos pares no vetor é:", contador_pares)