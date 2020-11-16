
# Escreva uma função que calcula o volume de uma esfera dado seu raio.
def volume_esfera(rad):
    volume = (4/3) * 3.14 * (rad**3)
    return volume

print(volume_esfera(3))

# Escreva uma função que verifica se um número está em um determinado intervalo (inclusive o máximo e mínimo)

def ran_check(num,min,max):
    if num in list(range(min,max+1)):# forma que fiz if num>min and num<max:
        return True
    else:
        return False

num = 14
min = 1
max = 10
print(ran_check(num,min,max))

# Escreva uma função Python que aceita uma string e calcule o número de maiúsculas e minúsculas. 
string = 'Olá, Mundo!'

def checar_strings(string):
    numMaisculas = 0
    numMinusculas = 0
    for char in string:
        if char.isupper():
            numMaisculas +=1
        elif char.islower():
            numMinusculas +=1
        else:
            continue
    print('Número de Minúsculas: ', numMaisculas )
    print('Número de Maiúsculas: ', numMinusculas)

checar_strings(string)

# Escreva uma função Python que recebe uma lista e retorna uma nova lista com elementos exclusivos da primeira lista.
lista = [1,1,1,1,2,2,3,3,3,3,4,5]

def list_to_set(lista):
    return set(lista)

print(list_to_set(lista))

# Escreva uma função Python para multiplicar todos os números em uma lista. 

def multiplicar_lista(lista):
    resultado = 1
    for num in lista:
        resultado = resultado*num
    return resultado

lista = [1,2,3,-4]
print(multiplicar_lista(lista))

# Escreva uma função Python que verifica se uma string passada é palindrome ou não.

def checar_palindromo(string):
    palavra = string.lower()
    return palavra == palavra[::-1]

print(checar_palindromo('Otto'))

# Escreva uma função Python para verificar se uma string é um pangrama ou não. (Difícil).
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''
Explicando a função abaixo: 
'''
def ispangram(string):
    '''
    Explicando a função abaixo:
    Função que verifica se uma frase/palavra é Pangrama ou não 
    '''
    count = 0 # contador para checar se temos 26 letras iguais na 'string' e no vetor 'alfabeto'
    for aux in string: # pegar uma letra da 'string'
        for num in range(0,26): # pegar uma letra do vetor 'alfabeto'
            if alfabeto[num] == aux : # se a letra do alfabeto for igual a letra da 'string'
                count += 1 # incrementamos o contador
                alfabeto[num] = 0 # e excluímos ele do vetor alfabeto, para não admitir palavras repetidas
    if count == 26:
        print('A palavra/frase é Pangrama')
    else:
        print('A palavra/frase não é um Pangrama')

ispangram("The quick brown fox jumps over the lazy doooog")
ispangram("The quick brown fox jumps the lazy dog")

# Refazendo o código Pangrama para uma forma mais 'limpa' usando set()

import string
def ispangramset(str, alphabet=string.ascii_lowercase): # Utilizando 'string.ascii_lowercase' para receber o alfabeto em minúsculo
    alphaset = set(alphabet) # fazendo um set() no alphabet para retirar os elementos repetidos e torna o alphabet num vetor de elementos não repetidos
    return alphaset <= set(str.lower()) # retornando e chegando se o alphaset 

print(ispangramset('The quick brown fox jumps over the lazy doooog'))
print(ispangramset('The quick brown fox jumps over the lazy cat'))

def ispangram2(str, alphabet = string.ascii_lowercase):
    num = len(alphabet)
    count = 0
    for i in alphabet:
        if i in str: # aqui podemos ver como o Python trata o 'in', se a letra i de 'alphabet' estiver em str, é verdadeiro, executa a ação
            count +=1
        return count == num # retorna true se o contador for igual ao número de elementos em 'alphabet'

print(ispangramset('The quick brown fox jumps over the lazy doooog'), 'mama mia')