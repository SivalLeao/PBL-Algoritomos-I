"""/*******************************************************************
Autor: Sival Leão de Jesus
Componente Curricular: MI - Algoritmos I
Concluído em: 22/05/2022
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
**********************************************************************/"""

import os
#import os responsavel por limpar o terminal
#codigo fonte: https://github.com/python/cpython/tree/3.10/Lib/os.py
from time import sleep
#from time import sleep responsavel por gerar um atraso na execução do codigo
#codigo fonte: https://github.com/python/cpython/blob/main/Modules/timemodule.c
from random import randint
#import random responsavel por gera numeros pseudoaleatorios
#codigo fonte: https://github.com/python/cpython/tree/3.10/Lib/random.py


#funcao responsavel pelo atrazo de execuçao do codigo
def delay(a):
    sleep(a)
#funcao responsavel por limpar o terminal
def faxina():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#funcao usada apenas para avaliar o funcionamento do codigo
def dados(jogo_facil,somal_jogo_facil,jogo_facil_mostrar,historico1):
    
    print("matiz")
    for i in range(3):
        for s in range(3):
            print(f"[{jogo_facil[i][s]}]",end="")
        print()
    print("soma linha\ncolu x linh")
    for i in range(3):
        for s in range(3):       
            print(f"[{somal_jogo_facil[i][s]}]", end="")
        print()
    
    print("matriz que mostra")
    for i in range(4):
        for k in range(4):
            print(f"[{jogo_facil_mostrar[i][k]}]", end="")
        print()

#funcao responsavel pelo o valor absoluto da subtracao do valor chutado pela soma de linha ou coluna
def somaj1(cordenada1,escolha_valor1):
  somaC = {"c1":somal_jogo_facil[0][0],"c2":somal_jogo_facil[1][0],"c3":somal_jogo_facil[2][0]}
  somaL = {"l1":somal_jogo_facil[0][2],"l2":somal_jogo_facil[1][2],"l3":somal_jogo_facil[2][2]}
  
  if cordenada1[0] == "c":
      resultado_1 = (escolha_valor1 - somaC[cordenada1])
      if resultado_1 < 0:
          resultado_1 = resultado_1 * (-1)
  if cordenada1[0] == "l":
      resultado_1 = (escolha_valor1 - somaL[cordenada1])
      if resultado_1 < 0:
          resultado_1 = resultado_1 * (-1)
  return resultado_1
def somaj2(cordenada2,escolha_valor2):
    somaC = {"c1":somal_jogo_facil[0][0],"c2":somal_jogo_facil[1][0],"c3":somal_jogo_facil[2][0]}
    somaL = {"l1":somal_jogo_facil[0][2],"l2":somal_jogo_facil[1][2],"l3":somal_jogo_facil[2][2]}

    if cordenada2[0] == "c":
        resultado_2 = (escolha_valor2 - somaC[cordenada2])
        if resultado_2 < 0:
            resultado_2 = resultado_2 * (-1)
    if cordenada2[0] == "l":
        resultado_2 = (escolha_valor2 - somaL[cordenada2])
        if resultado_2 < 0:
            resultado_2 = resultado_2 * (-1)
    return resultado_2

#funcao responsavel por mostra o tabuleiro, historico e placar
def tabelaExibidaF():
    print("HISTORICO")
    print("Jogador 1: ",end="")
    for i in historico1: 
        print(i,end = " ")
    print()
    print("Jogador 2: ",end="")
    for i in historico2: 
        print(i,end = " ")
    print()
    print()
    print("PLACAR")
    for i in ponto1:
        for j in ponto2:
            print(f"J1: {i} X {j} :J2")
    print()


    for i in range(5):
        for k in range(5):
            print(f"[{jogo_facil_mostrar[i][k]}]".center(5), end="")
        print()
        print()


