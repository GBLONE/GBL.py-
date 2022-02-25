import math
num = float(input('Digite o ângulo:'))
grau = math.radians(num)
seno = math.sin(grau)
cos = math.cos(grau)
tag = math.tan(grau)
print(f'O seu seno é {seno:.2f} ,\n o seu cosseno é {cos:.2f} \n e o tangente {tag:.2f}')
