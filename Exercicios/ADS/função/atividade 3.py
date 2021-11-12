def string(n):
    f = []
    f = n
    cont = 0
    for x in range(len(f)):
        if f[x].isnumeric() == True:
            cont += 1

    return cont


r = ''
print(string(r))
