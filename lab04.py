###################################################
# MC102 - Algoritmos e Programação de Computadores ( MC-102 Algorithms and computer programming )
# Lab 4 - A Pokemon battle
# 
# Description: The name says it all, the programm receives data about the life of the two pokes and it's
# speed, what decides who attacks firts, after that a repetition structure will display two new inputs for
# each poke at each round to receive the info about the attack damage and the potencializer, info that
# will be used to calculate the HP of each poke at each round, then after one of the pokes get's his life 
# equals to zero, the program displays the winner and it's HP. 
###################################################

# Leitura do hp e velocidade dos pokémons
hpIvysaur = int(input(""))
hpPikachu = int(input(""))
speedIvysaur = int(input(""))
speedPikachu = int(input(""))

# Leitura dos ataques dos turnos

while hpIvysaur > 0 and hpPikachu > 0:
    if(speedIvysaur > speedPikachu):
        if(hpIvysaur != 0):
            hpPikachu -= ((int(input(""))) * (float(input(""))))
            if(hpPikachu < 0):
                hpPikachu = 0
        else:
            print("HP Ivysaur =",int(hpIvysaur))
            print("HP Pikachu =",int(hpPikachu))
            break
        if(hpPikachu != 0):
            hpIvysaur -= ((int(input(""))) * (float(input(""))))
            if(hpIvysaur < 0):
                hpIvysaur = 0
        else:
            print("HP Ivysaur =",int(hpIvysaur))
            print("HP Pikachu =",int(hpPikachu))
            break
    else:
        if(hpPikachu != 0):
            hpIvysaur -= ((int(input(""))) * (float(input(""))))
            if(hpIvysaur < 0):
                hpIvysaur = 0
        else:
            print("HP Ivysaur =",int(hpIvysaur))
            print("HP Pikachu =",int(hpPikachu))
            break
        if(hpIvysaur != 0):
            hpPikachu -= ((int(input(""))) * (float(input(""))))
            if(hpPikachu < 0):
                hpPikachu = 0
        else:
            print("HP Ivysaur =",int(hpIvysaur))
            print("HP Pikachu =",int(hpPikachu))
            break

    print("HP Ivysaur =",int(hpIvysaur))
    print("HP Pikachu =",int(hpPikachu))

if(hpIvysaur > hpPikachu):
    print("Pokémon Vencedor: Ivysaur")
    print("HP do Vencedor:", int(hpIvysaur))
else:
    print("Pokémon Vencedor: Pikachu")
    print("HP do Vencedor:", int(hpPikachu))
