# Escreva um algoritmo que leia 3 valores inteiros e diferentes e mostre-os em ordem decrescente. Utilize para tal seleção encadeada.
# Quando, devido á necessidade de processamento, agruparmos várias seleções, formaremos uma seleção encadeada.Normalmente, tal formação ocorre
# quando uma determinada ação ou bloco deve ser executado se um grande conjunto de possibilidades ou combinações for satisfeito.

A = int(input())
B = int(input())
C = int(input())

if A<B and A<C : # A menor, partindo disso precisamos saber se B é menor que C
    if B<C:
        print(A, B, C)
    else:
        print(A, C, B)
elif B<C: # Sabendo que A não é menor, precisamos saber se B é menor e se A é menor ou menor que C
    if A<C:
        print(B, A, C)
    else:
        print(B, C, A)
else: # Sabendo que A e B não são menores, e C é, precisamos saber qual é menor, A ou B
    if B<A:
        print(C, B, A)
    else:
        print(C, A, B)


        