from math import hypot
ctp = float(input('Digite a metragem do Cateto Oposto:'))
cdj = float(input('Digite a metragem do Cateto Adjacente:'))
hi = hypot(ctp, cdj)
print(f'Hipotenusa igual à:{hi:.2f}')
