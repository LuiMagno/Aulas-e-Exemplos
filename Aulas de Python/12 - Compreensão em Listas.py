'''
Além das operações de sequência e métodos de lista, o Python inclui uma operação mais avançada chamada de compreensão em listas.
As compreensões de lista nos permitem construir listas usando uma notação diferente. Você pode pensar nisso essencialmente como um
loop construído dentro de colchetes. Vamos a exemplos:
'''

# Criando uma lista com esse método

lista = [x for x in 'palavra']
print(lista)

# Criando outra com o método junto com a função range()
lista2 = [i for i in range(0,30)]
print(lista2)

# Agora um exemplo definitivo de como compreensão em listas pode me ajudar a economizar linhas quando o objetivos é criar listas
# baseadas em sequências lógicas

# Como criar uma lista de números pares de 0 a 30:
listaPar = []

for i in range(0,30):
    if i % 2 == 0:
        listaPar += [i]
print(listaPar)

# Agora criando isso de um forma mais limpa e rápida, utilizando compreensão em listas
listaPar2 = [i for i in range(0,30) if i % 2 == 0]
print(listaPar2)

# Agora para fixar o exemplo nas nossas mentes, vamos usar a compreensão em listas para criar conveter temperatuas Celsius para 
# Faherenheit
celius = [0,10,20,30,40,50,100]
faherenheit = [(temp*(9/5)+32) for temp in celius]
print('Temperaturas em Faherenheit: ', faherenheit)

# Vamos criar uma lista de elementos de 0 a 15 onde todos estão elevados ao quadrado

elevados = [i**2 for i in range(0,15)]
print(elevados)
