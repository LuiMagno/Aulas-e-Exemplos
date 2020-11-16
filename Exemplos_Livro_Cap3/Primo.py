# Construa um algoritmo que confere se o número fornecido é primo ou não

numero = int(input('Insira o número: '))
numeroDivisoes = 0
for count in range(1, numero):
    if numero%count == 0:
        numeroDivisoes += 1

if numeroDivisoes > 2:
    print('Este número não é primo!')
else:
    print('Este número é primo!')