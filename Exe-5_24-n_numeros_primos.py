# Exercício 5.24 - Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

print('\nNÚMEROS PRIMOS\n')

while True:
    numero = int(input('Digite um número inteiro positivo (0 para sair): '))
    if numero < 0:
        print('Número inválido. Tente novamente.')
        continue
    elif numero == 0:
        print('Encerrando o programa.')
        break
    else:
        quant_primos = 0 # contador de números primos encontrados
        contador = 2 # número a ser verificado
        print(f'Os {numero} primeiros números primos são:')

        while quant_primos < numero: # enquanto não encontrar n primos
            primo = True
            for i in range(2, contador): # verifica se o número é primo
                if contador % i == 0:
                    primo = False
                    break
            if primo: # se for primo, imprime e incrementa o contador de primos
                print(f'{contador}')
                quant_primos += 1 # incrementa o contador de primos
            contador += 1 # incrementa o número a ser verificado
        print('\n') # nova linha após imprimir os primos

print('\nFim do programa!')
                