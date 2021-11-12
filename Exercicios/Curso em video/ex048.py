s = 0
a = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        a = a + 1
        s = s + c
print('a soma dos {} valores é: {}'.format(a, s))
