###################################################
# MC102 - Algoritmos e Programação de Computadores ( MC-102 Algorithms and computer programming )
# Lab 2 - A sandwich before class starts
# 
# Description: The objective of this lab was to calculate which path, according to the inputted data, 
# which of them was faster to arrive on time for class, but having a lunch mid while. 
#
#   For each test made, the code should receive the information about the time, that was the "T" variable.
# Also would be processed the info about the prices of the sandwichs in the "L1" and "L2" variables, each one 
# for each path. And the time of each bus was received in the "P's" variables. 
###################################################

# Leitura da entrada
# Sandwichs
T = int(input(""))
L1 = int(input(""))
L2 = int(input(""))
# Path times
P1 = int(input(""))
P2 = int(input(""))
P3 = int(input(""))
#

# Comparation between the inputted times
isPath1Better = True
timePath1 = P1 + P2 + T
timePath2 = P3 + T
menorPreco = min(L1, L2)
menorTempo = min(timePath1, timePath2)

if(timePath1 < 45 and timePath2 < 45):
    if(L1 == L2):
        print(isPath1Better) 
    elif (menorPreco == L1):
        print(isPath1Better) 
    else: 
        isPath1Better = False
        print(isPath1Better) 
else:
    if(timePath1 == timePath2):
        if(menorPreco == L1):
            print(isPath1Better) 
        else:
            isPath1Better = False
            print(isPath1Better) 
    elif (menorTempo == timePath1):
        print(isPath1Better) 
    else:
        isPath1Better = False
        print(isPath1Better) 
