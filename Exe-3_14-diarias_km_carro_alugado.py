# Exercício 3.14 - Escreva um programa que pergunte a quantidade e km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

print('\nCÁLCULO DE VALOR DE DIÁRIAS E KILOMETRAGEM PERCORRIDA')

kilometragem_percorrida = int(input('\nInforme a quantidade de kilômetros percorridos:     '))
dias_aluguel = int(input('\nInforme a quantidade de diárias:     '))

diaria = 60.00
valor_quilometro = 0.15

valor_total_diarias = dias_aluguel * diaria
valor_total_quilometragem = kilometragem_percorrida * valor_quilometro

valor_total = valor_total_diarias + valor_total_quilometragem

print(f'\nO valor total a pagar é de R$ {valor_total:.2f}, sendo R$ {valor_total_diarias:.2f} referentes a {dias_aluguel} diárias e R$ {valor_total_quilometragem:.2f} referentes à {kilometragem_percorrida} Km percorridos.')