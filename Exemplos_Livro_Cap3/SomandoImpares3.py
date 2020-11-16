# Elabore um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no conjunto
# de números de 1 a 500
acumulador = 0
for count in range(4):
    if count % 2 != 0:
        if count % 3 == 0:
            acumulador += count

print('Soma dos números ímpares divisíveis por 3 entre 1 e 500: ', acumulador)

# O for x in range(3) vai contar o loop 3 vezes, mas o x só vai de 0 até 2 e para no 3