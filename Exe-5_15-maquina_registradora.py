''' Exercício 5.15 - Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:
Código -    Preço
1           0,50
2           1,00
3           4,00
5           7,00
9           8,00
O programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código invalido".'''

print('\nMÁQUINA REGISTRADORA\n')

total_compra = 0 # Variável para armazenar o total da compra

while True:
    codigo = int(input('Digite o código do produto (0 para sair): ')) # Solicita o código do produto
    
    if codigo == 0: # Se o código for 0, sai do loop
        break
           
    # Verifica o código e atribui o preço
    elif codigo == 1: 
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print('Código inválido.') # Código inválido
        continue

    quantidade = int(input('Digite a quantidade comprada: ')) # Solicita a quantidade comprada
    
    total_compra += preco * quantidade # Atualiza o total da compra

print(f'\nTotal da compra: R$ {total_compra:,.2f}') # Exibe o total da compra

print('\nFIM DO PROGRAMA\n')