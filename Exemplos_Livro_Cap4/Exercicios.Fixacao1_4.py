
vetor1 = [3, 1, 41, 51, 62, 0, 13, 12, 4, 6, 72, 34, 98, 23, 89, 12, 43, 32, 52, 5]
vetorResultado = []


for aux in range(20):
    menorAtual = 100000
    posicaoMenor = 0
    for temp in range(aux, 20):
        if vetor1[temp] < menorAtual:
            menorAtual = vetor1[temp]
            posicaoMenor = temp
    x = vetor1[aux]
    vetor1[aux] = menorAtual
    vetor1[posicaoMenor] = x            
print(vetor1)

# Vetor simples para ordenar um vetor de 20 posições por Ordenação Direta
