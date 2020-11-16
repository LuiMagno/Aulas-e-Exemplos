'''
A função filter() basicamente 'filtra' os valores de um vetor dependendo da condição passada na função
'''

lista = [1,4,5,12,19,21,22,33]

listaPar = list((filter(lambda x: x%2 == 0, lista))) # Ou seja, o elemento x da lista 'lista' que for par passará no filter e formará uma nova lista somente
# com os elmentos que retornaram true no retorno da função lambda.
print(listaPar)