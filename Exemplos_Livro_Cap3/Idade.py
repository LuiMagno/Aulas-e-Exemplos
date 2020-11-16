# idade para votar 16+ e idade para dirigir 18+, leia o ano de nascimento, calcule a idade e dê as informações
import datetime

anoNascimento = int(input('Entre com a sua data de nascimento: '))
dataAtual = datetime.datetime.now()
if (dataAtual.year-anoNascimento)>= 16:
     print('Parabéns, já pode dirigir!')
else:
   print('Você não tem idade suficiente para dirigir!')

if (dataAtual.year-anoNascimento)>= 18:
    print('Parabéns, já pode votar!')
else:
    print('Você não tem idade suficiente para votar!')

