# Elabore um algoritmo que calcule um fatorial (Coisas básicas pra se ter na cabeça - Fatorial e Fibonacci)
# Lembrando que o fatorial é N!=1x2x3x4x..x(n-1)*n -> fatorial de 4!= 1x2x3x4 = 24

numeroFatorial = int(input('Insira o número:' ))
resultadoFatorial = 1
for count in range(1, numeroFatorial+1):
    resultadoFatorial = resultadoFatorial*count

print('Resultado = ', resultadoFatorial)