#Code done by Lui Magno 03/08/2020
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
import math
import random

class Jogador(object):
    def __init__(self,nome):
        self.nome = nome
        self.saldo = 0
        self.dealer = False
        self.cartas = []
        self.pontos = 0
        self.valorApostado = 0

    def definirSaldo(self, saldo):
        self.saldo = saldo

    def  adicionarSaldo(self,valor):
        self.saldo += valor

    def mostrarInformacoes(self):
        print('Jogador :', self.nome, '\nSaldo :', self.saldo)

    def getValorApostado(self):
        return self.valorApostado

    def setCartas(self, cartas):
        self.cartas += cartas

    def apostar(self):
        valorApostadoAtual = 0
        valorApostadoAtual = int(input('Quanto deseja apostar?\n')) 
        self.valorApostado += valorApostadoAtual
        if valorApostadoAtual > self.saldo:
            print('Saldo insuficiente, tente com outro valor ou continue o jogo.')
            valorApostadoAtual = 0
        else:
            self.saldo -= valorApostadoAtual
            print('Aposta em: ', self.valorApostado)
            print('Seu saldo é de: ', self.saldo)
            
    def gerenciarAposta(self):
        self.valorApostado = 0
        while True:
            escolha1 = input('O que deseja? 1 - Apostar  / 2 - Começar jogo / 3 - Checar Saldo \n')
            if escolha1 == '1':
               self.apostar()
            elif escolha1 == '2':
                if self.valorApostado < 10:
                    print('Você precisa apostar pelo menos 10 para começar o jogo!')
                    continue
                else:
                    print('Vamos começar!!!')
                    print('-'*50)
                    break
            elif escolha1 == '3':
                print('Seu saldo é de :', self.saldo)                  
            else:
                print('Escolha a opção 1 ou a opção 2')
        
    def darCartas(self, Baralho, numero):
        mao = []
        for x in range(0,numero):
            mao.append(Baralho.gerarCarta())
        return mao

    def mostrarCartas(self):
        naipe = []
        numero = []
        print('Cartas  de ', self.nome)
        for carta in self.cartas:
            if carta[1] == 0:
                naipe = 'Copas'
            elif carta[1] == 1:
                naipe = 'Espadas'
            elif carta[1] == 2:
                naipe = 'Ouros'
            else:
                naipe = 'Paus'

            if carta[0] == 1:
                numero = 'Ás'
            elif carta[0] == 11:
                numero = 'Valete'
            elif carta[0] == 12:
                numero = 'Rainha'
            elif carta[0] == 13:
                numero = 'Rei'
            else:
                numero = str(carta[0])
            print ('%s de %s'%(numero,naipe))
    
    def contarPontos(self):
        as1 = False
        self.pontos = 0 
        for carta in self.cartas:
            if carta[0] == 11 or carta[0] == 12 or carta[0] == 13:
                self.pontos += 10
            elif carta[0] == 1:
                self.pontos += 1
                as1 = True
            else:
                self.pontos += carta[0]
        if as1 == True and self.pontos <=11:
                self.pontos += 10
        print('Pontuação : ', self.pontos)
        print('-'*50)
        return self.pontos

class Baralho(object):
    def __init__(self):
        self.vetorBaralho = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13], [0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13]]
       
    def gerarCarta(self):
        carta =[]
        while True:
            cartaNaipe = math.ceil(4 * random.random()) - 1 
            cartaNumero = math.ceil(13 * random.random())
            if self.vetorBaralho[cartaNaipe][cartaNumero] == 0:
                continue
            else:
                carta = [cartaNumero,cartaNaipe]
                self.vetorBaralho[cartaNaipe][cartaNumero] = 0
                return carta
   
def main():

    baralho = Baralho()
    
    dealer = Jogador('Derek')
    dealer.dealer = True
    manterJogo = True
    print('Bem-vindo ao Black Jack Rebirth!')
    jogador1 = Jogador(input('Qual seu nome?\n'))
    jogador1.definirSaldo(int(input('Quanto deseja cadastrar?\n')))
    print('-'*40)
    print('Bem-vindo jogador %s! Seu saldo é de:  %s!'%(jogador1.nome,jogador1.saldo))
    while manterJogo:
        valorApostado = 0
        jogador1.gerenciarAposta()
        valorApostado = jogador1.getValorApostado()

        jogador1.setCartas(dealer.darCartas(baralho,2))
        jogador1.mostrarCartas()
        jogador1.contarPontos()

        dealer.setCartas(dealer.darCartas(baralho,1))
        dealer.mostrarCartas()
        dealer.contarPontos()

        if pegarOuManter(jogador1,dealer,baralho):
            print('Você perdeu.')
        else:
            julgarJogo(jogador1,dealer,valorApostado)
            jogador1.cartas = []
            dealer.cartas = []
        if terminarJogo(jogador1):
            manterJogo = False
        else:
            jogador1.cartas = []
    print('Até a próxima!')
    
def pegarOuManter(jogador,dealer,baralho):
    estouro = False
    while True:
        escolha2 =  input('O que deseja fazer? 1 - Pegar mais uma carta 2 - Manter\n')
        if escolha2 == '1':
            jogador.setCartas(dealer.darCartas(baralho,1))
            jogador.mostrarCartas()
            if jogador.contarPontos() > 21:
                print('Estorou! Não pode mais pedir cartas')
                estouro = True
                break
        elif escolha2 == '2':
            pontosJogador = jogador.contarPontos()
            pontosDealer = dealer.contarPontos()
            while pontosJogador > pontosDealer:
                dealer.setCartas(dealer.darCartas(baralho,1))
                dealer.mostrarCartas()
                pontosDealer = dealer.contarPontos()
            break
    if dealer.pontos > 21:
        ('Dealer estorou!')
        dealer.pontos = 0
    if estouro:
        return True
    else:
        print('Escolhas terminadas! Vamos ao resultado!')
        return False
    
def julgarJogo(jogador,dealer,valorApostado):
   
    if jogador.pontos > dealer.pontos:
        print('Jogador %s venceu!!! Ganhou um total de %s!' %(jogador.nome, valorApostado))
        
        jogador.adicionarSaldo(valorApostado*2)
    elif jogador.pontos < dealer.pontos:
        print('Infelizmente você perdeu! Menos %s no seu saldo.'%(valorApostado))
        
    else:
        print('Empate! Seu dinheiro será devolvido.')
        jogador.adicionarSaldo(valorApostado)
def terminarJogo(jogador):
    escolha3 = input('Deseja continuar jogando? 1 - Sim 2 - Não\n')
    if escolha3 == 1:
        return False
    elif escolha3 == 2:
        return True
main()

