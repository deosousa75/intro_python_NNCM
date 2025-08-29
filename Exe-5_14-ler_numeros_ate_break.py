# Exercício 5.14 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

print('\nLEITURA DE NÚMEROS INTEIROS (0 PARA PARAR)\n')

soma = 0 # Acumulador da soma dos números
contador = 0 # Contador de quantidade de números lidos

while True:
    numero = int(input('Digite um número inteiro (0 para parar): ')) # Lê o número inteiro
    if numero == 0: # Verifica se é o número de parada
        break # Sai do loop se for 0
    soma += numero # Adiciona o número à soma
    contador += 1 # Incrementa o contador

    
if contador > 0:
    print(f'\nQuantidade de números digitados: {contador}') # Exibe a quantidade de números lidos
    print(f'Soma dos números digitados: {soma}') # Exibe a soma dos números lidos
    print(f'Média aritmética: {soma / contador:.2f}') # Exibe a média aritmética
else:
    print('\nNenhum número foi digitado.') # Caso nenhum número tenha sido digitado

print('\nFIM DO PROGRAMA\n') # Indica o fim do programa