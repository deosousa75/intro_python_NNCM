# Exercício 5.7 - Modifique o programa anterior de modo que o usuário digite também o início e o fim da tabuada.

print("\nTABUADA DE MULTIPLICAÇÃO\n")

numero = int(input("\nDigite um número para ver a tabuada de multiplicação: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
contador = inicio

while contador <= fim:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1

print("\nFIM\n")