'''
O método embutido enumerate() vai fazer uma tupla com o iterável fonecido para que essa
nova tupla seja numerada de acordo com a sequência fornecida
'''
lista = ['a', 'b', 'c', 'd']

for number, item in enumerate(lista):
    print(number, ':', item)