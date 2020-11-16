#  1 - Crie um gerador que gere os quadrados de números até um número N.

def square(n):
    for num in range(n):
        yield num ** 2

for i in square(10):
    print (i)
print('*'*50)
# 2 - Crie um gerador que produza "n" números aleatórios entre um número baixo e alto (que são entradas). Nota: use a biblioteca random. Por exemplo:
import random
from math import ceil

def randomGerator(n,baixo,alto):
    for num in range(n):
        yield random.randint(baixo,alto) 

for i in randomGerator(5,1,10):
    print(i)
print('*'*50)

# 3 - Use a função iter() para converter a string abaixo

s = 'Diabolical'
s = iter(s)
print(s)

for i in s:
    print(i)

# 4 - Explique um caso de uso para um gerador usando uma declaração yield onde você não deseja usar uma função normal com uma declaração de retorno.
# Um caso de uso que eu vejo possível de ser aplicável usando o gerador, e até possivelmente ver um ganho, é em algum banco de dados grande que precisa ser testado dentro
# do próprio código, como criar um novo vetor com os carros que tiverem a placa com início V. Gerenciar um vetor gigantesco seria muito trabalhoso.