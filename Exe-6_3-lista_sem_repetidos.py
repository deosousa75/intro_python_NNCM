# Exercício 6.3 - Faça um programa que percorra duas listas e gere um terceira sem elementos repetidos.

print('\nGERA LISTA SEM ELEMENTOS REPETIDOS\n')

lista_1 = []
lista_2 = []
lista_3 = []

while True:
    numero = int(input('Digite um número para a lista 1 (ou -1 para sair): '))
    if numero == -1: # Condição de parada
        break
    lista_1.append(numero) # Adiciona o número à lista 1

while True:
    numero = int(input('Digite um número para a lista 2 (ou -1 para sair): '))
    if numero == -1: # Condição de parada
        break
    lista_2.append(numero) # Adiciona o número à lista 2

for elemento in lista_1: # Percorre a lista 1
    if elemento not in lista_3: # Verifica se o elemento não está na lista 3
        lista_3.append(elemento) # Adiciona o elemento à lista 3

for elemento in lista_2: # Percorre a lista 2
    if elemento not in lista_3: # Verifica se o elemento não está na lista 3
        lista_3.append(elemento) # Adiciona o elemento à lista 3    

print(f'\nLista 1: {lista_1}') # Exibe a lista 1
print(f'Lista 2: {lista_2}') # Exibe a lista 2
print(f'Lista 3 (união das listas 1 e 2 sem elementos repetidos): {lista_3}\n') # Exibe a lista 3       

print('\nFim do programa.\n')