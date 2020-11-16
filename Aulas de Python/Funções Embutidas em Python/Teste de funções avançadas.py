''' Funções avançadas Teste! 

Problema 1 - Use o map para criar uma função que encontre o tamanho de cada palavra na frase (quebrado por espaços) e retornar os valores em uma lista.
A função terá uma entrada de uma string e exibirá uma lista de números inteiros.

'''


def word_lengths(str): print(list(map(len, str.split()))) #Usando a função len() e splitando a string 'str' podemos resolver o problema 1

word_lengths('How long are the words in this phrase')

'''
Problema 2 - Use reduce para pegar uma lista de dígitos e retornar o número que eles correspondem a.
Não converta os números inteiros em strings! 

'''
from functools import reduce

def digits_to_num(numbers): print(reduce(lambda x,y: x*10 + y, numbers))
    
digits_to_num([3,4,3,2,1]) # saída desse método 34321

'''
Problema 3 - Use o filter para retornar as palavras de uma lista de palavras que começam com uma letra especificada.
'''

def filter_words(word_list, letter):
    print(list(filter(lambda word: word[0] == letter, word_list)))
    pass
l = ['hello','are','cat','dog','ham','hi','go','to','heart']

filter_words(l,'h')

'''
Problema 4 -  Use zip e list comprehension para retornar uma lista do mesmo comprimento onde cada valor é as duas cadeias de caracteres de L1 e L2 concatenados juntos com 
o conector entre eles. Veja o exemplo abaixo:
'''
def concatenate(lista1,lista2, conector):
    return [word1+conector+word2 for (word1,word2) in zip(lista1,lista2)]
    

print(concatenate(['A','B'],['a','b'],'-'))

'''
Problema 5 - Use enumerate e outras habilidades para retornar um dicionário que tenha os valores da lista como chaves e o índice como o valor. Você pode assumir que um 
valor só aparecerá uma vez na lista fornecida.
'''
def d_list(vetor):
    return {key:value for value,key in enumerate(vetor)}
    

print(d_list(['a', 'b', 'c', 'd']))