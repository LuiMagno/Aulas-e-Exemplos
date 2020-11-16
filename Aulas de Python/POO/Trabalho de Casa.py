# Problema 1 : Preencha os métodos da classe Line para aceitar coordenadas como um par de tuplas e retornar a inclinação e a distância da linha
class Line(object):
    def __init__(self, coor1, coor2): # coor1 = (x1,y1)  coor2 = (x2,y2)
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self): #distância das linhas
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        distancia = ( (x2-x1)**2 + (y2-y1)**2 )**0.5  # NUNCA USE ',' PARA NÚMEROS, SEMPRE USE '.', POIS A PORRA DO PADRÃO INTERNACIONAL PRA NÚMERO É COM '.'
        return distancia
    def slope(self): # inclinação das linhas
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        inclinacao = ((y2-y1) /(x2-x1))
        return inclinacao

coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1,coordinate2)
print(line.distance())
print(line.slope())

# Problema 2 : Preencha a classe Cylinder e faça com que os métodos funcionem

class Cylinder(object):
    def __init__(self, height,radius):
        self.height = height
        self.radius = radius

    def volume(self):
        volCyl = 3.14*(self.radius**2)*self.height
        return volCyl

    def surface_area(self):
        area = 2 * 3.14 * self.radius * (self.height+self.radius)
        return area

cil = Cylinder(2,3)
print(cil.volume())
print(cil.surface_area())
