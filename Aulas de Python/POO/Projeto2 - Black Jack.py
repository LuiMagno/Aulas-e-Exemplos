'''
Criar um Jogo de Black Jack(21) baseando-se nas seguintes exigências:
1. Criar o Jogo Black Jack baseando-se em texto
2. Um jogador contra um dealer automatizado
3. O jogador pode esperar ou pedir mais cartas
4. O jogador deve poder escolher o seu valor de apostas
5. Você precisa acompanhar o dinheiro total dos jogadores
6. Você precisa alertar os jogadores de vitórias, perdas e etc...

*** Você deve usar POO e classes em alguma parte do jogo. Você não pode apenas usar funções. Use aulas para ajudá-lo a definir o baralho e a mão do jogador. 
'''
import random
import math

class Jogador(object):
    '''
    Classe de Jogador - Responsável por guardar nome, saldo no jogo e gerar cartas e pontuação
    '''
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.cartas = []
        self.pontos = 0
        print('Jogador "%s" cadastrado!'%(self.nome))
        print('-'*40)
    def getSaldo(self):
        return self.saldo

    def sacar(self,valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            return True

    def definirCartas(self,carta):
        self.cartas.append(carta)
    
    def mostrarCartas(self):
        especial = ''
        naipe = ''
        for carta in self.cartas:
            if carta[1] == 1:
                especial = 'As'
            elif carta[1] == 11:
                especial = 'Valete'
            elif carta[1] == 12:
                especial = 'Rainha'
            elif carta[1] == 13:
                especial = 'Rei'
            else:
                especial = carta[1]
            
            if carta[0] == 0:
                naipe = 'Copas'
            elif carta[0] == 1:
                naipe = 'Paus'
            elif carta[0] == 2:
                naipe = 'Espadas'
            elif carta[0] == 3:
                naipe = 'Ouros'
            print('%s de %s'%(especial, naipe))

    def checarPontuacao(self):
        ases = False
        self.pontos = 0
        for carta in self.cartas:
            if (carta[1] == 11) or \
                (carta[1] == 12) or \
                (carta[1] == 13):
                self.pontos += 10
            else:
               self.pontos += carta[1]

            if carta[1] == 1:
                ases = True
        if ases == True and self.pontos <= 11:
            self.pontos += 10
        print('**** Pontuação : %s ****\n'%(self.pontos))
        if self.pontos > 21:
            print('Estorou papai')
            return True
        else:
            return False
       
    def retornarPontuacao(self):
        return self.pontos

class Dealer(object):
    '''
    Classe responsável pelo Dealer, onde temos nome, as cartas da mesa, o baralho e a pontuação da casa
    '''
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []
        self.baralho = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13], [0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13]]
        self.pontos = 0
        print('Olá, sou %s, e serei seu Dealer nesta partida!'%(self.nome))
   
    def definirCartas(self,carta):
        self.cartas.append(carta)

    def mostrarCartas(self):
        especial = ''
        naipe = ''
        for carta in self.cartas:
            if carta[1] == 1:
                especial = 'As'
            elif carta[1] == 11:
                especial = 'Valete'
            elif carta[1] == 12:
                especial = 'Rainha'
            elif carta[1] == 13:
                especial = 'Rei'
            else:
                especial = carta[1]
                
            if carta[0] == 0:
                naipe = 'Copas'
            elif carta[0] == 1:
                naipe = 'Paus'
            elif carta[0] == 2:
                naipe = 'Espadas'
            elif carta[0] == 3:
                naipe = 'Ouros'
            print('%s de %s'%(especial, naipe))
            
    def comecarJogo(self, Jogador):
        '''
        Método responsável pelas apostas e pelo começo do jogo (dar as cartas)
        '''
        valorApostado = 10
        print('Aposta em ', valorApostado)
        while True:
            escolha = input('O que deseja fazer?\n 1 - Aumentar Aposta \n 2 - Dar cartas \n')
            if escolha == '1':
                print('Seu saldo é: ', Jogador.getSaldo())
                valor = int(input('Qual valor deseja aumentar?\n'))
                if Jogador.sacar(valor):
                    valorApostado += valor
                    print('Aposta em ', valorApostado)
                else:
                    print('Saldo insuficiente, escolha outro valor ou comece o jogo.')
            if escolha == '2':
                break
            
    def gerarCarta(self,Owner,numeroCartas):
        num = 0
        while num < numeroCartas:
            carta = self.randomCarta()
            naipe = carta[0]
            numero = carta[1]
            if naipe == 0: # Copas
                self.baralho[naipe][numero] = 0
                Owner.definirCartas(carta)
            elif naipe == 1: # Paus
                self.baralho[naipe][numero] = 0
                Owner.definirCartas(carta)
            elif naipe == 2: # Espadas
                self.baralho[naipe][numero] = 0
                Owner.definirCartas(carta)
            else:   # Ouros
                self.baralho[naipe][numero] = 0
                Owner.definirCartas(carta)
            num += 1

    def darCartas(self, Jogador,numero):
        self.gerarCarta(Jogador,numero)
        Jogador.mostrarCartas()

    def randomCarta(self):
        while True:
            naipe = (math.ceil(4* random.random())-1)
            numero = (math.ceil(13* random.random()))
            if self.baralho[naipe][numero] == 0:
                continue
            else:
                carta = [naipe,numero]
                return carta
        
    def checarPontuacao(self):
        ases = False
        self.pontos = 0
        for carta in self.cartas:
            if (carta[1] == 11) or \
                (carta[1] == 12) or \
                (carta[1] == 13):
                self.pontos += 10
            else:
               self.pontos += carta[1]

            if carta[1] == 1:
                ases = True
        if ases == True and self.pontos < 11:
            self.pontos += 10
        print('**** Pontuação : %s ****\n'%(self.pontos))
        if self.pontos > 21:
            print('Estorou papai, perdeu fdp')
            return True
        else:
            return False
   
    def retornarPontuacao(self):
        return self.pontos    
    
    
def main():
    while True:
        escolhaJogador = True
        escolhaDealer = True
        nomeJogador = input('Bem-vindo ao Black Jack!\nQual seu nome?\n')
        saldoJogador = int(input('Qual quantia deseja cadastrar?\n'))
        jogador1 = Jogador(nomeJogador,saldoJogador)
        Derek = Dealer('Derek')

        Derek.comecarJogo(jogador1)
        print('Suas cartas', jogador1.nome)
        Derek.darCartas(jogador1,2)
        jogador1.checarPontuacao()

        print('Carta do Dealer')
        Derek.darCartas(Derek,1)
        Derek.checarPontuacao()

        while escolhaJogador: # while do jogador
            temp = input('\nO que deseja: \n 1 - Mais uma carta \n 2 - Esperar \n')
            print('-'*50)
            if temp == '1':
                Derek.darCartas(jogador1,1)
                if jogador1.checarPontuacao():
                    break
                Derek.mostrarCartas()
                Derek.checarPontuacao()
                escolhaJogador = True

            else:
                escolhaJogador = False
        
        while escolhaDealer:
            if Derek.retornarPontuacao() > jogador1.retornarPontuacao():
                print('Dealer venceu pae')
                break
            else:
                print('Agora vamos ás cartas do Dealer!')
                Derek.darCartas(Derek,1)
                Derek.checarPontuacao()
                
        print('Fim de Jogo\n', '*'*50)




main()