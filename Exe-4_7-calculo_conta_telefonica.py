# Exercício 4.7 - Reescrever o programa que calcula a conta da operadora tchau de acordo com os planos "falepouco" (franquia 100 minutos por R$ 50,00 e R$ 0,20 por minuto excedente) e "falemuito" (franquia 500 minutos por R$ 99,00 e R$ 0,15 por minuto excedente). Solicitar informar o plano e consumo em minutos e informar a conta no final.

print('\nCÁLCULO DO VALOR DA CONTA DE TELEFONE')

plano = str(input('\nInforme qual o seu plano de celular (falepouco ou falemuito):   '))

if plano == 'falepouco':
    franquia = 100
    valor_plano = 50
    valor_por_excedente = 0.2
elif plano == 'falemuito':
    franquia = 500
    valor_plano = 99
    valor_por_excedente = 0.15
else:
    print('\nO plano informado não existe.')

if plano == 'falepouco' or plano == 'falemuito':
    minutos_consumidos = int(input('\nInforma a quantidade de minutos consumidos:   '))
    valor_excedente = 0
    if minutos_consumidos > franquia:
        minutos_excedentes = minutos_consumidos - franquia
        valor_excedente = minutos_excedentes * valor_por_excedente
    total = valor_plano + valor_excedente

    print(f'\nValor do seu plano de assinatura: R$ {valor_plano:.2f}')
    print(f'Valor consumido além de sua franquia: R$  {valor_excedente:.2f}')
    print(f'Valor total da sua fatura:  R$  {total:.2f}')
    print('\nA sua Operadora de Telefonia TCHAU agradece a preferência.\n')
