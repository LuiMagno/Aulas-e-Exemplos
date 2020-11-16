# Elabora um algoritmo que leiam, some e imprima o resultado da soma entre dois vetores inteiros de 50 posições
import random
import math
vetor1 = []
vetor2 = []
vetorResultado = []
for aux in range(50):
    vetor1.append(math.ceil(10 * random.random())) 
    vetor2.append(math.ceil(10 * random.random()))
    resultado = vetor1[aux] + vetor2[aux]
    vetorResultado.append(resultado)

print(vetorResultado)
# IndexError: list assignment index out of range 
# Eu estava tentando adicionar um número inteiro a uma posição inexistente dentro do vetor1, por isso tive que usar a função append