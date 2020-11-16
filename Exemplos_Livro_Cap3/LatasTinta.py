# Construa um algoritmo que calcule a -----quantidade de latas de tinta------ necessárias e o ---custo----- para pintar tanques cilíndricos de combustível, em que são 
# fornecidos a altura e o raio desse cilindro.
# A lata de tinta custa 50 reais
# Cada lata tem 5 litros
# Cada litro pinta 3 metros quadrados
import math
altura = int(input('Altura do cilindro: '))
raio = int(input('Raio do cilindro: '))
# 1 litro 10 real, cada litro pinta 3 metros quadrados. Só calcular a área e dividir por 3

PI = 3.14

#areaTotal = (PI*(pow(raio,2))) + (2*PI*raio*altura)
areaTotal = 22
totalLitros = areaTotal/3

totalLatas = math.ceil(totalLitros/5)

precoTotal = totalLatas*50

print('Área Total do Cilindro: ', areaTotal)
print('Total Litros: ', totalLitros)
print('Total de Latas: ', totalLatas)
print('Preço Total: ', precoTotal)

