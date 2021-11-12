
def imprime_matriz(matriz, T):
    ordem = len(matriz)
    string = " "
    if ordem != 2:
        for i in range(ordem):
            for j in range(ordem):
                tam_e = len(str(matriz[i][j]))
                menos = tam_e - 1
                if j == 0:
                    if tam_e < T:
                        print("%s%d" % (string * (T - menos - 1), matriz[i][j]), end="")
                    else:
                        print("%s%d" % (string * (T - 2 - (tam_e - 2)), matriz[i][j]), end="")
                elif j == ordem - 1:
                    if tam_e < T:
                        print(" %s%d" % (string * (T - menos - 1), matriz[i][j]))
                    else:
                        print(" %s%d" % (string * (T - 2 - (tam_e - 2)), matriz[i][j]))
                else:
                    if tam_e < T:
                        print(" %s%d" % (string * (T - menos - 1), matriz[i][j]), end="")
                    else:
                        print(" %s%d" % (string * (T - 2 - (tam_e - 2)), matriz[i][j]), end="")
    else:
        print("1 2\n2 4")
    print("")


while True:
    ordem = int(input(""))
    if ordem == 0:
        break
    else:
        if ordem == 1:
            val = 1
            print("%1d\n" % val)
        else:
            matriz = []
            maior = 0
            for i in range(ordem):
                linha = []
                for j in range(ordem):
                    termo = 2 ** (i + j)
                    if termo > maior:
                        maior = termo
                    linha.append(termo)
                matriz.append(linha)
            maior = str(maior)
            tam = len(maior)
            imprime_matriz(matriz, tam)

from sys import argv

# Criar matriz
n = int(argv[1])
mat = [[0] * n for _ in range(n)]

# Definir largura máxima para os números
width = len(str((2 ** (n - 1)) ** 2))

# Preencher a matriz
for x in range(n):
    for y in range(n):
        mat[y][x] = (2 ** x) * (2 ** y)

# Imprimir a matriz
for l in mat:
    for c in l:
        # A chave está aqui, ao utilizarmos {:{}d}.
        # O conjunto de {} interiores vai ser substituido por 'width',
        # antes de ser feita a substituição do {} de fora, que depois
        # será substituído por 'c'.
        print('{:{}d} '.format(c, width), end='')
    print('')

def imprime_matriz(matriz,T):
    ordem = len(matriz)
    string =" "
    if ordem!=2:
        for i in range(ordem):
            for j in range(ordem):
                tam_e = len(str(matriz[i][j]))
                menos = tam_e-1
                if j == 0:
                    if tam_e < T:
                        print("%s%d"%(string*(T-menos-1),matriz[i][j]),end="")
                    else:
                        print("%s%d"%(string*(T-2-(tam_e-2)),matriz[i][j]),end="")
                elif j == ordem-1:
                    if tam_e < T:
                        print(" %s%d"%(string*(T-menos-1),matriz[i][j]))
                    else:
                        print(" %s%d"%(string*(T-2-(tam_e-2)),matriz[i][j]))
                else:
                    if tam_e < T:
                        print(" %s%d"%(string*(T-menos-1),matriz[i][j]),end ="")
                    else:
                        print(" %s%d"%(string*(T-2-(tam_e-2)),matriz[i][j]),end ="")
    else:
        print("1 2\n2 4")
    print("")
while True:
    ordem = int(input(""))
    if ordem == 0:
        break
    else:
        if ordem==1:
            val = 1
            print("%1d\n"%val)
        else:
            matriz = []
            maior = 0
            for i in range(ordem):
                linha = []
                for j in range(ordem):
                    termo = 2**(i+j)
                    if termo>maior:
                        maior = termo
                    linha.append(termo)
                matriz.append(linha)
            maior = str(maior)
            tam = len(maior)
            imprime_matriz(matriz,tam)


from sys import argv

# Criar matriz
n = int(argv[1])
mat = [[0] * n for _ in range(n)]

# Definir largura máxima para os números
width = len(str((2 ** (n-1)) ** 2))

# Preencher a matriz
for x in range(n):
    for y in range(n):
        mat[y][x] = (2 ** x) * (2 ** y)

# Imprimir a matriz
for l in mat:
    for c in l:
        # A chave está aqui, ao utilizarmos {:{}d}.
        # O conjunto de {} interiores vai ser substituido por 'width',
        # antes de ser feita a substituição do {} de fora, que depois
        # será substituído por 'c'.
        print('{:{}d} '.format(c, width), end = '')
    print('')
