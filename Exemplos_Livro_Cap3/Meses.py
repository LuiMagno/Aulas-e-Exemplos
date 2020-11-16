# Escreva um algoritmo que a partir de um mês fornecido( de 1 a 12) apresente o nome dele por extenso ou mensagem de mês inválido
mesEscolhido = int(input('Insira o mês: '))
if mesEscolhido>0 and mesEscolhido<13:
    print({
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }[mesEscolhido])
else:
    print('Mês inválido')