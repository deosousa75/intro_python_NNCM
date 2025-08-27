# Exercício 4.11 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

print('\nCÁLCULO DE VALOR DE PRESTAÇÃO DE FINANCIAMENTO DE IMÓVEL')

valor_imovel = float(input('\nInforme o valor do imóvel a ser financiado:   '))
tempo_financiamento = int(input('\nInforme agora a prazo de financiamento (em anos):   '))
salario = float(input('\nInforme o valor do seu salário mensal:   '))

capacidade_endividamento = salario * 0.3
valor_prestacao = valor_imovel / (tempo_financiamento * 12)

if valor_prestacao > capacidade_endividamento:
    print('\nInfelizmente sua renda não é suficiente para o financiamento do imóvel pretendido.')
    print(f'''Valor do imóvel: R$ {valor_imovel:.2f} 
          Prestação Pretendida:  R$ {valor_prestacao:.2f} 
          Valor Máximo da Prestação:  R$ {capacidade_endividamento:.2f} em um sálario de R$ {salario:.2f}.''')
else:
    print('\nParabéns, seu financiamento foi autorizado.')
    print(f'''Valor do imóvel: R$ {valor_imovel:.2f} 
          Prestação:  R$ {valor_prestacao:.2f} em {tempo_financiamento * 12} parcelas. 
          Valor Máximo da Prestação:  R$ {capacidade_endividamento:.2f} em um sálario de R$ {salario:.2f}.''')