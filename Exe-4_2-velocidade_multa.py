# Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de  80 km/h.

print('\nCÁLCULO DE MULTA EM CASO DE EXCESSO DE VELOCIDADE')

velocidade = int(input('\nInforme a velocidade do veículo:   '))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'\nVocê excedeu o limite de velocidade e pagará uma multa de R$ {multa:.2f} reais\n')
else:
    print('\nVocê está dentro do limite de velocidade permitido.\n')
