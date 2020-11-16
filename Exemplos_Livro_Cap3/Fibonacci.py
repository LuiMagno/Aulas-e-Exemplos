# Escreva um algoritmo que faz a série de fibonacci até o vigésimo número
primeiroAnterior = 1
segundoAnterior = 0
print(segundoAnterior)
print(primeiroAnterior)
for count in range(1, 20):
    numeroAtual = primeiroAnterior+segundoAnterior
    print(numeroAtual)
    segundoAnterior = primeiroAnterior
    primeiroAnterior = numeroAtual

