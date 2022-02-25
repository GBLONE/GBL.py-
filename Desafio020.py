import random
print('Sequência de apresentação dos trabalhos! ')
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quarto aluno:')
Lis = [n1, n2, n3, n4]
random.shuffle(Lis)
print('A ordem de apresentação é:')
print(Lis)
