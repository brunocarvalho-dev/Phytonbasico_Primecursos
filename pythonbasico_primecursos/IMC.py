import math
nome = input("Digite seu nome: ")
altura = input("Digite su altura: ")
altura = float(altura.replace(",","."))
peso =  input("Digite seu peso: ")
peso = float(peso.replace(",","."))

imc = (peso/(math.pow(altura, 2)))
print(peso, altura,  imc)
if (imc < 18.5):
    print(nome + " você está abaixo do peso")
elif(imc < 24.9):
    print(nome+ " você está no peso ideal, Parabens!")
elif(imc < 29.9):
    print (nome+ " você está com obrepeso")
elif(imc < 34.9):
    print(nome+ " você está com obesidade grau I")
elif(imc < 39.9):
    print(nome +" você está com obesidade Grau II severa")
else:
    print(nome+ " você está com obesidade III morbida")
