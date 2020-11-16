'''
Defaultdict é um dicionário como objeto que fornece todos os métodos fornecidos pelo dicionário, mas leva o primeiro argumento (default_factory) como tipo de dados 
padrão para o dicionário. Usar defaultdict é mais rápido do que fazer o mesmo usando o método dict.set_default.

** Um defaultdict nunca gerará um KeyError. Qualquer chave que não existe obtém o valor retornado pela fábrica padrão. **
'''
from collections import defaultdict

d = {}
d['one'] = 1
print(d)

# O defaultdict vai impedir que ocorra algum erro se eu tentar acessar uma posição do dicionário pra algo que não existe. Com isso ele preenche essa posição com alguma infor
# mação pré escolhida.

d2 = defaultdict(object)
d2['one'] = 1
# Essa linha de baixo não apresentará erro, pois o defaultdict gerará um objeto pra colocar na posição que eu estou buscando.
print(d2['two'])