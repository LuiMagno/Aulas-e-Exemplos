'''
Sets
Os conjuntos são uma coleção não ordenada de elementos únicos. Podemos construí-los usando a função set(). Avançemos e façamos um 
conjunto para ver como funciona

'''
# O set() possui apenas unidades únicas, ou seja, não aceita mais de um elemento igual.

x = set()
x.add(1)  #Adicionando 1 
print(x)
x.add(2)
x.add(1)  #Repetindo a adição do 1 e vendo que ele não é inserido no set(). O set ocupa apenas elementos exclusivos.
print(x)

lista = [11, 11, 11, 22, 33, 1, 2]

set_lista = set(lista) 

print(set_lista) #Aqui vimos que atribuir uma lista ao set() faz com que ele se crie apenas com elementos exclusivos

# De Booleanos já sabemos demais, essa parte do curso não ensina nada demais que eu não saiba, apenas o None
b = None