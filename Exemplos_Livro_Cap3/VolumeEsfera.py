# Faça um algoritmo para calcular o volume de uma esfera de raio R, em que R é um dado fornecido pelo usuário. O volume de uma esfera é dado por
# V = 4/3*pi*R^3

raioEsfera = float(input('Insira o Raio da esfera: '))
PI = 3.14

volumeEsfera = (4/3) * PI * pow(raioEsfera, 3)

print('O volume da esfera é : ', volumeEsfera)



# TypeError: can't multiply sequence by non-int of type 'float' 
# Origem do Erro: PI = 3,14 -> o padrão norte americano utiliza o '.' e não a ',', então temos que utilizar 3.14