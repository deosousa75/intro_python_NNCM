# Exercício 4.14 - Reescrever um programa de comparação de números.

print('\nCOMPARAÇÃO DE NÚMEROS\n')

numero = int(input('Digite um número inteiro: '))

if numero < 10:
    print(f'\nO número {numero} é menor que 10.')
elif numero >= 10 and numero < 20:
    print(f'\nO número {numero} é maior, ou igual a 10, e menor 20.')
else:
    print(f'\nO número {numero} é maior ou igual a 20.')