# exercício proposto 05 item e Fazer uma potência sem as operações de multiplicação e divisão / base,expoente e potência

base = int(input('Entre com a base: '))
expoente = int(input('Entre com o expoente: '))

aux = 0
resultado = 1
while aux < expoente:
    resultado = resultado*base
    aux += 1

print('Resultado = ', resultado)


# SyntaxError: unexpected EOF while parsing -> provavelmente seu loop está vazio ou fazendo algo de errado2

