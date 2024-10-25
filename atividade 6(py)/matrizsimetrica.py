def eh_matriz_simetrica(matriz):
    n_linhas = len(matriz)
    if n_linhas == 0:
       return True
    
    n_colunas = len(matriz[0])

    if n_linhas != n_colunas:
       return False
    
    for i in range(n_linhas):
        for j in range(i + 1, n_colunas):
            if matriz[i][j] != matriz[j][i]:
                return False
            
    return True

matriz_simetrica = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
]        

matriz_nao_simetrica = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

print("A matriz simétrica é simétrica?", eh_matriz_simetrica(matriz_simetrica))
print("A matriz não simétrica é simétrica?", eh_matriz_simetrica(matriz_nao_simetrica))