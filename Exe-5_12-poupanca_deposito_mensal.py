# Exercício 5.12 - Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o calculo de juros do ês seguinte.

print('\nCALCULO DE POUPANÇA COM DEPÓSITO MENSAL\n')

deposito_inicial = float(input('Informe o valor do depósito inicial: R$ '))
taxa_juros = float(input('Informe a taxa de juros (em %): '))
deposito_mensal = float(input('Informe o valor do depósito mensal: R$ '))   

meses = 1
total_juros = 0

while meses <= 24:
    juros_mes = deposito_inicial * (taxa_juros / 100) # Cálculo dos juros do mês
    total_juros += juros_mes # Acumula os juros totais
    deposito_inicial += juros_mes # Adiciona os juros ao saldo
    deposito_inicial += deposito_mensal  # Depósito mensal no início do mês
    print(f'Mês {meses:2d}, Saldo: R$ {deposito_inicial:,.2f} (Juros: R$ {juros_mes:,.2f})')
    meses += 1 # Incrementa o contador de meses

print(f'\nSaldo Final: R$ {deposito_inicial:,.2f}') # Exibe o saldo final após 24 meses
print(f'Total ganho com juros em 24 meses: R$ {total_juros:,.2f}\n') # Exibe o total ganho com juros