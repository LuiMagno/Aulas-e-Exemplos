# Vamos estudar como o código otimizado do Professor funciona e ver se ele é mais eficiente do que o meu (provavelmente)
# O objetivo é aprender realmente o que é Python e programar de forma consciente e limpa

# Variáveis Globais
board = [' ']*10
game_state = True
announce = ''

def reset_board():
    # Essa função reseta o game e redefine o tabuleiro
    global board, game_state
    board = [' '] * 10
    game_state = True

def display_board():
    # Printa o tabuleiro
    for c in range(0,9):
        if c%3 == 0:
            print('')
        print(f'|{board[c]:^5}|', end='')
    print()

def win_check(board,player):
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
        return False

def full_board_check(board):
    if ' ' in board[1:]:
        return False
    else:
        return True

def ask_player(mark): #Perguntar onde por o símbolo, e checar sua validade
    global board
    req = 'Escolha onde por o: '+ mark
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print('Desculpe, escolha um número de 1 a 9')
            continue
        if choice not in range(1,10):
            print('Desculpe, por favor escolha um número de 1 a 9')
        if board[choice] == ' ':
            board[choice] = mark
            break
        else:
            print ('Esse espaço não está vazio')
            continue

def player_choice(mark):
    global board,game_state,announce
    announce = ''
    mark = str(mark)
    ask_player(mark)
    if win_check(board,mark):
        display_board()
        announce = mark + ' ganhou. Parabéns!'
        game_state = False
    display_board()

    if full_board_check(board):
        announce = 'Tie!'
        game_state = False
    return game_state, announce

def play_game():
    reset_board()
    X = 'X'
    O = 'O'
    while True:
        display_board()
        # Vez do Jogador 'X'
        game_state,announce = player_choice(X)
        print(announce)
        if game_state == False:
            break

        # Vez do Jogador 'O'
        game_state,announce = player_choice(O)
        print(announce)
        if game_state == False:
            break

        # Perguntar por novo jogo
        rematch = input('Would you like to play again? y/n')
        if rematch == 'y':
            play_game()
        else:
            print('THX FOR PLAYING')

play_game()
