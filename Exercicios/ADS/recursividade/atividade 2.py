def s(n):
    if len(n) == 1:
        return 1

    else:
        return 1 + s(n[1:])

while True:
    e = str(input())
    print('A palavra digitada tem {} Digitos'.format(s(e)))



