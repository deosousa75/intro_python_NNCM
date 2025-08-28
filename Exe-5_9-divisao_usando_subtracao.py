# Exercício 5.9 - Escreva um programa que leia dois números. Imprima a divisão do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado.

print('\nDIVISÃO USANDO SUBTRAÇÃO\n')

numero_1 = int(input('\nDigite o primeiro número (dividendo): '))
numero_2 = int(input('\nDigite o segundo número (divisor): '))

resultado = 0
resto = numero_1

while resto >= numero_2:
    resto -= numero_2
    resultado += 1  

print(f'\n{numero_1} dividido por {numero_2} é igual a {resultado}, com resto {resto}.\n')

print('\nFIM DO PROGRAMA\n')