# Métodos são funções internas da Classe
class Dog(object):
    species = 'mamifero'
    def __init__(self,raca):
        self.raca = raca
    
    def latir(self):
        print ('Auau')

Jooj = Dog('Ruim')
Jooj.latir()

class Circulo(object):
    pi = 3.14
    def __init__(self,raio):
        self.raio = raio
    
    def area(self):
        return self.raio ** 2 * self.pi
    
    def defRaio(self,raio):
        self.raio = raio
    
    def obtemRaio(self): #sempre use o 'self' como parâmetro pra manipular o objeto dentro do método dentro da própria classe do objeto
        return self.raio

c = Circulo(5)
c.defRaio(3)
print(c.area())

raio_c = c.obtemRaio() # aqui usamos o 'return' para atribuir o raio a variável 'raio_c'
