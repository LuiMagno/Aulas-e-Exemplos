'''
A função embutida reduce() é, basicamente, uma forma de reduzir por meio de uma função uma lista, onde os elementos dessa lista são reduzidos
a apenas um elemento, que é o resultado dessa iteração.

'''
from functools import reduce

lst = [47,11,42,13]

print(reduce(lambda x,y: x+y,lst)) # A cada iteração o X é incrementado e o valor Y é a nova posição do vetor lst, assim fornecendo o resultado da soma de todos os valores de lst

max_find = lambda a,b: a if (a>b) else b

print(reduce(max_find, lst))