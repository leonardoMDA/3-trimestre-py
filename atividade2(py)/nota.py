nota = float(input("Digite a nota (entre 0 e 10): "))

if 7 <= nota <= 10:
    print("Aluno aprovado!")
elif 5 <= nota <= 7:
    print("Aluno em recuperação.")
elif 0 <= nota <= 5:
    print("Aluno reprovado.")
else:
    print("Nota inválida! A nota deve ser entre 0 e 10.")