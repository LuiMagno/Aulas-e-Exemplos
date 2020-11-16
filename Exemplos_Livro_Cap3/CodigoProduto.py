# Algoritmo que corresponda o número do produto com seu tipo (tentar usar o switch)
codigoProduto = int(input('Insira o código do produto: '))
print({
    1: 'Alimento não-perecível',
    2: 'Alimento perecível',
    3: 'Alimento perecível',
    4: 'Alimento perecível',
    5: 'Vestuário',
    7: 'Higiene Pessoal',
    8: 'Limpeza e utensílios domésticos'
}[codigoProduto])



# Isso é o mais próximo que temos de um switch em python

# if e switch é essencialmente a mesma coisa. O único ganho real dele é a otimização que algumas linguagens fazem, mas faz pouco sentido em Python. O switch pode ter um custo de sintaxe mais alto em alguns casos. Algumas linguagens colocam funcionalidade extra no switch.
# Eu uso uma linguagem que o switch não traz vantagens. Prefiro usar o if mesmo.
# switch não é uma função é um comando de linguagem.