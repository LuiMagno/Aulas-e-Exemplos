'''
Namedtuple
'''
# Vamos relembrar primeiro como uma tupla funciona:     (a diferença básica entre uma tupla e uma lista é que a tupla é imutável)

t = (12,13,14)
print(t[0]) # Em todos os iteráveis você vai utilizar os [], pois são tratados como listas

from collections import namedtuple
Dog = namedtuple('Dog', 'age breed name') # Como se fosse uma classe onde podemos acessar informações por índices
sam = Dog(age=2, breed='Huskie', name = 'Sam')
print(sam.age)

# Namedtuple parece muito com uma classe.