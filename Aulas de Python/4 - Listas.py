# Anteriormente, na aula de Strings, introduzimos o conceito de sequência em Python. Os elementos de uma Lista, diferente de Python, são mutáveis!
# Aqui um pequeno roteiro sobre o que vamos estudar nessa aula em Python:
# 1. Criação de Listas
# 2. Índice e corte de listas
# 3. Métodos básicos da Lista
# 4. Lista Aninhadas
# 5. Introdução ao método de Compreensão em listas
# 
# As listas são construídas em colchetes [] e vírgulas separam cada elemento dela.

# 1 - Criação de Listas - Atribuindo uma lista a uma variável
my_list = [1,2,3] 
# Uma lista em Python pode armazenar diferentes tipos de de objeto
my_list = ['A string', 23, 100.232,'o']
# Assim como em uma string, a função len() também irá informar qual tamanho da nossa lista
print(len(my_list))

# 2 - Indexação e Corte
# Indexar e cortar funciona exatamente como em strings. Vamos fazer uma nova lista para ver como funciona
my_list = ['one','two','three', 4 , 5]

# Pegar o elemento do índice 0
print(my_list[0])

# Pegar o índice 1 e tudo depois
print(my_list[1:])

# Pegar tudo até o elemento do índice 3
print(my_list[:3])

# Nós também podemos utilizar o + para concaternar listas, assim como fizemos em strings
my_list + ['new item'] # Isso não altera a lista original, como podemos ver no print a seguir ->
print(my_list)

# Para a mudaça permanente, precisamos reatribuir a lista
my_list = my_list + ['add new item permantly']
print(my_list)

# Também podemos usar o * para um método de duplicação semelhante às strings
print(my_list*2)

# 3 - Métodos de Lista Básica 
# Duas características importantes das Listas em Python -> Não é preciso definir o tamanho nem o tipo! 
# Vamos a métodos básicos da Lista em Python
# Criar uma lista
lista = [1,2,3]

# Append - adicionar um objeto ao final da lista
lista.append("append me!")
print(lista)

# Pop - retira o último item da lista, mas pode também tirar um objeto definido no parâmetro da função
lista.pop()
lista.pop(0)
print(lista)

# Vamos agora atribuir um elemento retirado da lista, lembrando que o índice padrão é -1 (o último do vetor)
lista.append("append me!")
popped_item = lista.pop()
print(popped_item)

# Lembrando que o programa retornará um erro caso a posição solicitada da lista estiver vazia, como um 'print(lista[100])', por exemplo.
# Podemos usar os métodos 'sort' e 'reverse' para alterar listas
nova_lista = ['a', 'c', 'e', 'b', 'd']
nova_lista.reverse()
print(nova_lista)

# Método Sort ordena a lista de string por ordem alfabética
nova_lista.sort()
print(nova_lista)

# 4 - Lista Aninhadas
# Uma ótima característica das estruturas de dados do Python é que eles suportam "aninhamento". Isso significa que podemos  ter estruturas de dados dentro
# das estruturas de dados. Por exemplo: uma lista dentro de outra lista. Vamos ver como isso funciona:

lista_1= [1,2,3]
lista_2= [4,5,6]
lista_3= [7,8,9]
# Formando uma lista de listas
matriz = [lista_1, lista_2, lista_3]
print(matriz)

# Agora temos dois níveis dentro do meu novo objeto Matriz, para pegar a primeira lista, fazemos:
print(matriz[0])
# Se quisermos pegar um item específico da primeira lista da matriz, precisamos mandar os parâmetros para dois níveis
print(matriz[0][0])

# 5 - Comprenssão de Listas
# Compreensão de Listas seria um método mais rápido de criar uma lista (método esse que será entendido com mais clareza mais na frente)

first_col =[row[0] for row in matriz] # Basicamente formamos uma lista 'first_col' para pegar o primeiro objeto de cada lista dentro da matriz, assim
print(first_col) # imprimindo [1,4,7]