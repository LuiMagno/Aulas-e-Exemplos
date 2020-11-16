# Aula sobre Números - No python o foco é dado em cima de dois tipos principais de números, inteiro e ponto flutuante
# 2 e -2 são exemplos de inteiros, já 3.14 e 9.99 são exemplos de ponto flutuantes.
# Agora veremos alguns exemplos de aritmética básica dados na Aula de número 10.

# Soma
print(2+1)
# Subtração
print(2-1)
# Multiplicação
print(2*2)
# Divisão
print(3/2)
# Especificando um número como um float (ponto flutuante)
print(4.0/2)
# Funciona para os dois números
print(3/2.0)
# Potência
print(2**3)
# Um forma alternativa de fazer raiz quadrada
print(4**0.5) 
# Ordem das operações matemáticas em python respeita a formalidade matemática
print(2+10*10+3)
# Também podemos usar parênteses para definir a ordem desejada
print((2+10) * (2+10))

# Aqui tratamos sobre o básico da atribuição. Ou seja, se atribuírmos um número a uma variável x, ele pertencerá a ele.
x = 5
print(x+x)

# Ele muda até usarmos uma redefinição apropriada
x = x+x
print(x)

# Existem algumas regras para a atribuição em Python: 1. Não pode-se começar com números, 2. Não pode haver espaço entre os nomes, 
# ao invés disso use o _, 3. Não é possível usar caracteres especiais, 4. É considerado a melhor prática nomes minúsculos - Segundo o 
# Pep8(melhores práticas para Python)

meu_salario = 100
tax_imposto = 0.1
minha_taxa = meu_salario*tax_imposto
print(minha_taxa)

# Método Python : type(0) mostra o tipo do número inserido como argumento
x = 3.14

print(type(x))

# Próxima aula -> Strings
# Código de Fatorial
i = 0
produto = 1
n = int(input())
int(n)

while i < n:
    i += 1
    produto = (produto*i)

print("Número fatorial é =", produto)


