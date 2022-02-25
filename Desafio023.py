print('Por favor, apenas números de 0 a 9999!')
n = int(input('Digite um número:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('='*20)
print(f'A Unidade é {u},\na Dezena é {d},\na Centena é {c} \ne o Milhar é {m}.')
print('='*20)
