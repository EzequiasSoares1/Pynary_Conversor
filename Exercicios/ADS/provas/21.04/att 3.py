def m(n):
    if len(n) == 1:
        return int(n[0])
    else:
        return int(n[0])* m(n[1:])



print(m([4,5]))
