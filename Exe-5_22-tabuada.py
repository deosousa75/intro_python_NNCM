# Exercício 5.22 - Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuda da operação escolhida. Repita ateé que opção de saída seja escolhida.

print('\TABUDA DE OPERAÇÕES\n')

# Loop principal do programa
while True:
    print('Escolha a operação desejada:')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')

    escolha = input('Digite o número da operação (1-5): ')

# Sai do programa se a escolha for '5'
    if escolha == '5':
        print('Saindo do programa. Até mais!')
        break

# Verifica se a escolha é válida    
    if escolha not in ['1', '2', '3', '4']:
        print('Opção inválida. Tente novamente.\n')
        continue

# Determina a operação com base na escolha do usuário
    if escolha == '1':
        operacao = 'Adição'
        simbolo = '+'
    elif escolha == '2':
        operacao = 'Subtração'
        simbolo = '-'
    elif escolha == '3':
        operacao = 'Multiplicação'
        simbolo = '*'
    elif escolha == '4':
        operacao = 'Divisão'
        simbolo = '/' 
    
    numero = int(input(f'\nDigite o número para ver a tabuada de {operacao}: '))
    contador = 1
    print(f'\nTabuada de {operacao}:\n')
    while contador <= 10:
        if escolha == '1':
            resultado = numero + contador
        elif escolha == '2':
            resultado = numero - contador
        elif escolha == '3':
            resultado = numero * contador
        elif escolha == '4':
            resultado = numero / contador
      
        print(f'{numero} {simbolo} {contador} = {resultado}')
        contador += 1
    
print('\nFim do programa.')
    