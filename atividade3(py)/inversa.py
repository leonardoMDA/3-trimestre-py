vetor = [0] * 5

for i in range(5):
    vetor[i] = int(input(f"Digite o elemento {i + 1}: "))

print("Elementos do vetor na ordem inversa:")
for elemento in vetor[::-1]:
    print(elemento)
