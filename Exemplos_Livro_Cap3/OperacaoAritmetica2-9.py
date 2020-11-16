numero1 = float(input())
numero2 = float(input())

operacaoAritmetica = input('Insira a operação desejada: ')
resultado = 0
if operacaoAritmetica == '+':
    resultado = numero1 + numero2

if operacaoAritmetica == '-':
    resultado = numero1 - numero2

if operacaoAritmetica == '*':
    resultado = numero1 * numero2

if operacaoAritmetica == '/':
    resultado = numero1 / numero2

print('Resultado é: ', resultado)