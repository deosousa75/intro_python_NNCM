# Exercício 6.1 - Modifique o programa de notas para ler 7 notas ao invés de 5.

print('\nMÉDIA DE 7 NOTAS\n')

notas = [0]*7 # lista para armazenar as notas
soma = 0 # variável para soma das notas
x = 0 # contador
while x < 7: # enquanto contador for menor que 7
    notas[x] = float(input(f'Digite a {x + 1}ª nota: ')) # entrada das notas
    soma += notas[x] # soma das notas
    x += 1 # incremento do contador
x = 0 # zera o contador
while x < 7: # enquanto contador for menor que 7
    print(f'A {x + 1}ª nota é {notas[x]:.2f}') # exibe as notas
    x += 1 # incremento do contador
print(f'A média das notas é {soma / 7:.2f}\n') # exibe a média das notas

print('\nFIM DO PROGRAMA\n')  