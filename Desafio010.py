# print('Quantos reais ela tem em carteira e quantos ela pode comprar em dólares US$1,00=R$3,27')
print('Conversor de R$ para US$')
x = float(input('Digite seu dinheiro em R$:'))
dol = x / 5.19
eur = x / 5.89
chn = x * 1.22
print(f'Com esse valor de R$ {x}, você vai ter US$ {dol:.3} Dólares.')
print(f"Em Yuan Chinês {chn:.3}, e em Euros {eur:.2}.")
