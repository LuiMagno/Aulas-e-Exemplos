listaLampadas = [True, False, False, False, False, True, True, True, False, False]
lampadasBoas = 0
lampadasRuins = 0

for x in listaLampadas:
    if x:
        print('Não precisa trocar!')
        lampadasBoas += 1 #por incrível que pareça, python não suporta o variável++
    else:
        print('Trocando lâmpada quebrada!')
        lampadasRuins += 1
        x += 1

print('Lampadas boas = ', lampadasBoas)
print('Lampadas ruins = ', lampadasRuins)


#o objetivo da construção de um algoritmo é sequenciar ações para se chegar a uma solução, compondo assim uma estrutura sequencial. O 'for' é 
#utilizado com uma estrutura de repetição