capital = input("Digite o capital inicial R$ ")
capital = float(capital.replace(",","."))
juros = input("Digite a taxa de juros em %")
juros = float(juros.replace(",","."))
tempo = int(input("Digite o prazo em meses"))

for i in range(tempo):
    capital += capital * ((juros /100))
    print(capital)

print("a parcela fica {:.2f}, por {} meses".format((capital/tempo),tempo))