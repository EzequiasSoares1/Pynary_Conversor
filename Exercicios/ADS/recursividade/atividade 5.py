def vetor(n):
    if len(n) == 1:
        return float(n[0])

    else:
        return float(n[0]) + vetor(n[1:])


d = [6.0, 8.0, 7.0, 8.0]
print(vetor(d))
