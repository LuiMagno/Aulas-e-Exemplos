# Elabora um algoritmo que, a partir de um dia, mês e ano fornecidos, valide se eles compoem uma data válida. Não deixe de considerar
# os meses com 30 ou 31 dias, e o tratamento de ano bissexto.
anoBissexto = False
mesValido = False
diaValido = False
anoEscolhido = int(input('Insira o ano: '))
mesEscolhido = int(input('Insira o mes: ')) 
diaEscolhido = int(input('Insira o dia: '))

if anoEscolhido%4 == 0 and anoEscolhido%100 != 0 or anoEscolhido%400 == 0:
    anoBissexto = True
    print('É bissexto!')  

if mesEscolhido>0 and mesEscolhido<13:
    mesValido = True

if mesEscolhido == 1:
    if diaEscolhido>0 and diaEscolhido<32:
        diaValido = True

if mesEscolhido == 2 and anoBissexto == True:
    if diaEscolhido>0 and diaEscolhido<30:
        diaValido = True
elif mesEscolhido == 2:
    if diaEscolhido>0 and diaEscolhido<29:
        diaValido = True

if mesEscolhido == 3:
    if diaEscolhido>0 and diaEscolhido<32:
        diaValido = True

if mesEscolhido == 4:
    if diaEscolhido>0 and diaEscolhido<31:
        diaValido = True

if mesEscolhido == 5:
    if diaEscolhido>0 and diaEscolhido<32:
        diaValido = True

if mesEscolhido == 6:
    if diaEscolhido>0 and diaEscolhido<31:
        diaValido = True

if mesEscolhido == 7:
    if diaEscolhido>0 and diaEscolhido<32:
        diaValido = True

if mesEscolhido == 8:
    if diaEscolhido>0 and diaEscolhido<32:
        diaValido = True

if mesEscolhido == 9:
    if diaEscolhido>0 and diaEscolhido<31:
        diaValido = True

if mesEscolhido == 10:
    if diaEscolhido>0 and diaEscolhido<32:
        diaValido = True

if mesEscolhido == 11:
    if diaEscolhido>0 and diaEscolhido<31:
        diaValido = True

if mesEscolhido == 12:
    if diaEscolhido>0 and diaEscolhido<32:
        diaValido = True

if mesValido == True and diaValido == True:
    print('Data válida!')
else:
    print('Data inválida!')