def s(n):
    if len(n) == 1:
        return int(n)

    else:
        return int(n[0]) + s(n[1:])


e = str(input('Digite os numeros:'))
d = e.replace('', '+').strip('+')
print(d, '=', s(e))

