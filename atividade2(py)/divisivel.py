numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} é divisível por 3 e por 5.")
else:
    print(f"O número {numero} NÃO é divisível por 3 e por 5.")