# Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km em viagens de até 200 km, e R$ 0,45 para viagens mais longas.

print('\nCÁLCULO DO VALOR DA PASSAGEM DE ACORDO COM A DISTÂNCIA.')

distancia = int(input('\nInforme a distância para o seu destino:   '))
valor_kilometro = 0

if distancia <= 200:
    valor_kilometro = 0.5
else:
    valor_kilometro = 0.45

valor_total = distancia * valor_kilometro

print(f'\nO valor da sua passagem é de R$ {valor_total:.2f} Reais\n')