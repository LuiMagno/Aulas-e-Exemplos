# Em Python, tudo é um objeto. Lembre-se de palestras anteriores que podemos usar o type() para verificar o tipo de objeto de algo.
# Python é uma linguagem orientada á objeto
print(type(1))
print(type([]))
print(type(()))
print(type({}))

l = [1,2,3] # essa lista l é instância de uma classe de lista
print(type(l))

# Até mesmo um número o Python observa como um objeto da classe inteiro
x = 1
print(type(x))

# Agora vamos criar Classes

class Sample(object):
    pass

x = Sample()
print(type(x))

class Dog(object):
    especie = 'mamífero' # assim como uma função, minha classe pode ter variáveis próprias 
    def __init__(self, raca): #construtor 
        self.raca = raca

Jooj = Dog(raca='Pé duro safad')
print(Jooj.raca)

Frank = Dog('Huskie')

print(Frank.raca)
print(Frank.especie)