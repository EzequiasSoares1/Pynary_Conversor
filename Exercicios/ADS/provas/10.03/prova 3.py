pilha = []
pilha2= []
for w in range(1, 21):
    d = int(input('Digite um valor:'))
    f = d % 2

    if f == 0:
        pilha.append(d)

    elif f == 1:
        pilha2.append(d)

pilha.pop()
pilha2.pop()

