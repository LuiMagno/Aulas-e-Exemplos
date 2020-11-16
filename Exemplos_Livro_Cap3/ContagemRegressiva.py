# Elabore um algoritmo que simule uma contagem regressiva de 10 segundos, ou seja, mostre 10:00, então 9:59, 9:58 ...  até 0:00

minutos = 10
segundos = 00
for countMinutos in range(10):
    print(minutos,':', segundos)
    minutos -= 1
    segundos = 59
    for countSegundos in range(59):
        print(minutos, ':', segundos)
        segundos -= 1
         