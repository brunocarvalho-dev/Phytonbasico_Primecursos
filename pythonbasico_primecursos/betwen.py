
userNumber = float(input("Digite um número: "))


if((userNumber > 100) and (userNumber < 200)):
    print("O valor {:.0f} está entre 100 e 200".format(userNumber))
else:
    print('Valor fora do intervalo')