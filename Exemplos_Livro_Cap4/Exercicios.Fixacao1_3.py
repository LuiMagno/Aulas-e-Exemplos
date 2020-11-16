import random
import math

vetor1 = []
vetor2 = []
vetorResultado = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp = 9
for aux in range(20):
    vetor1.append(math.ceil(10*random.random()))
    vetor2.append(math.ceil(10*random.random()))
    vetorResultado[temp] = vetor1[aux] * vetor2[aux]
    temp -= 1
    if temp == -1:
        temp = 19
    print(vetorResultado)

print(vetorResultado)
