'''
Geradores nos permitem gerar informação
As funções do gerador nos permitem escrever uma função que pode enviar de volta um valor e, em seguida, continuar de onde ele parou. Esse tipo 
de função se chama gerador em Python, permitindo gerar sequências de valores ao longo do tempo. Usamos o 'yield'. Rescurso de 'Suspensão de Estado'

'''

def gencubes(n):
    for num in range(n):
        yield num ** 3              

for x in gencubes(10): # É como se a função 'gencubes()' passada como parâmetro se tornasse um iterável e assim virando um vetor, que é o que temos como resposta.
    print(x)

# Um iterável normal já é carregado na memória, e um gerador não, ele aloca cada valor solicitado por vez.

def gencubes2(n):
    lst = []
    for num in range(n):
        lst += num ** 3
        return lst


def genfib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for num in genfib(10):
    print(num)

print(list(genfib(10)))

# Fazendo um código de Fibonacci simples

def fibon(n): 
    a = 1
    b = 1
    output = []
    for i in range(n):
        output += [a]
        a, b = b, a+b
    return output

for i in fibon(10):
    print(i)


'''
Ou seja, temos 10 linhas com o algoritmo normal e 6 linhas com yield
(linhas não necessariamente diminuem a complexidade do programa, mas provavelmente diminuem a quantidade de informação e ajuda no entendimento)
'''