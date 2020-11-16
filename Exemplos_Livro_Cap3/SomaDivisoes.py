
numero = int(input('Insira o numero: '))
numeroH = 0

for count in range(1, numero+1):
    numeroH += (1/count)

print('Resultado :', numeroH)