lista = []
lista1 = []
k = len(lista)
f = len(lista1)
for n in range(1,21):
    if k <= 10:
        d = int(input('Digite um valor:'))
        lista.append(d)
    elif f <= 10:
        d = int(input('Digite um valor:'))
        lista1.append(d)
print(lista, lista1)