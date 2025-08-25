# Exercício 4.1 - Escreva um programa que leia dois valores, a e b, e que exiba uma mensagem informado qual o valor maior.

print('\nCOMPARA DOIS VALORES, A E B')

numero_a = int(input('\nDigite o primeiro valor (a):    '))
numero_b = int(input('\nDigite o segundo valor (b):   '))

if numero_a > numero_b:
    print('\nO primeiro valor digital é maior do que o segundo.')
elif numero_b > numero_a:
    print('\nO segundo valor é maior do que o primeiro.')
else:
    print('\nOs números digitados são iguais.')