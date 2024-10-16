def fatorial_iterativo(n):

  if n < 0:
    return
  elif n == 0:
    return 1
  else:
    fatorial = 1
    for i in range(1, n+1):
      fatorial *= i
    return fatorial

numero = 5
resultado = fatorial_iterativo(numero)
print(f"O fatorial de {numero} é {resultado}")