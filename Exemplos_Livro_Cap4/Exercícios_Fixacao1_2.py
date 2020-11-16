import random
import math

vetor1 = []
vetor2 = []
vetorOperacoes = ['+', '-', '*', '/']
vetorAleatorioOperacoes = []
vetorResultado = []
for aux in range(20):
    vetor1.append(math.ceil(10*random.random()))
    vetor2.append(math.ceil(10*random.random()))
    vetorAleatorioOperacoes.append(random.choice(vetorOperacoes))
    if vetorAleatorioOperacoes[aux] == '+':
        temp = vetor1[aux] + vetor2[aux]
        vetorResultado.append(temp)
    elif vetorAleatorioOperacoes[aux] == '-':
        temp = vetor1[aux] - vetor2[aux]
        vetorResultado.append(temp)
    elif vetorAleatorioOperacoes[aux] == '*':
        temp = vetor1[aux] * vetor2[aux]
        vetorResultado.append(temp)
    else:
        temp = vetor1[aux] / vetor2[aux]
        vetorResultado.append(temp)

print(vetorResultado)
