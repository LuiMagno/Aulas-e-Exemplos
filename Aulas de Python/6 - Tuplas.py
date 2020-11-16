'''
Tuplas
Em Python, as tuplas são muito semelhantes às listas, no entanto, ao contrário das listas, elas são imutáveis, o que significa 
que elas não podem ser alteradas. Você usaria tuplas para apresentar coisas que não deveriam ser alteradas, como dias da semana 
ou datas em um calendário.

'''

# Declarando uma tupla
tupla = (1,2,3)

# Podemos utilizar métodos que já conhecemos nas tuplas, como index, type, len e etc
print(tupla.index(2)) # O index do valor 2 é 1
print(tupla.count(2)) # Vamos contar quantas vezes aparece o número '2'

# Como acessar as informações de uma tupla
print(tupla[2]) # da mesma maneira que numa lista normal

# Diz no curso que a tupla não tem muitos métodos

# A tupla não possui método append e nem admite novos elementos a partir de -> tupla + ('item qualquer')