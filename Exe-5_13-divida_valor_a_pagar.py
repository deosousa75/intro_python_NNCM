# Exercício 5.13 - Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a divida seja paga, o total pago e o total de juros pago.

print('\nCÁLCULO DE PAGAMENTO DE DÍVIDA\n')

valor_divida = float(input('Informe o valor inicial da dívida: R$ '))
juros_mensal = float(input('Informe a taxa de juros mensal (em %): '))
valor_pago_mensal = float(input('Informe o valor que será pago mensalmente: R$ '))  

meses = 0
total_pago = 0
total_juros = 0

while valor_divida > 0:
    juros = valor_divida * (juros_mensal / 100) # Cálculo dos juros do mês
    valor_divida += juros # Adiciona os juros à dívida
    total_juros += juros # Acumula o total de juros pagos
    
    if valor_pago_mensal > valor_divida: # Se o valor pago mensal for maior que a dívida restante
        valor_pago_mensal = valor_divida # Ajusta o valor pago para quitar a dívida
    
    valor_divida -= valor_pago_mensal # Subtrai o valor pago da dívida
    total_pago += valor_pago_mensal # Acumula o total pago
    meses += 1 # Incrementa o número de meses

print(f'\nNúmero de meses para quitar a dívida: {meses}')
print(f'Total pago: R$ {total_pago:,.2f}')
print(f'Total de juros pago: R$ {total_juros:,.2f}')

print('\nPrograma encerrado.') # Fim do programa