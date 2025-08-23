# Exercício 3.8 - Escreva um programa que leia um valor em metros e 
# o exiba covertido em milimetros.

entrada_m = float(input("Conversão de valores - metros para milimetros." \
"\nDigite um valor em metros para conversão: "))
saida_mm = float(entrada_m*1000)
print(f'O número {entrada_m} metros, convertido para milimetros é {saida_mm}')