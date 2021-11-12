def f(op,li):
    if op == 'S' or op == 's':
        def soma(n):
            if len(n) == 1:
                return int(n[0])

            else:
                return int(n[0]) + soma(n[1:])

        print(soma(li))

    elif op == 'M' or op == 'm':
        def m(n):
            if len(n) == 1:
                return int(n[0])
            
            else:
                return int(n[0])* m(n[1:])

        print(m(li))

    else:
        print('Operação inválida')

        
f('m',[2,3])
