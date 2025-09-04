# Exercício 5.21 - Reescreva o programa de contagem de cédulas de forma a continuar executando até que o valor digitado seja 0. Utilize repetições aninhadas.

print ('\nCONTAGEM DE CÉDULAS\n')

valor = int(input('Digite o valor a ser sacado (0 para sair): R$ '))

while valor != 0:
    if valor < 0:
        print('Valor inválido. Tente novamente.')
    else:
        a_pagar = valor
        cedula = 100
        total_cedulas = 0

        while True:
            if a_pagar >= cedula:
                a_pagar -= cedula
                total_cedulas += 1
            else:
                if total_cedulas > 0:
                    print(f'Total de {total_cedulas} cédulas de R$ {cedula}')
                if cedula == 100:
                    cedula = 50
                elif cedula == 50:
                    cedula = 20
                elif cedula == 20:
                    cedula = 10
                elif cedula == 10:
                    cedula = 5
                elif cedula == 5:
                    cedula = 2
                elif cedula == 2:
                    cedula = 1
                total_cedulas = 0
                if a_pagar == 0:
                    break

    valor = int(input('\nDigite o valor a ser sacado (0 para sair): R$ '))

print('\nObrigado por usar nosso sistema de contagem de cédulas. Até logo!')