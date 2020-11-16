# print('Hello)
# Essa linha causa o erro de sintaxe -> EOL while scanning string literal, que quer dizer 'END OF LINE ERROR'

# É indispensável saber ler o que é um erro e de que tipo ele é, como por exemplo, 'SyntaxError' ser um erro de sintaxe

# Depurar um código é nada mais que debugar o código, usar uma função do interpretador para ler o funcionamento passo a passo

'''
A terminologia básica e a sintaxe usadas para lidar com erros no Python são as instruções 'try' e 'except'. O código que pode causar uma exceção é colocado no bloco 'try' e o
tratamento da exceção é implementado no * do bloco de código except. O formulário de sintaxe é:
    try:
        Você tenta fazer algo aqui...
    ...
    except ExceptionI:
        Se causar a ExceptionI, roda isso.
    except ExceptionII:
        Se causar a ExceptionII, roda isso.
    ...
    else:
        Se não causar excessões, roda isso.
'''
try:
    file = open('testefile', 'r')
    string = ('A confiança gera muito mais ignorância do quê conhecimento')
    file.write(string)
except: # Aqui poderíamos escrever IOError para capturar o tipo específico de erro, mas o except captura no geral, temos aqui a opção.
    print('Erro ao tratar o arquivo.')
else:
    print('Não ouve erro')


try:
    file2 = open('testefile2', 'w')
    file2.write('Só sei que nada sei')
finally:
    print('Sempre será executado, independente do erro.')

def askint():
    while True:
        try:
            val = int(input('Entre com um inteiro: '))
        except:
            print('Erro, usuário não entrou com um inteiro.')
            continue
        else:
            print('Boa, é um inteiro')
            break
        finally:
            print('manga com sal')
        print(val)

askint()