# Fazer a média aritmética de 50 alunos utilizando o for
contador = 0
acumulador = 0
mediaAnualTurma = 0

for contador in range(5):
    mediaAnualAluno = float(input('Insira a nota do aluno: '))
    acumulador += mediaAnualAluno

mediaAnualTurma = acumulador/5
print('A media anual da turma é: ', mediaAnualTurma)