#
jogo_facil = [
[0,0,0],
[0,0,0],
[0,0,0]]
#
jogo_facilmaior = [
[0,0,0],
[0,0,0],
[0,0,0]]
jogo_facilmenor = [
[0,0,0],
[0,0,0],
[0,0,0]]
#
somal_jogo_facil = [
[0,0,0],
[0,0,0],
[0,0,0]]
jogo_facil_mostrar = [
["ッ","C1","C2","C3","+L"],
["L1","","","",""],
["L2","","","",""],
["L3","","","",""],
["+C","","","","ッ"]]
#
historico1 = []
historico2 = []
ponto1 = [0]
ponto2 = [0]
faxina()


#while pricipal
on = 0
while on == 0:
    novo = input("\033[1;95m<<<NEW GAME>>>\033[m".center(50)) #menu de novo jogo com o codigo de cores
    faxina()
    tabul = 0
    while tabul == 0:
        print("\033[1;95m<<<NÚMERO DE TABULEIRO>>>\033[m".center(50))
        print()
        tabuleiro = input("\033[1;33m(1)  ou (2): ")
        
        if tabuleiro != "1" and tabuleiro != "2":
            tabul = 0
            faxina()

        elif tabuleiro == "1":
            faxina()
            #while secundario menu de nivel
            niv = 0
            while niv == 0:
                print("\033[1;95m<<<NÍVEL>>>\033[m".center(50))
                print()
                print("\033[1;32m(1) FÁCIL   \033[m".center(50))
                print("\033[1;93m(2) MÉDIO   \033[m".center(50))
                print("\033[1;91m(3) DIFÍCIL\033[m\n".center(50))
                nivel = input("Digite o nível: ")

                if nivel != "1" and nivel != "2" and nivel != "3":
                    niv = 0
                    faxina()
                if nivel == "1":
                    faxina()
                    for i in range(3):
                        for j in range(3): 
                            fica = 0
                            while fica < 9:
                                aleatorio = randint(1,30)
                                if aleatorio != jogo_facil[0][0] and aleatorio != jogo_facil[0][1] and aleatorio != jogo_facil[0][2] and aleatorio != jogo_facil[1][0] and aleatorio != jogo_facil[1][1] and aleatorio != jogo_facil[1][2] and aleatorio != jogo_facil[2][0] and aleatorio != jogo_facil[2][1] and aleatorio != jogo_facil[2][2]: 
                                    
                                    jogo_facil[i][j] = aleatorio
                                    jogo_facilmaior[i][j] = aleatorio
                                    jogo_facilmenor[i][j] = aleatorio
                                    fica += 1
                    soma = 0
                    for d in range(3):
                        for l in range(3):
                            for c in range(3):
                                soma += jogo_facil[l][c]
                            somal_jogo_facil[l][c] = soma
                            soma = 0
                    
                    soma = 0
                    for d in range(3):
                        for l in range(3):
                            for c in range(3):
                                soma += jogo_facil[c][l]
                            somal_jogo_facil[l][0] = soma
                            soma = 0

               

                    """dados(jogo_facil,somal_jogo_facil,jogo_facil_mostrar,historico1)""" # usado para analisar o fucionamento
                    
                fim = 0
                while fim == 0:
                    print("\033[1;95m<<<COMO FINALIZAR O JOGO>>>\033[m".center(50))
                    finalizar = input("\033[1;33m(1) Até comppletar\n(2) Numero de jogadas: ")
                    if finalizar != "1" and finalizar != "2":
                        fim = 0

                    elif finalizar == "1":
                        play = 0
                        while play == 0:
                            
                                faxina()
                                lc1 = 0
                                while lc1 == 0:                                 
                                    print("ESCOLHA UMA LINHA OU COLUNA\nlinhas tem inicial L coluna C os numeros sao suas posicoes\na linhas 4 e a coluna 4 sao para mostrar o resultado\n")
                                            
                                    tabelaExibidaF()
                                    cordenada1 = input("JOGADOO 1\nL1, L2, L3\nC1, C2, C3\n>>>>>>> ").lower()
                                    if cordenada1 != "l1" and cordenada1 != "l2" and cordenada1 != "l3" and cordenada1 != "c1" and cordenada1 != "c2" and cordenada1 != "c3":          
                                        print("Dados nao encontrado")
                                        delay(0.75)
                                        lc1 = 0
                                        faxina()

                                    else:
                                        
                                        escolha_valor1 = input(f"qual o valor da soma de {cordenada1}: ").strip()
                                        while not escolha_valor1.isdigit() or (escolha_valor1 := int(escolha_valor1)) < 6 or escolha_valor1 > 87:
                                            escolha_valor1 = input(f"qual o valor da soma de {cordenada1} (esse valor não é possivel): ").strip()
                                        historico1.append(cordenada1)
                                        historico1.append(escolha_valor1)
                                        faxina()
                                        lc2 = 0
                                        while lc2 == 0:
                                            print("ESCOLHA UMA LINHA OU COLUNA\nlinhas tem inicial L coluna C os numeros sao suas posicoes\na linhas 4 e a coluna 4 sao para mostrar o resultado\n")
                                            
                                            tabelaExibidaF()
                                            cordenada2 = input("JOGADOO 2\nL1, L2, L3\nC1, C2, C3\n>>>>>>> ").lower()
                                            if cordenada2 != "l1" and cordenada2 != "l2" and cordenada2 != "l3" and cordenada2 != "c1" and cordenada2 != "c2" and cordenada2 != "c3":
                                                print("Dados nao encontrado")
                                                delay(0.75)
                                                lc2 = 0
                                                faxina()

                                            else:

                                                escolha_valor2 = input(f"qual o valor da soma de {cordenada2}: ").strip()
                                                while not escolha_valor2.isdigit() or (escolha_valor2 := int(escolha_valor2)) < 6 or escolha_valor2 > 87:
                                                    escolha_valor2 = input(f"qual o valor da soma de {cordenada2} (esse valor não é possivel): ").strip()
                                                historico2.append(cordenada2)
                                                historico2.append(escolha_valor2)
                                                lc2 += 1
                                            faxina()
                                            

