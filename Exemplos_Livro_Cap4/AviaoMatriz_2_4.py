import math
import random

cidade1 = 0
cidade2 = 1
matriz1 = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

for l in range(0,7):
    for c in range(0,7):
        if c == l:
            continue
        else: 
            matriz1[l][c] = math.ceil(10*random.random())
       
while cidade1 != cidade2:
    cidade1 = int(input('Forneça a cidade de saída e a de chegada para calcularmos o tempo necessário de deslocamento: '))
    cidade2 = int(input())
    print(matriz1[cidade1][cidade2])       

