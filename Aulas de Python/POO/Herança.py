class Animal(object):
    def __init__(self):
        print('Animal criado.')
    def quemSouEu(self):
        print('Eu sou um animal.')
    def comer(self):
        print('Comendo...')

leao = Animal()
leao.quemSouEu()
leao.comer()

class Cachorro(Animal): #tornar código mais simples reutilziando classes com Herança
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criado.')
    def quemSouEu(self):
        print('Eu sou um cachorro.')
    def latir(self):
        print('Au au...')

Jooj = Cachorro()
Jooj.quemSouEu()
Jooj.latir()
Jooj.comer()    
