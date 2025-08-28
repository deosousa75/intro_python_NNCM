# Exercício 5.10 - Reescrever um programa que verifica correção de questões

print('\nCORREÇÃO DE QUESTÕES\n')

pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f'Qual a resposta da questão {questao}? ')
    if questao == 1 and resposta == 'b' or resposta == 'B':
        pontos += 1
    if questao == 2 and resposta == 'a'or resposta == 'A':
        pontos += 1
    if questao == 3 and resposta == 'd' or resposta == 'D':
        pontos += 1
    questao += 1

print(f'\nO aluno fez {pontos} ponto(s).')

print('\nFIM DO PROGRAMA\n')