# Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

print('\nCALCULO DE JUROS DE POUPANÇA\n')

deposito_inicial = float(input('Informe o valor do depósito inicial: R$ '))
taxa_juros = float(input('Informe a taxa de juros (em %): '))

total_juros = 0
meses = 1

while meses <= 24:
    juros_mes = deposito_inicial * (taxa_juros / 100)
    total_juros += juros_mes
    deposito_inicial += juros_mes
    print(f'Mês {meses:2d}, Saldo: R$ {deposito_inicial:,.2f} (Juros: R$ {juros_mes:,.2f})')
    meses += 1

print(f'\nTotal ganho com juros em 24 meses: R$ {total_juros:,.2f}\n')