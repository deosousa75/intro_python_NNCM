# Exercício 5.23 - Escreva um programa que leia um número e verifique se é ou não um número primro. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números primos impares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que o 2 é o único número primo que é par.

print('\nVERIFICADOR DE NÚMEROS PRIMOS\n')

while True:
    inteiro = int(input('\nDigite um número inteiro positivo (0 ou 1 para sair): '))
    if inteiro <= 1: # 0 e 1 não são primos
        print('\nEncerrando o programa...')
        break
    elif inteiro == 2: # 2 é o único número primo que é par
        print(f'\n{inteiro} é um número primo!\n')
        continue
    elif inteiro % 2 == 0: # outros números pares não são primos
        print(f'\n{inteiro} não é um número primo!\n')
        continue
    else:
        primo = True # variável de controle
        for i in range(3, inteiro, 2): # verifica apenas os números ímpares
            if inteiro % i == 0: # se o resto da divisão for 0, não é primo
                primo = False # atualiza a variável de controle
                break
        if primo:    
            print(f'\n{inteiro} é um número primo!\n')
        else:
            print(f'\n{inteiro} não é um número primo!\n')

print('\nFim do programa!')