# Exercício 6.5 - Altere o programa de fila de forma a poder trabalhar com vários comandos digitados de uma só vez. Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma string. Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa.

print('\nSIMULAÇÃO DE FILA DE BANCO\n')

ultimo_cliente = 10 # Número do último cliente que entrou na fila
fila = list(range(1, ultimo_cliente + 1)) # Clientes na fila inicialmente

while True: # Loop principal do programa
    print(f'\nExistem {len(fila)} clientes na fila.') # Mostra o número de clientes na fila
    print(f'Fila atual: {fila}') # Mostra a fila atual
    operacao = input('\nDigite a operação (F - Adicionar, A - atender, S - sair): ').upper() # Solicita a operação do usuário
    if operacao == 'A':  # Atender o próximo cliente
        if len(fila) > 0: # Verifica se há clientes na fila
            atendido = fila.pop(0) # Remove o primeiro cliente da fila
            print(f'O cliente {atendido} foi atendido.') # Informa qual cliente foi atendido
        else:
            print('Não há clientes na fila.') # Informa que a fila está vazia
    elif operacao == 'F': # Adicionar um novo cliente
        ultimo_cliente += 1 # Incrementa o número do último cliente
        fila.append(ultimo_cliente) # Adiciona o novo cliente ao final da fila
        print(f'O cliente {ultimo_cliente} entrou na fila.') # Informa qual cliente entrou na fila
    elif operacao == 'S': # Sair do programa
        print('Encerrando o programa.') # Informa que o programa está sendo encerrado
        break # Sai do loop principal
    else: # Operação inválida
        print('Operação inválida. Digite F, A ou S.') # Informa que a operação é inválida

print('Programa encerrado.')