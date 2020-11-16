# Construa um algoritmo que seja capaz de concluir qual dentre os seguintes animais foi escolhido, atráves de perguntas e respostas.
# Animais possíveis: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.

primeiraEscolha = int(input('Mamifero, ave ou reptil?'))
animalEscolhido = '0'

if primeiraEscolha == 1:
    locomocao1 = int(input('Quadrupe, bípede, voador ou aquatico? '))
    if locomocao1 == 1:
        alimentacao1 = int(input('Carnivoro ou hervivoro? '))
        if alimentacao1 == 1:
            animalEscolhido = 'Leão'
        else:
            animalEscolhido = 'Cavalo'
    if locomocao1 == 2:
       alimentacao2 = int(input('Onívoro ou frutívoro?'))
       if alimentacao2 == 1:
           animalEscolhido = 'Homem'
       else:
            animalEscolhido = 'Macaco'
    if locomocao1 == 3:
        animalEscolhido = 'Morcego'
    else:
        animalEscolhido = 'Baleia'
elif primeiraEscolha == 2:
    tipoVoo = int(input('Não voadoras, nadadora ou de rapina? '))
    if tipoVoo == 1:
        clima = int(input('Tropical ou polar? '))
        if clima == 1:
            animalEscolhido = 'Avestruz'
        else:
            animalEscolhido = 'Pinguim'
    elif tipoVoo == 2:
        animalEscolhido = 'Pato'
    else:
        animalEscolhido = 'Aguia'
else:
    caracteristica = int(input('Com casco, carnívoro ou sem patas? '))
    if caracteristica == 1:
        animalEscolhido = 'Tartaruga'
    elif caracteristica == 2:
        animalEscolhido = 'Crocodilo'
    elif caracteristica == 3:
        animalEscolhido = 'Cobra'
    
print(animalEscolhido)