# Exercício 4.15 - Reescrever um programa de comparação com horário.

print('\nCOMPRIMENTO DE ACORDO COM O HORÁRIO\n')

hora = int(input('Digite a hora atual (0-23): ')) 

if 0 <= hora < 12:
    print('\nBom dia!')
elif 12 <= hora < 18:
    print('\nBoa tarde!')
elif 18 <= hora < 24:
    print('\nBoa noite!')
else:
    print('\nHora inválida! Por favor, digite um valor entre 0 e 23.')