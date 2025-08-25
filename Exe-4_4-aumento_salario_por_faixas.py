# Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, e 15%.

print('\nAUMENTO DE SALÁRIO PROPORCIONAL')

salario = float(input('\nInforma o valor do seu salário:   '))
aumento = 0

if salario > 1250:
    aumento = salario * 0.1
elif salario <= 1250:
    aumento = salario * 0.15
print(f'\nO aumento do seu salário será de R$ {aumento:.2f} Reais')
    