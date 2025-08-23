# Exercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e 
# segundos de um usuário. Calcule o total em segundos.


print('\nA seguir serão solicitados os dados, insira-os corretamente.')
dias=int(input('Digite a quantidade de dias: '))
# para efeito de exercício foram considerados os valores acima do que convém para a célula.
# por exemplo: mais de 24 horas, mais de 60 minutos, mais de 60 segundos. Apenas para fins de
# conversão de valores para segundos.
horas=int(input('Digite a quantidade de horas: '))
minutos=int(input('Digite a quantidade de minutos: '))
segundos=int(input('Digite a quantidade de segundos: '))
total=(dias*24*60*60 + horas*60*60 + minutos*60 + segundos)

print(f'\nA soma de {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos é {total} segundos.\n')