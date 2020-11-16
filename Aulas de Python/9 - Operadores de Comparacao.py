'''
Essa aula é muito trivial, principalmente pelos meus conhecimentos prévios, então vamos dar uma passada bem rápida por ela.
O que basicamente se precisa saber é a tabela de comparadores lógicos que todos nós já sabemos como funciona.

== -----> se os valores forem iguais, temos saída verdadeira
!= -----> se os valores forem diferentes, temos saída verdadeira
<> -----> se os valores forem diferentes, temos saída verdadeira
>  -----> se o valor do operando esquerdo for maior que o direito, temos verdadeira
<  -----> se o valor do operando direito for maior que o esquerdo, temos verdadeiro
>= -----> se o valor do operando direito for maior ou igual que o esquerdo, temos verdadeiro
<= -----> se o valor do operando esquerdo for maior ou igual ao do direito, temos verdadeiro
'''

x = 2
y = 1
c = 2
if x == y:
    print('X igual a Y')
elif x>y:
    print('X maior que Y')
elif x<y:
    print('X menor que Y')
if x != y:
    print('X diferente de Y')


 # Ainda nessa aula vamos tratar de operadores de comparacao utilizados de forma encadeada, como na linha abaixo

if (x == c and y <= c) and (y != 3):
     print('Eita menino')