#############################################################################################################################
                                        #todo trecho abaixo é responsavel por fazer com que os numeros sejam exibidos aos jogadores
                                            #play1igual
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "c1" and escolha_valor1 == somal_jogo_facil[0][0]:
                                                for i in range(3):
                                                    ponto1[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[i+1][1] = jogo_facil[i][0]
                                                        jogo_facilmaior[i][0] = -1
                                                        jogo_facilmenor[i][0] = 99
                                                historico1.append(3)
                                            
                                        
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "c2" and escolha_valor1 == somal_jogo_facil[1][0]:
                                                for i in range(3):
                                                    ponto1[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[i+1][2] = jogo_facil[i][1]
                                                        jogo_facilmaior[i][1] = -1
                                                        jogo_facilmenor[i][1] = 99


                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "c3" and escolha_valor1 == somal_jogo_facil[2][0]:
                                                for i in range(3):
                                                    ponto1[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[i+1][3] = jogo_facil[i][2]
                                                        jogo_facilmaior[i][2] = -1
                                                        jogo_facilmenor[i][2] = 99
                                        
                                        #play2 igual
                                        
                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "c1" and escolha_valor2 == somal_jogo_facil[0][0]:
                                                for i in range(3):
                                                    ponto2[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[i+1][1] = jogo_facil[i][0]    
                                                        jogo_facilmaior[i][0] = -1
                                                        jogo_facilmenor[i][0] = 99
                                                historico2.append(3)
                                            
                                        
                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "c2" and escolha_valor2 == somal_jogo_facil[1][0]:
                                                for i in range(3):
                                                    ponto2[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[i+1][2] = jogo_facil[i][1]    
                                                        jogo_facilmaior[i][1] = -1
                                                        jogo_facilmenor[i][1] = 99


                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "c3" and escolha_valor2 == somal_jogo_facil[2][0]:
                                                for i in range(3):
                                                    ponto2[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[i+1][3] = jogo_facil[i][2]    
                                                        jogo_facilmaior[i][2] = -1
                                                        jogo_facilmenor[i][2] = 99
                                                
                                                
#############################################################################################################################
                                        #play1igual l
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "l1" and escolha_valor1 == somal_jogo_facil[0][2]:
                                                for i in range(3):
                                                    ponto1[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[1][i+1] = jogo_facil[0][i]
                                                        jogo_facilmaior[0][i] = -1
                                                        jogo_facilmenor[0][i] = 99
                                                
                                            
                                        
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "l2" and escolha_valor1 == somal_jogo_facil[1][2]:
                                                for i in range(3):
                                                    ponto1[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[2][i+1] = jogo_facil[1][i]
                                                        jogo_facilmaior[1][i] = -1
                                                        jogo_facilmenor[1][i] = 99


                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "l3" and escolha_valor1 == somal_jogo_facil[2][2]:
                                                for i in range(3):
                                                    ponto1[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[3][i+1] = jogo_facil[2][i]
                                                        jogo_facilmaior[2][i] = -1
                                                        jogo_facilmenor[2][i] = 99
                                        
                                        #play2 igual
                                        
                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "l1" and escolha_valor2 == somal_jogo_facil[0][2]:
                                                for i in range(3):
                                                    ponto2[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[1][i+1] = jogo_facil[0][i]
                                                        jogo_facilmaior[0][i] = -1
                                                        jogo_facilmenor[0][i] = 99
                                                
                                            
                                        
                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "l2" and escolha_valor2 == somal_jogo_facil[1][2]:
                                                for i in range(3):
                                                    ponto2[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[2][i+1] = jogo_facil[1][i]
                                                        jogo_facilmaior[1][i] = -1
                                                        jogo_facilmenor[1][i] = 99


                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "l3" and escolha_valor2 == somal_jogo_facil[2][2]:
                                                for i in range(3):
                                                    ponto2[0] += 1
                                                    for i in range(3):
                                                        jogo_facil_mostrar[3][i+1] = jogo_facil[2][i]
                                                        jogo_facilmaior[2][i] = -1
                                                        jogo_facilmenor[2][i] = 99

###################################################################################################################################
                                        #play1maior
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "c1" and escolha_valor1 > somal_jogo_facil[0][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[i][0] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[i][0]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto1[0] += 1
                                                        jogo_facil_mostrar[ifalso+1][1] = cmaior_numero
                                                    if jogo_facil_mostrar[ifalso+1][1] == jogo_facil[ifalso][0]:
                                                        jogo_facilmaior[ifalso][0] = -1
                                                        jogo_facilmenor[ifalso][0] = 99
                                        #         
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "c2" and escolha_valor1 > somal_jogo_facil[1][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[i][1] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[i][1]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto1[0] += 1 
                                                        jogo_facil_mostrar[ifalso+1][2] = cmaior_numero
                                                    if jogo_facil_mostrar[ifalso+1][2] == jogo_facil[ifalso][1]:
                                                        jogo_facilmaior[ifalso][1] = -1
                                                        jogo_facilmenor[ifalso][1] = 99
                                        
                                        #         
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "c3" and escolha_valor1 > somal_jogo_facil[2][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[i][2] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[i][2]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto1[0] += 1
                                                        jogo_facil_mostrar[ifalso+1][3] = cmaior_numero
                                                    if jogo_facil_mostrar[ifalso+1][3] == jogo_facil[ifalso][2]:
                                                        jogo_facilmaior[ifalso][2] = -1
                                                        jogo_facilmenor[ifalso][2] = 99


                                        #play2
                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "c1" and escolha_valor2 > somal_jogo_facil[0][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[i][0] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[i][0]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto2[0] += 1
                                                        jogo_facil_mostrar[ifalso+1][1] = cmaior_numero
                                                    if jogo_facil_mostrar[ifalso+1][1] == jogo_facil[ifalso][0]:
                                                        jogo_facilmaior[ifalso][0] = -1
                                                        jogo_facilmenor[ifalso][0] = 99
                                        #         
                                        if somaj1(cordenada2,escolha_valor2) < somaj2(cordenada1,escolha_valor1):
                                            

                                            if cordenada2 == "c2" and escolha_valor2 > somal_jogo_facil[1][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[i][1] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[i][1]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto2[0] += 1    
                                                        jogo_facil_mostrar[ifalso+1][2] = cmaior_numero
                                                    if jogo_facil_mostrar[ifalso+1][2] == jogo_facil[ifalso][1]:
                                                        jogo_facilmaior[ifalso][1] = -1
                                                        jogo_facilmenor[ifalso][1] = 99
                                        
                                        #         
                                        if somaj1(cordenada2,escolha_valor2) < somaj2(cordenada1,escolha_valor1):
                                            

                                            if cordenada2 == "c3" and escolha_valor2 > somal_jogo_facil[2][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[i][2] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[i][2]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto2[0] += 1  
                                                        jogo_facil_mostrar[ifalso+1][3] = cmaior_numero
                                                    if jogo_facil_mostrar[ifalso+1][3] == jogo_facil[ifalso][2]:
                                                        jogo_facilmaior[ifalso][2] = -1
                                                        jogo_facilmenor[ifalso][2] = 99



#################################################################################################################################
                                        #play1 menor
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            print("entra onde eu quero")

                                            if cordenada1 == "c1" and escolha_valor1 < somal_jogo_facil[0][0]:
                                            
                                                cmenor_numero = 99
                                                cmaior_numero = -1
                                                ifalso = 0
                                                for i in range(3):   
                                                    if jogo_facilmenor[i][0] < cmenor_numero:
                                                        cmenor_numero = jogo_facil[i][0]
                                                        ifalso = i
                                                if cmenor_numero != 99:
                                                    ponto1[0] += 1
                                                    jogo_facil_mostrar[ifalso+1][1] = cmenor_numero
                                                if jogo_facil_mostrar[ifalso+1][1] == jogo_facil[ifalso][0]:
                                                    jogo_facilmaior[ifalso][0] = -1
                                                    jogo_facilmenor[ifalso][0] = 99
                                                    
                                        #        
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "c2" and escolha_valor1 < somal_jogo_facil[1][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[i][1] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[i][1]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto1[0] += 1 
                                                        jogo_facil_mostrar[ifalso+1][2] = cmenor_numero
                                                    if jogo_facil_mostrar[ifalso+1][2] == jogo_facil[ifalso][1]:
                                                        jogo_facilmaior[ifalso][1] = -1
                                                        jogo_facilmenor[ifalso][1] = 99
                                        
                                        #         
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "c3" and escolha_valor1 < somal_jogo_facil[2][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[i][2] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[i][2]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto1[0] += 1 
                                                        jogo_facil_mostrar[ifalso+1][3] = cmenor_numero
                                                    if jogo_facil_mostrar[ifalso+1][3] == jogo_facil[ifalso][2]:
                                                        jogo_facilmaior[ifalso][2] = -1
                                                        jogo_facilmenor[ifalso][2] = 99


                                        #play2
                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "c1" and escolha_valor2 < somal_jogo_facil[0][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[i][0] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[i][0]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto2[0] += 1
                                                        jogo_facil_mostrar[ifalso+1][1] = cmenor_numero
                                                    if jogo_facil_mostrar[ifalso+1][1] == jogo_facil[ifalso][0]:
                                                        jogo_facilmaior[ifalso][0] = -1
                                                        jogo_facilmenor[ifalso][0] = 99
                                        #         
                                        if somaj1(cordenada2,escolha_valor2) < somaj2(cordenada1,escolha_valor1):
                                            

                                            if cordenada2 == "c2" and escolha_valor2 < somal_jogo_facil[1][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[i][1] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[i][1]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto2[0] += 1 
                                                        jogo_facil_mostrar[ifalso+1][2] = cmenor_numero
                                                    if jogo_facil_mostrar[ifalso+1][2] == jogo_facil[ifalso][1]:
                                                        jogo_facilmaior[ifalso][1] = -1
                                                        jogo_facilmenor[ifalso][1] = 99
                                        
                                        #         
                                        if somaj1(cordenada2,escolha_valor2) < somaj2(cordenada1,escolha_valor1):
                                            

                                            if cordenada2 == "c3" and escolha_valor2 < somal_jogo_facil[2][0]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[i][2] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[i][2]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto2[0] += 1
                                                        jogo_facil_mostrar[ifalso+1][3] = cmenor_numero
                                                    if jogo_facil_mostrar[ifalso+1][3] == jogo_facil[ifalso][2]:
                                                        jogo_facilmaior[ifalso][2] = -1
                                                        jogo_facilmenor[ifalso][2] = 99                                            




###################################################################################################################################
                                        #play1maior
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "l1" and escolha_valor1 > somal_jogo_facil[0][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[0][i] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[0][i]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto1[0] += 1 
                                                        jogo_facil_mostrar[1][ifalso+1] = cmaior_numero
                                                    if jogo_facil_mostrar[1][ifalso+1] == jogo_facil[0][ifalso]:
                                                        jogo_facilmaior[0][ifalso] = -1
                                                        jogo_facilmenor[0][ifalso] = 99
                                        #         
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "l2" and escolha_valor1 > somal_jogo_facil[1][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[1][i] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[1][i]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto1[0] += 1 
                                                        jogo_facil_mostrar[2][ifalso+1] = cmaior_numero
                                                    if jogo_facil_mostrar[2][ifalso+1] == jogo_facil[1][ifalso]:
                                                        jogo_facilmaior[1][ifalso] = -1
                                                        jogo_facilmenor[1][ifalso] = 99
                                        
                                        #         
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "l3" and escolha_valor1 > somal_jogo_facil[2][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[2][i] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[2][i]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto1[0] += 1   
                                                        jogo_facil_mostrar[3][ifalso+1] = cmaior_numero
                                                    if jogo_facil_mostrar[3][ifalso+1] == jogo_facil[2][ifalso]:
                                                        jogo_facilmaior[2][ifalso] = -1
                                                        jogo_facilmenor[2][ifalso] = 99


                                        #play2
                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "l1" and escolha_valor2 > somal_jogo_facil[0][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[0][i] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[0][i]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto2[0] += 1
                                                        jogo_facil_mostrar[1][ifalso+1] = cmaior_numero
                                                    if jogo_facil_mostrar[1][ifalso+1] == jogo_facil[0][ifalso]:
                                                        jogo_facilmaior[0][ifalso] = -1
                                                        jogo_facilmenor[0][ifalso] = 99
                                        #         
                                        if somaj1(cordenada2,escolha_valor2) < somaj2(cordenada1,escolha_valor1):
                                            

                                            if cordenada2 == "l2" and escolha_valor2 > somal_jogo_facil[1][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[1][i] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[1][i]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto2[0] += 1   
                                                        jogo_facil_mostrar[2][ifalso+1] = cmaior_numero
                                                    if jogo_facil_mostrar[2][ifalso+1] == jogo_facil[1][ifalso]:
                                                        jogo_facilmaior[1][ifalso] = -1
                                                        jogo_facilmenor[1][ifalso] = 99
                                        
                                        #         
                                        if somaj1(cordenada2,escolha_valor2) < somaj2(cordenada1,escolha_valor1):
                                            

                                            if cordenada2 == "l3" and escolha_valor2 > somal_jogo_facil[2][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmaior[2][i] > cmaior_numero:
                                                            cmaior_numero = jogo_facil[2][i]
                                                            ifalso = i
                                                    if cmaior_numero != -1:
                                                        ponto2[0] += 1 
                                                        jogo_facil_mostrar[3][ifalso+1] = cmaior_numero
                                                    if jogo_facil_mostrar[3][ifalso+1] == jogo_facil[2][ifalso]:
                                                        jogo_facilmaior[2][ifalso] = -1
                                                        jogo_facilmenor[2][ifalso] = 99



#################################################################################################################################
                                        #play1 menor
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            print("entra onde eu quero")

                                            if cordenada1 == "l1" and escolha_valor1 < somal_jogo_facil[0][2]:
                                            
                                                cmenor_numero = 99
                                                cmaior_numero = -1
                                                ifalso = 0
                                                for i in range(3):   
                                                    if jogo_facilmenor[0][i] < cmenor_numero:
                                                        cmenor_numero = jogo_facil[0][i]
                                                        ifalso = i
                                                if cmenor_numero != 99:
                                                    ponto1[0] += 1
                                                    jogo_facil_mostrar[1][ifalso+1] = cmenor_numero
                                                if jogo_facil_mostrar[1][ifalso+1] == jogo_facil[0][ifalso]:
                                                    jogo_facilmaior[0][ifalso] = -1
                                                    jogo_facilmenor[0][ifalso] = 99
                                                    
                                        #        
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "l2" and escolha_valor1 < somal_jogo_facil[1][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[1][i] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[1][i]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto1[0] += 1
                                                        jogo_facil_mostrar[2][ifalso+1] = cmenor_numero
                                                    if jogo_facil_mostrar[2][ifalso+1] == jogo_facil[1][ifalso]:
                                                        jogo_facilmaior[1][ifalso] = -1
                                                        jogo_facilmenor[1][ifalso] = 99
                                        
                                        #         
                                        if somaj1(cordenada1,escolha_valor1) < somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada1 == "l3" and escolha_valor1 < somal_jogo_facil[2][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[2][i] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[2][i]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto1[0] += 1 
                                                        jogo_facil_mostrar[3][ifalso+1] = cmenor_numero
                                                    if jogo_facil_mostrar[3][ifalso+1] == jogo_facil[2][ifalso]:
                                                        jogo_facilmaior[2][ifalso] = -1
                                                        jogo_facilmenor[2][ifalso] = 99


                                        #play2
                                        if somaj1(cordenada1,escolha_valor1) > somaj2(cordenada2,escolha_valor2):
                                            

                                            if cordenada2 == "l1" and escolha_valor2 < somal_jogo_facil[0][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[0][i] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[0][i]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto2[0] += 1
                                                        jogo_facil_mostrar[1][ifalso+1] = cmenor_numero
                                                    if jogo_facil_mostrar[1][ifalso+1] == jogo_facil[0][ifalso]:
                                                        jogo_facilmaior[0][ifalso] = -1
                                                        jogo_facilmenor[0][ifalso] = 99
                                        #         
                                        if somaj1(cordenada2,escolha_valor2) < somaj2(cordenada1,escolha_valor1):
                                            

                                            if cordenada2 == "l2" and escolha_valor2 < somal_jogo_facil[1][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        if jogo_facilmenor[1][i] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[1][i]
                                                            ifalso = i
                                                    if cmenor_numero != 99:
                                                        ponto2[0] += 1 
                                                        jogo_facil_mostrar[2][ifalso+1] = cmenor_numero
                                                    if jogo_facil_mostrar[2][ifalso+1] == jogo_facil[ifalso][1]:
                                                        jogo_facilmaior[1][ifalso] = -1
                                                        jogo_facilmenor[1][ifalso] = 99
                                        
                                        #         
                                        if somaj1(cordenada2,escolha_valor2) < somaj2(cordenada1,escolha_valor1):

                                            if cordenada2 == "l3" and escolha_valor2 < somal_jogo_facil[2][2]:
                                                
                                                    cmenor_numero = 99
                                                    cmaior_numero = -1
                                                    ifalso = 0
                                                    for i in range(3):
                                                        ponto2[0] += 1
                                                        if jogo_facilmenor[2][i] < cmenor_numero:
                                                            cmenor_numero = jogo_facil[2][i]
                                                            ifalso = i
                                                    if cmaior_numero != -1:    
                                                        jogo_facil_mostrar[3][ifalso+1] = cmenor_numero
                                                    if jogo_facil_mostrar[3][ifalso+1] == jogo_facil[2][ifalso]:
                                                        jogo_facilmaior[2][ifalso] = -1
                                                        jogo_facilmenor[2][ifalso] = 99              

                                    #mostra resultado de soma linha
                                    #l1
                                    if jogo_facil_mostrar[1][1] == jogo_facil[0][0] and jogo_facil_mostrar[1][2] == jogo_facil[0][1] and jogo_facil_mostrar[1][3] == jogo_facil[0][2]:
                                        jogo_facil_mostrar[1][4] = somal_jogo_facil[0][2]
                                    #L2
                                    if jogo_facil_mostrar[2][1] == jogo_facil[1][0] and jogo_facil_mostrar[2][2] == jogo_facil[1][1] and jogo_facil_mostrar[2][3] == jogo_facil[1][2]:
                                        jogo_facil_mostrar[2][4] = somal_jogo_facil[1][2]
                                    #L3
                                    if jogo_facil_mostrar[3][1] == jogo_facil[2][0] and jogo_facil_mostrar[3][2] == jogo_facil[2][1] and jogo_facil_mostrar[3][3] == jogo_facil[2][2]:
                                        jogo_facil_mostrar[3][4] = somal_jogo_facil[2][2]

                                    #mostra resultado de soma coluna
                                    #C1
                                    if jogo_facil_mostrar[1][1] == jogo_facil[0][0] and jogo_facil_mostrar[2][1] == jogo_facil[1][0] and jogo_facil_mostrar[3][1] == jogo_facil[2][0]:
                                        jogo_facil_mostrar[4][1] = somal_jogo_facil[0][0]
                                    #C2
                                    if jogo_facil_mostrar[1][2] == jogo_facil[0][1] and jogo_facil_mostrar[2][2] == jogo_facil[1][1] and jogo_facil_mostrar[3][2] == jogo_facil[2][1]:
                                        jogo_facil_mostrar[4][2] = somal_jogo_facil[1][0]
                                    #L3
                                    if jogo_facil_mostrar[1][3] == jogo_facil[0][2] and jogo_facil_mostrar[2][3] == jogo_facil[1][2] and jogo_facil_mostrar[3][3] == jogo_facil[2][2]:
                                        jogo_facil_mostrar[4][3] = somal_jogo_facil[2][0]

                                    #para finalizar o jogo
                                    if jogo_facil_mostrar[4][1] == somal_jogo_facil[0][0] and jogo_facil_mostrar[4][2] == somal_jogo_facil[1][0] and jogo_facil_mostrar[4][3] == somal_jogo_facil[2][0] and jogo_facil_mostrar[1][4] == somal_jogo_facil[0][2] and jogo_facil_mostrar[2][4] == somal_jogo_facil[1][2] and jogo_facil_mostrar[3][4] == somal_jogo_facil[2][2]:
                                        faxina()
                                        print("FIM DE JOGO\n")
                                        if ponto1[0] > ponto2[0]:
                                            print("JOGADOR 1 GANHOU!!!\nPARABÉNS")
                                        else:
                                            print("JOGADOR 2 GANHOU!!!\nPARABÉNS")
                                        delay(5)
                                        faxina()
                                        print("OBRIGADO POR JOGAR")
                                    delay(5)
                                    fim += 1
                                    lc1 += 1
                                    lc2 += 1
                                    tabul += 1
                                    on += 1
                                        


                                            
