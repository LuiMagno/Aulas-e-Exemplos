def primeira_funcao():
    # printa 'Olá, Mundo!'
    
    print('Olá, Mundo!')
    pass 

primeira_funcao() #se você segurar 'ctrl' o VSCODE irá mostrar a você a função que foi escrita 

# argumentos de função são valores passados pra função para definir as informações com que a função deve trabalhar.
# evitar funções padrão do Python

def somar(num1,num2):
    return (num1+num2)

print(somar(4, 3))


def primo(num):
    '''
    Método para checar primos
    '''
    for n in range(2,num):
        if num % n == 0:
            print('Não é primo!')
            break
    else:                    # Procurar 'else' funcionando de forma diferente      
        print('É primo!')
            
# INFORMAÇÃO IMPORTANTE -> O 'ELSE' identado do jeito que está acima só ocorre na última interação dentro do for, ou seja, ele ocorre
# de forma diferente do 'else' indentado na mesma posição do 'if', onde nesse caso ele faz o teste em todos os casos
while True:
    num = int(input('Insira um número para saber se é primo:'))
    if num == 0:
       break
    else:
        primo(num)

# Podemos ter funções dentro de funções 

'''
Vou colocar aqui também um comentário sobre Métodos, que são funções de objetivos específicos, como no rápido exemplo:
'''

vetor = [1,2,3,4]
vetor.append(5) # aqui temos um método do objeto do tipo 'list', esse método é o 'append'
