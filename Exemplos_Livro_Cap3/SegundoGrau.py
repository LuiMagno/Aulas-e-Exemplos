# Construa um algoritmo para calcular as raízes de uma equação de 2° grau( Ax^2 + Bx + C), sendo os valores A, B, C são fornecidos pelo usuário 
# a equação possui duas raízes reais.

A = int(input('A : '))
B = int(input('B : '))
C = int(input('C : '))

delta = pow(B,2) - 4*(A*C)

x1 = (-1*(B) + pow(delta, 0.5))/(2*A)

x2 = (-1*(B) - pow(delta, 0.5))/(2*A)

print("Solução Real 1 : ", x1)
print("Solução Real 2 : ", x2)