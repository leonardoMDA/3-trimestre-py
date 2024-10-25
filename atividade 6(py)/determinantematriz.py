def determinante(matriz):

  if len(matriz) == 2 and len(matriz[0]) == 2:
  
    a, b = matriz[0]
    c, d = matriz[1]
    return a*d - b*c
  elif len(matriz) == 3 and len(matriz[0]) == 3:

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
  else:
    raise ValueError("Matriz deve ser 2x2 ou 3x3")

matriz_2x2 = [[1, 2],
              [3, 4]]

matriz_3x3 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

det_2x2 = determinante(matriz_2x2)
det_3x3 = determinante(matriz_3x3)

print(det_2x2)  
print(det_3x3)  