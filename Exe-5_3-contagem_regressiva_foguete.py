# Exercício 5.3 - Escreva um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 0, e Fogo! na tela.

print('\nCONTAGEM REGRESSIVA PARA O LANÇAMENTO DO FOGUETE\n')

contador = 10

while contador >= 0:
    print(contador)
    contador -= 1

print('\nFOGO!\n')