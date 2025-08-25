# Exercício 3.13 - Escreva um programa que converta uma temperatura digitada em C para F. A fórmula para essa conversão é F = (9 x C)/5 + 32

print("CONVERSÃO DE GRAUS CELSIUS PARA FARENHEIT")

celsius = float(input('\nDigite o valor em Celsius a ser convertido:     '))
farenheit = (9 * celsius)/5 + 32

print(f'\nO valor de {celsius:.2f} graus Celsius equivale à {farenheit:.2f} graus Farenheit.\n')