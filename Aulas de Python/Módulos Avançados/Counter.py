'''
Coleções - Tratamento de Dados
'''
from collections import Counter

l = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
print(Counter(l)) # Aqui criamos um objeto da classe counter que lista o número de vezes que tal elemento apareceu na minha lista

print(Counter('asdadsasdasdasdasdasdasdada')) # Contando as vezes que letras aparecem dentro da string
s =  'Quantas palavras aparecem dentro dessa frase? Será que aparecem palavras repetidas?'
# Então, a partir dessa string 's' junto com a função Counter(), poderemos saber quantas vezes as palavras apareceram.
# Aqui é importante usarmos o split, para separar cada palavra da string e formar iteráveis.

c = Counter(s.split())
print(c)

# Como se torna um objeto da Classe Counter, 'c' tem seus próprios métodos.

print(c.most_common(2)) # 2 palavras mais comuns 
