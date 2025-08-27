# Exercício 4.12 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C par comércios. Calcule o preço a pagar de acordo com os seguintes dados: Residencial (Até 500 - R$ 0,40; Mais de 500 - R$ 0,65), Comercial (Até 1000 - R$ 0,55; Acima de 1000 - R$ 0,60) e Industrial (Até 5000 - R$ 0,55; Acima de 5000 - R$ 0,60)

print('\nCALCULADORA DE CONSUMO DE ENERGIA ELÉTRICA\n')

consumo_energia = float(input('Informe o consumo em kWh: '))
tipo_instalacao = str(input('Informe o tipo de instalação (R - Residencial, C - Comercial, I - Industrial): '))    

if tipo_instalacao == 'R' or tipo_instalacao == 'r':
    if consumo_energia <= 500:
        print(f'Valor a Pagar: R$ {consumo_energia * 0.40:.2f}')
    else:
        print(f'Valor a Pagar: R$ {consumo_energia * 0.65:.2f}')
elif tipo_instalacao == 'C' or tipo_instalacao == 'c':
    if consumo_energia <= 1000:
        print(f'Valor a Pagar: R$ {consumo_energia * 0.55:.2f}')
    else:
        print(f'Valor a Pagar: R$ {consumo_energia * 0.60:.2f}')
elif tipo_instalacao == 'I' or tipo_instalacao == 'i':
    if consumo_energia <= 5000:
        print(f'Valor a Pagar: R$ {consumo_energia * 0.55:.2f}')
    else:
        print(f'Valor a Pagar: R$ {consumo_energia * 0.60:.2f}')
else:
    print('Tipo de instalação inválido. Por favor, informe R, C ou I.')
