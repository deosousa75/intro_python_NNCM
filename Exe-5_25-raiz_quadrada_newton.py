# Exercício 5.25 - Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado arpoximado. Sendo n o número a obter a raiz quadrada, considere a base b=2. Calcule p usano a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

print('\nCÁLCULO DE RAIZ QUADRADA PELO MÉTODO DE NEWTON\n')

numero = float(input('Digite um número para calcular a raiz quadrada: '))
base = 2
p = (base + (numero / base)) / 2
quadrado_p = p ** 2 
diferenca = abs(numero - quadrado_p)
print(f'Diferença inicial: {diferenca:.4f}')

while diferenca >= 0.0001:
    base = p
    p = (base + (numero / base)) / 2
    quadrado_p = p ** 2
    diferenca = abs(numero - quadrado_p)
    print(f'Calculando diferença: {diferenca:.4f}')

print(f'\nA raiz quadrada de {numero} é aproximadamente {p:.4f}\n')
