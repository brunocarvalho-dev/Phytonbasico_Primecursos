numero = int(input("Digite um número para ver sua tabuada"))


print("\nTabuada do numero: {}".format(numero))
for i in range (0,11):
    print("{:.0f} X {:.0f} = {:.0f}".format(numero,i,(i*numero)))