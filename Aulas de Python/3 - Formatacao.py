# Nesta aula abordaremos brevemente várias maneiras de formatar declarações impressas. A partir do momento em que você codifica mais e mais
# é preciso ter formas de declarar impressões para incluir variáveis em uma declaração de string impressa.

# Podemos utilizar o %s para formatar strings em suas instruções de impressão.

s = "STRING"

print("Place another string with a mod and s: %s"%(s)) # Basicamente é inserir uma string de variável em uma declaração de impressão.

# Número de ponto flutuante
# Podemos printar os números no formato de %n1.n2f onde n1 é o número mínimo total de dígitos que a cadeia deve conter, caso não tenha são substituídos
# por espaços em branco, e n2 é o número máximo de números depois do ponto decimal. Alguns exemplos:
n = 3.14159265
print("1.Floating point numbers: %1.2f" %(n))
print("2.Floating point number: %1.0f" %(n))
print("3.Floating point number: %1.5f" %(n))
print("4.Floating point number: %10.2f" %(n))
print("5.Floating point number: %25.2f" %(n))

# Métodos de Conversão
# %s e %r convertem qualquer objeto Python em uma string usando dois métodos separados str() e repr()
print("Here is a number: %s. Here is a string: %s" %(3.14159, "hi"))

# Formatação Múltipla
# Passe uma tupla para junto com o símbolo do módulo para colocar vários formatos nas suas declarações de impressão
print("First: %s, Second: %1.2f, Third: %r" %("hi!",3.14,22))

# Usando o método string.format()
# A melhor maneira de formatar objetos em suas strings para instruções de impressão é usar o método format(). A sintaxe é:
# "String aqui {var1} e também {var2}".format(var1 = "something1", var2 = "something2") - Vamos a alguns exemplos:
print("This is a string with an {p}".format(p = "insert"))
print("One: {p}, Two: {p}, Three: {p}".format(p='hi!'))
print("Object One: {a}, Object Two: {b}, Object Three: {c}".format(a= 1, b= 'Dois', c=3.00))

# Próxima aula: Listas


# Erro encontrado ao usar o método 'format' -> Não podemos usar números na hora de referenciar variáveis para o dicionário formado na
# função, então se faz o uso de letras.
# Exemplo do erro = print('One: {1}, Two: {2}, Three: {3}'.format(1='Hi!', 2='tomar', 3='no cu'))