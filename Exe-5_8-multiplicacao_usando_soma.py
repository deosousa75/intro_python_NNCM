# Exercício 5.8 - Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilizando apenas os operadores de soma e subtração para calcular o resultado.

print('\n MULTIPLICAÇÃO USANDO SOMA \n')

numero_1 = int(input('\nDigite o primeiro número: '))
numero_2 = int(input('\nDigite o segundo número: '))

resultado = 0

while numero_2 > 0:
    resultado += numero_1
    numero_2 -= 1 
 
print(f'\nO resultado da multiplicação é: {resultado}\n')
print('FIM DO PROGRAMA')