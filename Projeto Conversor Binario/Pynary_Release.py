import time
import sys
from random import *

def help_commands():
    print("Você pode:")
    print("a. Converter Binário para Decimal")
    print("b. Converter Decimal para Binário")
    print("c. Realizar operações com números binários")
    time.sleep(1)
    print()
    print("Para executar uma ação, digite sua letra correspondente e aperte Enter")
    time.sleep(1)
    print()
    print("Digite \"ajuda\" para mostrar estes comandos novamente")
    time.sleep(1)
    print("Digite \"sair\" para encerrar o programa")
    time.sleep(1)
    print("Digite \"voltar\" enquanto em uma operação para retornar a seleção de operações")
    time.sleep(2)

def options():
    while True:
        print()
        option = input("O que você quer fazer? ")

        if option == "ajuda":
            print()
            help_commands()

        elif option == "sair":
            sys.exit()

        elif option == "a":
            conv_bin_to_dem()

        elif option == "b":
            dem_to_bin()

        elif option == "c":
            bin_ops()

        else:
            print("Opção inválida")
            print("Digite ajuda para ver uma lista de opções disponíveis")
            time.sleep(2)

def conv_bin_to_dem():
    binary_split = []
    binary = 0
    isValidBin = False

    binary = input("Digite um número binário: ")

    if binary == "voltar":
        options()

    binary_split = [c for c in binary]

    for i in range(len(binary_split)):
        current_bin = binary_split.pop(0)
        try:
            if not (int(current_bin) == 1 or int(current_bin) == 0):
                isValidBin = False
                break
            else:
                isValidBin = True
        except ValueError:
            print("O número não foi digitado corretamente")
            time.sleep(2)
            conv_bin_to_dem()

    if isValidBin == True:
        bin_to_dem = int(binary,2)
        print()
        print("{} em decimal é: {}" .format(binary, bin_to_dem))
        time.sleep(2)
    elif isValidBin == False:
        print("O número não foi digitado corretamente")
        time.sleep(2)
        conv_bin_to_dem()

def dem_to_bin():
    while True:
        decimal = input("Digite um número decimal: ")

        if decimal == "voltar":
            options()

        try:
            dem_to_bin = int(decimal)
            dem_to_bin = bin(dem_to_bin).replace("0b", "")
            isValidDem = True
        except ValueError:
            isValidDem = False


        if isValidDem == False:
            print("O número não foi digitado corretamente")
            time.sleep(2)

        elif isValidDem:
            print()
            print("{} em binário é: {}" .format(decimal, dem_to_bin))
            time.sleep(2)
            break

def bin_ops():
    binary_operation = 0
    bin1 = 0
    bin2 = 0
    operation = 0

    avail_ops = ["+", "-", "*", "/"]

    randBin1 = randint(1, 100)
    randBin2 = randint(1, 100)
    randOps = avail_ops[randint(0, 3)]

    randBin1 = "{0:b}".format(randBin1)
    randBin2 = "{0:b}".format(randBin2)

    binary_operation = input("Digite a operação (ex.: {} {} {}): " .format(randBin1, randOps, randBin2))

    if binary_operation == "voltar":
        options()

    try:
        bin1,operation,bin2 = binary_operation.split()
    except ValueError:
        print("A operação não foi digitada corretamente")
        time.sleep(1)
        bin_ops()

    bin1_split = [c for c in bin1]
    bin2_split = [c for c in bin2]

    for i in range(len(bin1_split)):
        current_bin = bin1_split.pop(0)

        if not (int(current_bin) == 1 or int(current_bin) == 0):
            isValidBin1 = False
            break
        else:
            isValidBin1 = True

    for i in range(len(bin2_split)):
        current_bin = bin2_split.pop(0)

        if not (int(current_bin) == 1 or int(current_bin) == 0):
            isValidBin2 = False
            break
        else:
            isValidBin2 = True

    if not (operation in avail_ops):
        print("A operação não foi digitada corretamente")
        time.sleep(1)
        bin_ops()

    if (isValidBin1 == True and isValidBin2 == True):
        bin1 = int(bin1,2)
        bin2 = int(bin2,2)

        if operation == "+":
            result = bin1 + bin2
        elif operation == "-":
            result = bin1 - bin2
        elif operation == "*":
            result = bin1 * bin2
        elif operation == "/":
            result = bin1 / bin2

        result = bin(int(result)).replace("0b", "")
        print("O resultado é: {} ({})" .format(result, (int(result,2))))

    elif (isValidBin1 == False and isValidBin2 == False):
        print("Nenhum dos números foram digitados corretamente")
        time.sleep(2)
        bin_ops()

    elif isValidBin1 == False:
        print("O primeiro número não foi digitado corretamente")
        time.sleep(2)
        bin_ops()

    elif isValidBin2 == False:
        print("O segundo número não foi digitado corretamente")
        time.sleep(2)
        bin_ops()

print("Bem-vindo ao Pynary!")
time.sleep(1)
print()
print("Digite \"ajuda\" para mostrar os comandos disponíveis")
time.sleep(2)
options()
