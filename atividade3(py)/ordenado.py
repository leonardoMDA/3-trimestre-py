vetor = [0] * 5

for i in range(5):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

ordenado = True

for i in range(len(vetor) - 1):
    if vetor[i] > vetor[i + 1]:
        ordenado = False
        break

if ordenado:
    print("Os elementos do vetor estão em ordem crescente.")
else:
    print("Os elementos do vetor não estão em ordem crescente")