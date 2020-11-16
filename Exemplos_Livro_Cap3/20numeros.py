# Algoritmo que lê 20 números e devolve o maior e o menor



menorNumero = 1000000
maiorNumero = 0

for count in range(20):
    numero = int(input('Insira um numero: '))
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero:
        menorNumero = numero


print('Menor Número:', menorNumero)
print('Maior Número:', maiorNumero)