'''
Nessa aula teremos uma noção introdutória de alguns conceitos de declaração em Python
'''

# Por exemplo, o ':' subistitui o colchetes usado em outras linguagens de programação, como em C. E também utilizamos a identação
# para identificar o corpo de um código

a = 3
b = 2
 
if a>b:
    print('Aula de Declaracoes') # Aqui podemos ver que esta linha está identada, pois toda identação a partir dessa if pertence a ele

'''
IF, ELIF E ELSE
'''
# Criando um dicionário de aluno com notas pra correr as várias possibilidades dos ifs
a = {'Lui': 10, 'Caio': 6, 'Zero': 2}

aluno = a['Zero']

if aluno >=9:
    print('Aluno Brilhante!')
elif aluno >=7:
    print('Ótimo! Está aprovado')
elif aluno >=4:
    print('Está de recuperação, estude seu vagabundo')
else:
    print('Reprovou, mas a vida de tá várias oportunidades, aproveite as próximas!')

'''
FOR
O loop 'for' atua como um iterador em Python, ele passa por itens que estão em sequência ou em qualquer outro item iterável. Os objetos
que aprendemos até agora e podem ser iterados são: Strings, listas, tuplas e até iteráveis imbutidos em dicionários, como chaves ou
valores.

Pelo que vi até agora, o 'for' funciona de uma forma 'diferente' em Python, como se fosse de forma mais direta do quê nas outras 
linguagens (como a maioria do que vi até agora)
'''
lista = [1,2,3,4,5,6,7,8,9,10]

for num in lista: #para cada 'num'(elemento) contido na lista execute a ação de print(). O 'num' é um variável sendo reatribuida
    print(num)

# Código exemplo para checar se o número é par

for num in lista:
    if num % 2 == 0:
        print('Número ', num, ' é par')
    else:
        print('Número ', num, ' é ímpar')

# Somatório dos compenentes do vetor
soma = 0
for num in lista:
    soma += num
print(soma)

# Também posso usar o for para iterar sobre uma string

string = 'Eu sou um ótimo programador'
for char in string: # Aqui nesse for qualquer palavra pode ser colocada como variável no lugar de 'char'
    print(char)
print('//////////////////////////////////////////////////////////')

# Posso iterar na tupla também
tup = (1,2,3,4,5)
for num in tup:
    print(num)
print('//////////////////////////////////////////////////////////')
# Vou mostrar agora um conceito de desembalagem de tuplas para interação
lista_tuplas = [(1,2), (3,4), (5,6)]
for (t1,t2) in lista_tuplas: # Assim eu posso pegar cada item das tuplas e designar a uma variável diferente
    print(t1+t2)
print('//////////////////////////////////////////////////////////')
# Isso também funciona com atribuições
(t1,t2) = lista_tuplas[2]
print(t1)
print(t2)
print('//////////////////////////////////////////////////////////')
# A iteração também pode ser realizada em dicionários
d = {'k1': 1, 'k2': 2, 'k3': 3}
for (keys, items) in d:
    print(items)

'''
WHILE
'''
print('//////////////////////////////////////////////////////////')
x = True
while x: # Não preciso usar o 'while x == True' pois ele já define 'True' como sendo default para booleanos
    x = input('X é verdadeiro ou falso?')
    if x == 'verdadeiro':
        x = True
    else:
        x = False
        
# ESTRUTURA DE CÓDIGO PERIGOSA -> 'while TRUE' pois nunca para
        