###################################################
# MC102 - Algoritmos e Programação de Computadores ( MC-102 Algorithms and computer programming )
# Lab 3 - Investments
# 
# Description: At this lab, the information that should be received was the inicial amount of money, the
# number of days that the money will be invested and the investment return rate of the both investments
# that are being compared.
# 
#   At the end, the programm should return the final value of each investment and which had the biggest return.
#  
###################################################

# leitura de dados
inicialAmmount = float(input())
numD = int(input())
jurosPoupanca = 1 + float(input())/100
jurosPreFix = 1 + float(input())/100

# cálculo dos rendimentos

poupanca = 0.0
tesouro = 0.0
months = 0

for months in range(numD//30): 
    poupanca += ((inicialAmmount * jurosPoupanca) - poupanca) - inicialAmmount
    tesouro += ((inicialAmmount * jurosPreFix) - tesouro) - inicialAmmount

if(numD <= 180):
    tesouro = tesouro - (tesouro * 0.225)
elif(numD > 180 and numD <= 360):
    tesouro = tesouro - (tesouro * 0.2)
elif(numD > 360 and numD <= 720):
    tesouro = tesouro - (tesouro * 0.175)
else:
    tesouro = tesouro - (tesouro * 0.15)

# Impressão da saída
print("Rendimento poupança: {:.2f}".format(poupanca))
print("Rendimento tesouro: {:.2f}".format(tesouro))

if poupanca > tesouro:
    print("Maior rendimento: poupança")
else:
    print("Maior rendimento: tesouro")
