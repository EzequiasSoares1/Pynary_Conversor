from random import choice
a = str(input('Primeiro aluno:'))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro aluno'))
d = str(input('Quarto aluno:'))
lista = [a, b, c, d]
g = choice(lista)
lista = [a, b, c, d]
print('o aluno escolhido foi {}'.format(g))
