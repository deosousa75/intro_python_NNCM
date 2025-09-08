# Exercício 6.6 -Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2. O mesmopara a chegada de clientes: F para fila 1 e G para fila 2.

print('\nSIMULAÇÃO DE DUAS FILAS DE BANCO\n')

ultimo_cliente = 10 # Número do último cliente que entrou na fila
ultimo_cliente_fila2 = 10 # Número do último cliente que entrou na fila 2
fila = list(range(1, ultimo_cliente + 1)) # Clientes na fila inicialmente
fila2 = list(range(1, ultimo_cliente_fila2 + 1)) # Clientes na fila 2 inicialmente  

while True: # Loop principal do programa
    print(f'\nExistem {len(fila)} clientes na fila 1.') # Mostra o número de clientes na fila
    print(f'Fila atual: {fila}') # Mostra a fila atual
    print(f'\nExistem {len(fila2)} clientes na fila 2.') # Mostra o número de clientes na fila
    print(f'Fila atual: {fila2}') # Mostra a fila atual
    operacao = input('\nDigite a operação (F - Adicionar Fila 1, G - Adicionar Fila 2, A - Atender fila 1, B - Atender fila 2, S - sair): ').upper() # Solicita a operação do usuário
    if operacao == 'A' or operacao == 'B':  # Atender o próximo cliente
        if operacao == 'A': # Atender fila 1
            if len(fila) > 0: # Verifica se há clientes na fila
                atendido = fila.pop(0) # Remove o primeiro cliente da fila
                print(f'O cliente {atendido} foi atendido.') # Informa qual cliente foi atendido
            else:
                print('\nNão há clientes na fila.') # Informa que a fila está vazia
        elif operacao == 'B': # Atender fila 2
            if len(fila2) > 0: # Verifica se há clientes na fila 2
                atendido = fila2.pop(0) # Remove o primeiro cliente da fila 2
                print(f'O cliente {atendido} foi atendido na fila 2.') # Informa qual cliente foi atendido
            else:
                print('\nNão há clientes na fila 2.') # Informa que a fila 2 está vazia
    elif operacao == 'F' or operacao == 'G': # Adicionar um novo cliente
        if operacao == 'F': # Adicionar na fila 1
            ultimo_cliente += 1 # Incrementa o número do último cliente
            fila.append(ultimo_cliente) # Adiciona o novo cliente ao final da fila
            print(f'O cliente {ultimo_cliente} entrou na fila.') # Informa qual cliente entrou na fila
        elif operacao == 'G': # Adicionar na fila 2
            ultimo_cliente_fila2 += 1 # Incrementa o número do último cliente da fila 2
            fila2.append(ultimo_cliente_fila2) # Adiciona o novo cliente ao final da fila 2
            print(f'O cliente {ultimo_cliente_fila2} entrou na fila 2.') # Informa qual cliente entrou na fila 2
    elif operacao == 'S': # Sair do programa
        print('\nEncerrando o programa.') # Informa que o programa está sendo encerrado
        break # Sai do loop principal
    else: # Operação inválida
        print('Operação inválida. Digite F, A ou S.') # Informa que a operação é inválida

print('\nPrograma encerrado.')