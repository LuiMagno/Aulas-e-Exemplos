# Para construir uma matriz em python (de uma forma que eu considero 'amadora', você precisa fazer um vetor de vetores)

matriz = [[0 , 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: ')) # o f antes da string vem com o intuito de tornar a interpolação
                                                                       # de strings com variáveis mais fácil  

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='') # aqui vemos o uso de duas novas formas, o end e o ^5, para estudarmos no futuro
    print()

