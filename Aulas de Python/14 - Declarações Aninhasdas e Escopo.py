''' 
Como Python enxerga suas variáveis?
'''
# No exemplo a seguir, vamos ver 2 tipos de escopos diferentes

x = 25 # esse é uma variável global

def printer():
    x = 50 # isso é uma variável local da função
    return x

print(x)        # temos x na definição inicial do código
print(printer())# temos x na definição do escopo da função 'printer'
# print é uma função built in
'''
Existem 3 regras gerais para definir a ideia de escopo em Python
1. As atribuições de nomes criam ou alteram nomes locais por padrão
2. Existem 4 possíveis scopes. São eles:
    1. Local
    2. Enclosing functions
    3. Global
    4. Built-in
3. Os nomes declarados em declarações globais e não locais mapeiam nomes atribuídos para preencher módulos e escopos de função
Regra LEGB
Local
Enclosing
Global
Built-in
'''
# Agora vamos a um exemplo de acesso as variáveis de tipos de declarações diferentes

name = 'Este é um nome global' # nome global

def greet():
    name = 'Sammy' #nome da segunda regra, enclosing
    def hello():
    #name = 'joao' isso seria procurar um nome pela regra: primeiro local, mas como não tem, ele vai pra próxima; Enclosing Functions
        print('Hello ' +name)
    hello()

greet()
print(name) #print, nome built-in