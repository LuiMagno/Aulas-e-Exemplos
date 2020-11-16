# Desenvolver permutando posições vizinhas caso for menor

vetor = [3, 1, 41, 51, 62, 0, 13, 12, 4, 6, 72, 34, 98, 23, 89, 12, 43, 32, 52, 5]
for temp in range(10):
    for aux in range(20):
        if aux<19:
            if vetor[aux] > vetor[aux+1]:
                x = vetor[aux]
                vetor[aux] = vetor[aux+1]
                vetor[aux+1] = x

print(vetor)


# Ordenação de vetor por Bubble Sort