def calcular_media(lista_numeros):

  if not lista_numeros:
    return "A lista está vazia."
  else:
    soma = sum(lista_numeros)
    quantidade = len(lista_numeros)
    media = soma / quantidade
    return media

numeros = [2, 4, 6, 8, 10]
media = calcular_media(numeros)
print(f"A média dos números é: {media}")