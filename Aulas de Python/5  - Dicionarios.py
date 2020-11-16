'''
Podemos pensar em Dicionários com tabelas hash, mas esse não é um exemplo muito bom pois eu não lembro muito bem de hash.
Tópicos para o estudo de dicionários:
1. Construindo um dicionário
2. Acessando objetos de um dicionário
3. Dicionários de Assentamento
4. Métodos básicos do dicionário

Mas o que são mapeamentos???
Os mapeamentos são uma coleção de objetos que são armazenados por uma chave, ao contrário de uma sequência que armazena objetos por
sua posição relativa (índices). Isso é importante, por vamos nos referenciar à objetos por uma chave e não pelo índice, como acontece
nas listas (vetores).
'''

my_dict = {'chave1': 99, 'chave2':'cachaça', 'chave3': 1.932, 'chave4': 'caracter'}
print( my_dict['chave1'])

my_dict['chave2'] = 123456 # podemos reatribuir os valores de uma chave do dicionário da mesma forma de um vetor
print( my_dict['chave2']) 

# assim como um inception de listas, também podemos fazer um inception de dicionários - chamamos de aninhamento de dicionários

dicionario = {'dic':{'chaveInception1': 123}} # exemplo de dicionário dentro de dicionário
print( dicionario['dic'])

# Agora vamos utilizar alguns métodos de dicionário
print(my_dict.keys()) # retorna um keys, um tipo de dado diferente

print(my_dict.values()) # mostra os valores dos elementos dentro do dicionário

# Exemplo interessante: acessar um vetor dentro de um dicionário:
dicionarioExemplo = {'a1': [1, 2, 3]}
print(dicionarioExemplo['a1'][1])  # entendar a sintaxe dessa linha é importante


# linha extra 
# Preciso entender o aninhamento de dicionários de uma forma mais precisa
print('Aqui aninhamento de dicionários')
print(dicionario['dic']['chaveInception1'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1]) #buscando somento o 'hello'
'''
Dicionário nos dá a oportunidade de utilizar e trabalhar com banco de dados não estruturado

1. Os dicionários mantêm uma ordem? Como faço para imprimir os valores do dicionário em ordem?

Os dicionários são mapeamentos e não mantêm uma ordem! Se você quer as capacidades de um dicionário, mas você gostaria 
de fazer um ordenamento também, confira a aula de dicionário ordenado mais tarde no curso!
'''
