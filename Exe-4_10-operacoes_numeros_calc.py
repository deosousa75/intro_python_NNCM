# Exercício 4.10 - Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma, subtração, multiplicação e divisão. Exiba o resultado da operação solicitada.

print('\nCALCULADORA DE DOIS NÚMEROS SOMA, SUBTRAÇÃO, DIVISÃO E MULTIPLICAÇÃO')

valido = True


operacao = int(input('\nInforme a operação desejada:' \
        '\n1 - SOMA' \
        '\n2 - SUBTRAÇÃO' \
        '\n3 - DIVISÃO' \
        '\n4 - MULTIPLICAÇÃO:\n'))

if operacao > 4 or operacao < 1:
    print('Operação inválida. ')

else:
    numero_a = int(input('\nInforme o primeiro número:  '))
    numero_b = int(input('\nInforme o segundo número:  '))
    
    if operacao == 1:
        print(f'\nO numero {numero_a} somado ao numero {numero_b} é {numero_a + numero_b}')
    elif operacao == 2:
        print(f'\nO número {numero_a} menos o número {numero_b} é {numero_a - numero_b}')
    elif operacao == 3:
        print(f'\nO número {numero_a} dividido por {numero_b} é {numero_a / numero_b}')
    elif operacao == 4:
        print(f'\nO número {numero_a} multiplicado por {numero_b} é {numero_a * numero_b}')