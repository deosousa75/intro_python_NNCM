# Exercício 5.19 - Modifique o programa para aceitar valores decimais, ou seja, também aceitas moedas e 0,01; 0,02; 0,05; 0,10 e 0,50.

print('\nCONTAGEM DE CÉDULAS OU MOEDAS\n')

valor = float(input('Digite o valor a ser sacado (em R$): '))
valor_centavos = int(round(valor * 100))  # Trabalha em centavos

cedulas = 0
atual = 10000  # 100 reais em centavos
a_pagar = valor_centavos

while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'{cedulas} cédula/moeda(s) de R$ {atual/100:.2f}')
        if a_pagar == 0:
            break
        if atual == 10000:
            atual = 5000
        elif atual == 5000:
            atual = 2000
        elif atual == 2000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 200
        elif atual == 200:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cedulas = 0
