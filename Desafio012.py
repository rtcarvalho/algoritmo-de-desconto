print('Desafio012: Faça um algoritimo que leia o preço de um produto e mostre um novo preço com 5% de desconto:')

produto1 = float(input('Valor produto: '))

desconto = float(produto1 * 0.05)
valor = produto1-desconto

print('O produto custa R${} tem um desconto de 5%, você vai pagar apenas R${:.2f} ' .format(produto1, valor))
