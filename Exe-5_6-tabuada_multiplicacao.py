# Exercício 5.6 - Escreva um programa que faça a tabuada de multiplação (1 a 10) do número informado pelo usuário.

print("\nTABUADA DE MULTIPLICAÇÃO\n")

numero = int(input("\nDigite um número para ver a tabuada de multiplicação: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1

print("\nFIM\n")