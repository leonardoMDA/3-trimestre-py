def contar_vogais(texto):

  vogais = "aeiouAEIOU"
  contador = 0
  for letra in texto:
    if letra in vogais:
      contador += 1
  return contador

palavra = "Python"
numero_vogais = contar_vogais(palavra)
print(f"A palavra '{palavra}' tem {numero_vogais} vogais.")