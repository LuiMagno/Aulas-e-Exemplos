# Construa um algoritmo que efetue a leitura, a soma e a impressão do resultado entre duas matrizes inteiras que comportem 25 elementos
import random
import math

matriz1 = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
matriz2 = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
matrizResultado = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

for l in range(0,5):
    for c in range(0,5):
        matriz1[l][c] = math.ceil(10*random.random())
        matriz2[l][c] = math.ceil(10*random.random())
        matrizResultado[l][c] = matriz1[l][c] + matriz2[l][c]

for l in range(0,5):
    for c in range(0,5):
        print(f'[{matrizResultado[l][c]:^5}]', end='')
    print()

# Debuggar é o efeito para o sucesso