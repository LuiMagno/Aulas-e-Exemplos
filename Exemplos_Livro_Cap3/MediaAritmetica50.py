# Fazer a média aritmética de 50 alunos
contador = 0
acumulador = 0
mediaAnualTurma = 0
mediaAnualAluno = 0
while mediaAnualAluno != -1:
    mediaAnualAluno = float(input('Insira sua média: '))
    if mediaAnualAluno == -1:
        break
    acumulador += mediaAnualAluno
    contador += 1
    
mediaAnualTurma = acumulador/contador

print('Média Anual dos ',contador, 'alunos é:', mediaAnualTurma)