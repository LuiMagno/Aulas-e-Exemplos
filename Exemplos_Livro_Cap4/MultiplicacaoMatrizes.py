

matriz1 = [[1,2,3], [0,0,0], [0,0,0]]
matriz2 = [[1,2,3], [0,0,0], [0,0,0]]
matrizResultado = [[0,0,0], [0,0,0], [0,0,0]]
k = 0

for l in range (0,3):
    for c in range(0,3):
        for k in range(0,3):
            matrizResultado[l][c] += matriz1[l][k] * matriz2[k][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrizResultado[l][c]:^5}]', end='')
    print()

# O entendimento da linha 11 se dá por alguns motivos: Sabemos que para a formação do elemento R[i,j], o índice da linha i se repete
# na matriz A e o índice da coluna j se repete na matriz B. Coluna A é igual a linha de B, e repete-se 3 vezesm de 1 a 3, logo, criamos
# um índice K para efetuar a repetição. 
# Temos esse loop de K que será repetido 3 vezes para formar o R[0,0].

