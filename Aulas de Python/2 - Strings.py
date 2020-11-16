# Nessa aula estudaremos sobre Strings, seguindo estes passos:
# 1. Criando Strings
# 2. Impressão de coStringsrdas
# 3. Indexação e corte de strings
# 4. Propriedades da Cadeia de Caracteres
# 5. Métodos de Strings
# 6. Formatação de Impressão

# 1 e 2. Criando uma String e imprimindo uma string
string = 'hello world'
print(string) # print é um método padrão do python 
# podemos usar \n para imprimir uma nova linha e /t para criar um espaço maior
print('hello')
print('\n')
print('world')
print('Hello, \t world')
# Podemos utilizar o len() para definir quantos caracteres tem um string
print(len(string))

# 3. Indexação em Strings - Sabemos que strings são sequências de caracteres, podemos utilizar índices para chamar partes das sequências, no Python se
# após um objeto para chamar seu índice, devemos notar também que a indexação começa em 0 para Python, vamos para um exemplo de
# indexação, vamos mostrar a terceira letra da string
print(string[2])
# podemos também usar ':' para executar um corte e pegar tudo a partir de um ponto designado
print('lalala ô' ,string[2:]) # imprime a partir da terceira ou pula [0] e [1] e imprime [2]
# ou usar o ':' para definir até onde vai a indexação
print(string[:5]) # imprime até a quarta e para na quinta

# Também podemos utilizar índices negativos para retroceder a indexação
print(string[-2])
print(string[:-2])
# Podemos utilizar "::" para pegar espaçamentos no que for de interesse na string
print(string[::2])

# 4. Propriedades de Strings
# Uma string tem a propriedade de ser imutável, ou seja, a ela não pode ser atribuída nenhum tipo de novo caractere. O recurso que temos para mudar
# essa string é a concatenação
string = string + " I'm here, bitches"
print(string)
# Podemos utilizar multiplicação para criar repetições
letra = 'z'
print(letra*100)

# 5. Métodos embutidos em Strings
# Os objetos em Python geralmente possuem métodos internos. Chamamos a função na forma: objeto.método(parâmetros). Vamos a alguns métodos de Strings
# Coloca toda uma string em caixa alta
print(string.upper())
# Caixa baixa
print(string.lower())
# Divide uma string nos espaços em branco (padrão)
print('AQUI Ó \n')
print(string.split())
# Divide em um elemento específico
print(string.split("w"))

# 6. Formatação de impressão
# Método .format() serve para colocar uma string designada num espaço de chaves {}
print('inserindo uma string qualquer aqui {}'.format('String qualquer'))

# Próxima aula: Formatação de Impressão 
#\t insere um tab no texto