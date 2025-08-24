# Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

print('\nCÁLCULO DE DESCONTO EM MERCADORIA')

valor_produto = float(input('\nDigite o valor do produto: '))
percentual_desconto = float(input('Digite o percentual de desconto: '))
valor_desconto = valor_produto*percentual_desconto/100
novo_valor_produto = valor_produto - valor_desconto

print(f'\nO valor do desconto é de {valor_desconto:.2f} e o novo valor o produto é de {novo_valor_produto:.2f}')