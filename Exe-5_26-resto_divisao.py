# Exercício 5.26 - Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.

print('\nCÁLCULO DO RESTO DA DIVISÃO INTEIRA ENTRE DOIS NÚMEROS]\n')

numero = int(input('Digite o número que deseja dividir: '))
divisor = int(input('Digite o número pelo qual deseja dividir: '))
resto = numero

while resto >= divisor:
    resto -= divisor

print(f'\nO resto da divisão entre {numero} e {divisor} é {resto}.')