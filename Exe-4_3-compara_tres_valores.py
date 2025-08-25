#- Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.

print('\nSOLICITA E COMPARA TRÊS VALORES')

numero_a = int(input('\nDigite o primeiro valor:  '))
numero_b = int(input('\nDigite o segundo valor:   '))
numero_c = int(input('\nDigite o terceiro valor:   '))

maior_numero = numero_a

if numero_b > maior_numero:
    maior_numero = numero_b
if numero_c > maior_numero:
    maior_numero = numero_c
print(f'\nO maior número digitado é {maior_numero}')