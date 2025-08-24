# - Exercício 3.10 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

print('\nCÁLCULO DE AUMENTO DE SALÁRIO')

salario_atual = float(input('Digite o valor do salário: '))
percentual = float(input('Digite o percentual de aumento: '))
aumento = salario_atual*percentual/100
novo_salario = salario_atual+aumento

print(f'\nValor do aumento foi de {aumento:.2f} e o novo salário é de {novo_salario:.2f}\n')