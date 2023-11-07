###################################################
# MC102 - Algoritmos e Programação de Computadores ( MC-102 Algorithms and computer programming )
# Lab 5 - Last chance to win the prize
# 
# Description: At this lab, we received the infos about the number of parts of a roulette ("N"), the amount of 
# money that the player will  consider a winning ("V") and the amount of money accumulated till this round of 
# the game ("P").
#   Then, we will just calculate the chance at the last round, in all of the possible results, that the player 
# will leave with the ammount that he will consider a fulfilling winning. 
###################################################

# Leitura da primeira linha
N, V, P = input().split()
N = int(N)
V = int(V)
P = int(P)

# Leitura da roleta

i = 1
premio_medio = 0
prob_viagem = 0
valorRodada = 0
premios = 0
premio_sortudo = 0

for i in range(N):
    resultadoRodada = input()
    operacaoRodada = resultadoRodada[0]

    if "R" in resultadoRodada and operacaoRodada == "-" :
        valorResultadoInt = int(resultadoRodada[1:resultadoRodada.index("R")])
        valorRodada = (P - valorResultadoInt)

    elif "R" in resultadoRodada and operacaoRodada != "-":
        valorResultadoInt = int(resultadoRodada[1:resultadoRodada.index("R")])
        valorRodada = (P + valorResultadoInt)

    elif "%" in resultadoRodada and operacaoRodada == "-":
        valorResultadoPct = int(resultadoRodada[1:resultadoRodada.index("%")])
        rendimento =  P * (valorResultadoPct/100)
        valorRodada = (P - rendimento) 

    elif "%" in resultadoRodada and operacaoRodada != "-" :
        valorResultadoPct = int(resultadoRodada[1:resultadoRodada.index("%")]) 
        rendimento =  P * (valorResultadoPct/100)
        valorRodada = (P + rendimento) 
    else:
        print("Erro")

    if(valorRodada >= V):
        premio_sortudo += 1 
    if( valorRodada > 0):
        premios += valorRodada
    

# Calculo da probabilidade
prob_viagem = (premio_sortudo/N) * 100
premio_medio = premios/N


# Imprime a probabilidade do premio final ser suficiente para a viagem
print("{:.2f}%".format(prob_viagem))
# Imprime o valor médio do premio final a ser recebido
print("R$ {:.2f}".format(premio_medio))
