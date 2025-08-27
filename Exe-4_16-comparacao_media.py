# Exercício 4.16 - Reescrever um programa de comparação com média.

print('\nCOMPARA NOTA COM A MÉDIA\n')

media = float(input('Digite a sua média: '))

if media < 4:
    print('\nInfelizmente você foi reprovado(a).')
elif 4 <= media < 7:
    print('\nVocê está de recuperação.')
else:
    print('\nParabéns, você foi aprovado(a)!')