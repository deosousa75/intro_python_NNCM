# Exercício 5.4 - Escreva um programa que imprima os números ímpares do número 1 até o número digitado pelo usuário.

print('\nNUMEROS ÍMPARES\n')

fim = int(input('\nDigite um número inteiro positivo: '))

contador = 1

while contador <= fim:
    if contador % 2 != 0:
        print(contador)
    contador += 1

print('\nFIM DO PROGRAMA\n')