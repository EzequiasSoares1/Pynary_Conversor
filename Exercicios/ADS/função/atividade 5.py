def notas(d):
    o = []
    o = d
    o.sort(reverse=True)
    m = []
    for x in range(30):
       m.append(o[x])

    return m


candidatos = []

print(notas(candidatos))
