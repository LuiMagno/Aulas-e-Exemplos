# fazendo uma divisão sem usar a operação de divisão
dividendo = int(input('Digite o dividendo '))
divisor = int(input('Digite o divisor '))
resultado = 0
while dividendo >= divisor:
    resultado += 1
    dividendo -= divisor
resto = dividendo

print('Resultado = ', resultado)
print('Resto = ', resto)
