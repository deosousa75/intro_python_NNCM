# Exercício 3.15 - Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

print('\nCÁLCULO DE QUANTOS DIAS DE VIDA UM FUMANTE PERDEU')

anos_fumou = int(input('\nInforme a quantos anos você fuma:    '))
cigarros_dia = int(input('\nInforme a quantidade de cigarros que você fuma diariamente:     '))

perda = 10 # minutos por dia

perda_total = (cigarros_dia * (anos_fumou * 365) * perda) # quantidade de minutos
dias_perdidos = perda_total / 60 / 24

print(f'\nVocê perdeu aproximadamente {dias_perdidos:.2f} dias de sua vida.\n')