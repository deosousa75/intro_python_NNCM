# Exercício 5.27 - Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o mesmo caso seus digitos sejam invertidos. Exemplos: 454, 10501.

print('\nVERIFICAÇÃO DE NÚMERO PALÍNDROMO\n')

numero = int(input('Digite um número inteiro: '))
numero_invertido = 0 # variável para armazenar o número invertido
numero_copia = numero # variável para manipular o número original
while numero_copia > 0: # enquanto houver dígitos no número
    digito = numero_copia % 10 # obtém o último dígito
    print(f'Dígito extraído: {digito}') # exibe o dígito extraído
    numero_invertido = numero_invertido * 10 + digito # constrói o número invertido
    print(f'Número invertido até agora: {numero_invertido}') # exibe o número invertido até agora
    numero_copia //= 10 # remove o último dígito do número original
    print(f'Número restante para processar: {numero_copia}\n') # exibe o número restante para processar
if numero == numero_invertido: # compara o número original com o invertido
    print(f'\nO número {numero} é um palíndromo!\n') # se forem iguais, é palíndromo
else:
    print(f'\nO número {numero} não é um palíndromo!\n') # se forem diferentes, não é palíndromo