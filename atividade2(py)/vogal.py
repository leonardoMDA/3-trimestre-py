letra = input("Digite uma letra: ").lower()

if len (letra) == 1 and letra.isalpha():
    if letra in 'aeiou':
        print(f"A letra {letra} é uma vogal.")
    else:
        print(f"A letra {letra} é uma consoante.")
else:
    print("Por favor, digite apenas uma letra.")