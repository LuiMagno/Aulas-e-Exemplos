# para homens: (72.7 * h) - 58
# para mulheres: (62.1 * h) - 44.7

sexo = input('Insira seu sexo: ')
altura = float(input('Insira sua altura: '))

if sexo == 'feminino':
    pesoIdeal = (62.1*altura) - 44.7
else:
    pesoIdeal = (72.7 * altura) - 58

print('Para o sexo ', sexo, ' o peso ideal é: ', pesoIdeal)
