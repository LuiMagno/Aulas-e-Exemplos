
def main():
    while True:
        print('Bem-vindo ao Jogo da Velha do Lui!!!\n','Jogador 1 joga com X\n', 'Jogador 2 joga com O' )
        mostrar_board(board)
        jogar()
        print('Fim de Jogo!')
        if not replay():
            print('Até mais!')
            break
    
def replay():
    return input('Quer jogar novamente? "SIM" ou "NAO"  - > ').lower().startswith('s') #se começar com s vai retornar True, pela função startswith()    

def mostrar_board(board): # mostrando o placa do jogo da velha
    for c in range(0,9):
        if c%3 == 0:
            print('')
        print(f'|{board[c]:^5}|', end='')
    print()

def checar_jogo():# checando se alguém ganhou ou deu velha
    if  (board[0] == board[1] == board[2])    or  \
        (board[0] == board[3] == board[6])    or  \
        (board[0] == board[4]  == board[8])   or  \
        (board[3] == board[4]  == board[5])   or  \
        (board[6] == board[7]  == board[8])   or  \
        (board[2] == board[5]  == board[8])   or  \
        (board[2] == board[4]  == board[6])   or  \
        (board[1] == board[4]  == board[7]):
        return True
    else:
        velha = 0
        for x in board:
            if x != 'X' and x != 'O': #se tiver algo diferente de X e O, 'velha' será incrementada
                velha += 1
        if velha == 0:
            return False
            
def jogar(): #jogando
    while True:
        fazer_jogada(1)
        mostrar_board(board)
        if checar_jogo():
            print('Jogador 1 é o vencedor!!!')
            break
        elif checar_jogo() == False :
            print('Deu velha!')
            break
    
        fazer_jogada(2)
        mostrar_board(board)
        if checar_jogo():
            print('Jogador 2 é o vencedor!!!')
            break
        elif checar_jogo() == False:
            print('Deu velha!')
            break

def fazer_jogada(jogador):
    invalida = True
    print('Jogador', jogador, 'faça sua jogada!')
    while invalida:
        jogada1 = int(input())
        if board[jogada1-1] == 'X' or board[jogada1-1] == 'O':
            print('Jogada inválida! Escolha novamente.')
        else:
            invalida = False
            if jogador == 1:
                board[jogada1-1] = 'X'
            else:
                board[jogada1-1] = 'O'

board = [1,2,3,4,5,6,7,8,9]
main()
