# Construa um algoritmo que forneça a distância de 2 pontos.
x1 = int(input('Insira x1 do ponto P: '))
y1 = int(input('Insira y1 do ponto P: '))

x2 = int(input('Insira x2 do ponto Q: '))
y2 = int(input('Insira y2 do ponto Q: '))

result1 = pow((x2-x1), 2)
result2 = pow ((y2-y1), 2)
distanciaPontos = pow((result1+result2), 0.5)

print('Distância entre dois pontos é :', distanciaPontos)