'''
O que a função zip() é juntar dois outros iteráveis e formar tuplas
'''

x = [1,3,5,7,9]
y = [2,4,6,8,10]

xy = list(zip(x,y)) #Formando um vetor de tuplas com os iteráveis x e y
print(xy)

# Vamos agora a um for interessante que o professor fez:

for i in zip(x,y):
    print(max(i))

