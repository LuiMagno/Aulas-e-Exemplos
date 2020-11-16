def func():
    return 1

print(func())

s = 'Global Variable'

def funcs():
    a = 1
    print(locals()) #Permite que print as variáveis locais

funcs()
print(globals()) # Mostra todas as variáveis globais

def hello(nome = 'Rodrigo'):
    return 'Olá, '+ nome

print(hello())

boasvindas = hello #Aqui eu atribuo uma função a uma variável, toda vez que eu chamar a função boasvindas() eu terei executado a função hello()

print(boasvindas())


# Criando funções dentro de funções

def helloLui(nome = 'Lui'):
    print('Olá, '+ nome)
    def tudoBem():
        print('Tudo bem?')
    def comoEsta():
        print('Como você está?')
    #print(locals())
#helloLui()

# E como podemos retornar um função?

def helloLui2(nome = 'Lui'):
    print('Oláaa, '+ nome)
    def tudoBem():
        print('Tudo bem?')
    def comoEsta():
        print('Como você está?')
    if nome == 'Lui': 
        return tudoBem  #Ou seja, existe o conceito de retornar uma função em Python, e isso é importante para entedermos decoradores
    else:
        return comoEsta
helloLui()

print(helloLui2())

# Vamos agora um exemplo de função sendo chamada como parâmetro de outra função

def olar(func):
    print('Fala mano, ')
    func()

def eai():
    print('beleza?')

# Agora eu chamo a função olar() e como argumento eu mando a função eai(), fazendo assim uma função ter como argumento outra e essa outra ser executada. 

olar(eai)

# Aprendendo decorador

def novo_decorador(func):
    def funcao_interna():
        print('Código executado antes da função!')
        func()
        print('Código executado depois da função!')
    return funcao_interna

def precisa_decorar():
    print('Essa funcao precisa de decorador!')
    #Um decorador vai alterar uma função e devolver ela

novo_decorador(helloLui)()

# Vamos ver a definição de decorador pelo notebook e tentar entender por algum outro vídeo da internet