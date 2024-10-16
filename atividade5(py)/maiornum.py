def encontrar_maior_loop(lista):

  if not lista:
    return "A lista está vazia."
  else:
    maior = lista[0]
    for numero in lista:
      if numero > maior:
        maior = numero
    return maior

numeros = [2, 9, 3, 7, 5]
maior_numero = encontrar_maior_loop(numeros)
print(f"O maior número é: {maior_numero}")