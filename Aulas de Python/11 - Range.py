'''
Decidi fazer uma aula separada da estrutura de repetição Range() pois é algo novo em relação as outras linguagens 
e eu quero fixar isso de forma confortável
'''

x = range(0,1000,100) # Basicamente é um gerador para criar listas gigantes, por exemplo, 1000 elementos
lista = list(x)     # Gerador é um tipo de objeto de Python que gera um iterador a partir do instante que a gente gera seus valores
print(lista)

# Principal uso de range no meu histórico até agora
for i in range(0,10):
    print('E ae moçada')

# Comentário importante, a linha de código range(0,10) inclui o 0 e exclui o 10, indo até 9, mas com 10 iterações.