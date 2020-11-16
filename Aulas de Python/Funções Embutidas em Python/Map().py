'''
Uma função iterável que usa como argumento uma outra função e um iterável
'''

def fahrenheit(T):
    return (9/5) * T + 32


temp = [9, 22, 40, 90, 120]

temp_f = []
for temperature in temp:
    temp_f += [fahrenheit(temperature)]

listaTemperaturas = list(map(fahrenheit, temp)) #Reduzindo o trabalho de várias linhas para só uma linha
print(listaTemperaturas)

# Temos um método de simplificar ainda mais

lista3 = list(map((lambda t: (9/5) * t + 32), temp)) #Aqui usamos lambda para eliminar o uso de uma função e usamos junto dele o map para aplicar em uma lista
print(lista3)