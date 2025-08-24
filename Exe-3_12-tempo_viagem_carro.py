# Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

print('\nCALCULO DE TEMPO DE VIAGEM')

# Não será levado em consideração os cálculos de minutos e segundos.

distancia = int(input('\nInforme a distância a ser percorrida em km:   '))
velocidade = int(input('Informe a velocidade média pretendida:   '))
tempo = distancia/velocidade

print(f'\nO tempo de viagem será de aproximandamente {tempo:.2f} horas.\n')