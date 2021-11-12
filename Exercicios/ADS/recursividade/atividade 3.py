def s(n):
    if len(n) == 1:
        if n[0].isnumeric() == True:
            if n[0] == '1':
                return 1
        else:
            return 0

    else:
        if n[0].isnumeric() == True:
            if n[0] == '1':
                return 1 + s(n[1:])
            else:
                return s(n[1:])
        else:
            return s(n[1:])


while True:
    e = str(input('Digite:'))
    print(s(e))
