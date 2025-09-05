# Exercício 6.2 - Faça um programa que leia duas listas e gere uma terceira com os elementos das duas primeiras.

print('\nPrograma que lê duas listas e gera uma terceira com os elementos das duas primeiras.\n')

lista_1 = [] # Primeira lista
lista_2 = [] # Segunda lista
lista_3 = [] # Terceira lista (união das duas primeiras)

while True:
    numero = int(input('Digite um número para a lista 1 (ou -1 para sair): '))
    if numero == -1: # Condição de parada
        break
    lista_1.append(numero) # Adiciona o número à lista 1
lista_3.extend(lista_1) # Adiciona os elementos da lista 1 à lista 3

while True:
    numero = int(input('Digite um número para a lista 2 (ou -1 para sair): '))
    if numero == -1: # Condição de parada
        break
    lista_2.append(numero) # Adiciona o número à lista 2
lista_3.extend(lista_2) # Adiciona os elementos da lista 2 à lista 3

print(f'\nLista 1: {lista_1}') # Exibe a lista 1
print(f'Lista 2: {lista_2}') # Exibe a lista 2
print(f'Lista 3 (união das listas 1 e 2): {lista_3}\n') # Exibe a lista 3

print('\nFim do programa.\n')