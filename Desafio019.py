import random
n1 = str(input('Primeiro (a) aluno (a):'))
n2 = str(input('Segundo (a) aluno (a):'))
n3 = str(input('Terceiro (a) aluno (a):'))
n4 = str(input('Quarto (a) aluno (a):'))
x = [n1, n2, n3, n4]
print(f'O escolhido(a) foi: {random.choice(x)}')
