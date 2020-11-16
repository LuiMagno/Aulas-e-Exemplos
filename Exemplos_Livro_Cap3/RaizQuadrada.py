# Elabore um algoritmo que calcule um número inteiro que mais se aproxima da raiz quadrada de um número fornecido pelo usuário

numero = int(input('Insira seu número: '))

for count in range(numero):
    raizAproximada = count*count
    if raizAproximada>numero:
        break
    raizAproximada = 0

print('Número inteiro aproximado é: ', count-1)