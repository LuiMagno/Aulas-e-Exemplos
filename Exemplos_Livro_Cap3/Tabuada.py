# Algoritmo de uma tabuada

numero = 0

while numero !=  -1:
    numero = int(input('Insira o número que deseja para a tabuada: '))
    for count in range(11):
        resultado = numero*count
        print(numero,'*',count,'=',resultado)
    
