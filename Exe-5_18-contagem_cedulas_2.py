# Exercício 5.18 - Modifique o programa para trabalhar com notas de 100

print('\nCONTAGEM DE CÉDULAS\n')

valor = int(input('Digite o valor a ser sacado (em R$): ')) # Solicita o valor a ser sacado

cedulas = 0 # Inicializa o contador de cédulas
atual = 100 # Inicializa a cédula atual como 100
a_pagar = valor # Inicializa o valor a pagar como o valor solicitado

while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R$ {atual},00')
        if a_pagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cedulas = 0
