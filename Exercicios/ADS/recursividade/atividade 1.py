def fibonacci(x):

    if x == 1:
        return 0
    elif x == 2:
        return 1
    elif x > 2:
        return  fibonacci(x-1) + fibonacci(x-2)

def valor(a):
    for x in range(1,a+1):
        print(fibonacci(x))


while True:
    d = int(input('digite os termos que deseja saber a fibonacc :'))
    valor(d)
