def eh_palindromo(palavra):
  
  palavra = palavra.replace(" ", "").lower()
  palavra_invertida = palavra[::-1]
  return palavra == palavra_invertida

palavra = "A bola vai e vem"
if eh_palindromo(palavra):
  print("A palavra é um palíndromo.")
else:
  print("A palavra não é um palíndromo.")