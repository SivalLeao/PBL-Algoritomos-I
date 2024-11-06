"""/*******************************************************************
Autor: Sival Leão de Jesus
Componente Curricular: MI - Algoritmos I
Concluído em: 10/04/2022
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
**********************************************************************/"""


#variaveis
#as variaveis sem "_" são as que o programa ira fazer as operacoes de soma e subtracao para calculo das cestas e itens
#as variaveis com "_j" armazena o total de um determinado item ou produto doado por pessoas jurídicas
#as variaveis com "_f" armazena o total de um determinado item ou produto doado por pessoas físicas
#as variaveis com "_t" armazena o total recebido de um determinado item ou produto
#existe algumas exeções, porem são autoexplicativas (onde "p" = pessoa "ext" = extra )
#
acucar = 0
acucar_j = 0
acucar_f = 0
acucar_t = 0
#
arroz = 0
arroz_j = 0
arroz_f = 0
arroz_t = 0
#
cafe = 0
cafe_j = 0
cafe_f = 0
cafe_t = 0
#
extrato_de_tomate = 0
extrato_de_tomate_j = 0
extrato_de_tomate_f = 0
extrato_de_tomate_t = 0
#
macarrao = 0
macarrao_j = 0
macarrao_f = 0
macarrao_t = 0
#
pct_bolacha = 0
pct_bolacha_j = 0
pct_bolacha_f = 0
pct_bolacha_t = 0
#
oleo = 0
oleo_j = 0
oleo_f = 0
oleo_t = 0
#
farinha_de_trigo = 0
farinha_de_trigo_j = 0
farinha_de_trigo_f = 0
farinha_de_trigo_t = 0
#
feijao = 0
feijao_j = 0
feijao_f = 0
feijao_t = 0
#
sal = 0
sal_j = 0
sal_f = 0
sal_t = 0
#
total_extra = 0
extra = 0
#
cesta_basica = 0
cesta_basica_t = 0
cesta_basica_ex =0
#variaves pessoa
p_fisica_kg = 0
p_fisica_l = 0
p_fisica_pct = 0
p_fisica_un = 0
p_fisica_ext = 0
#
p_juridica_kg = 0
p_juridica_l = 0
p_juridica_pct = 0
p_juridica_un = 0
p_juridica_ext = 0


#a lista de alimentos serve exclusivamente para evita a repeticao dos inputs deste programa
#as demais lista nao sera importante para o funcionamento do codigo porem armazena alguns dados inserido pelo usuario 
#listas
alimentos =["açúcar", "arroz", "café", "extrato de tomate", "macarrão", "pct de bolacha", "óleo", "farinha de trigo", "feijão", "sal"]
nome_doador = []
nome_doador_j = []
nome_doador_f = []
itens_extra = []
itens_extra_num =[]

#prints de aviso
print("="*100)
print(" "*40,"ATENÇÃO!\n")
print("""   Esse código é desenvolvido na linguagem Python, linguagem essa que tem como fundação
a língua inglesa, ou seja, as operações matemáticas e entrada de dados vai respeitar
as normas da língua inglesas onde os números decimais utilizam um ponto ".", e não uma vírgula ",",
para separar a parte inteira da parte decimal.""")

enter = input("\nPress Enter para continuar")

#mensagem de boas vindas 
print("="*100)
print("\n                         Seja Bem-vindo")
print("                              Ao")
print("Sistema de Gerenciamento de Doações e Montagem de Cestas Básicas.")
print(" "*20,"Dispensário Santana")
enter = input("\nPress Enter para continuar ")

#condicao para o while funcionar o valor de "on" altera dependendo da situacao
on = 0
#loop para o codigo sempre roda
#menu
while on == 0:
    print("="*100)
    print()
    print("-="*5,"MENU","=-"*5 )
    menu = input("\nDigite 1 para doações \nDigite 2 para ver o relatorio \nDigite 3 para encerrar \n>>> ")
    #verificacao se a entrada inserida é correta, caso contrario repete a pergunta 
    if menu != "1" and menu != "2" and menu != "3":
        on = 0

    #primeira condicional para menu (CADASTRO)
    elif menu == "1":
        print("="*100)
        nome = input("\nNome do doador: ").strip()    
        while not nome.replace(" ","").isalpha():
            nome = input("Nome do doador (A nome deve conter apenas letras): ")
        nome_doador.append(nome)
        print()    
        print("="*100)
        #tipo de pessoa
        off = 0
        while off == 0:
            tipo_pessoa = input("\nDigite  [ F ] para pessoa Física \nDigite [ J ] para pessoa Jurídica: ").strip().lower()
            if tipo_pessoa != "f" and tipo_pessoa != "j":
                print("Digite  apenas [ F ] ou [ J ]")
                off = 0
            elif tipo_pessoa == "f":
                nome_doador_f.append(nome)
                off += 1
            elif tipo_pessoa == "j":
                nome_doador_j.append(nome)
                off += 1
        print()
        print("="*45,nome,"="*45)
        print()
        #for para nao repetir os inputs como dito anteriormente
        for i in alimentos:
            #entradas
            #condicionais utilizadas para separa a unidade de medida de cada produto
            if i == "extrato de tomate" or i == "pct de bolacha" or i == "macarrão":
                doacao =""
                while type(doacao) != int:
                    try:
                        doacao = int(input(f"Quantos {i} você deseja doar: "))
                        while doacao < 0:
                            doacao = int(input(f"Quantos {i} você deseja doar(apenas numero maior que zero): "))     
                    except ValueError:
                        print("ERRO!!! Por Favor Digite Apenas Numeros Validos")
                        doacao = ""
                
                #atribuicao de valores as variaveis
                #codicoes extrato de tomate
                if i == "extrato de tomate":
                    extrato_de_tomate += doacao
                    extrato_de_tomate_t += doacao
                   
                if i == "extrato de tomate" and tipo_pessoa == "j":
                    extrato_de_tomate_j += doacao
                    
                    p_juridica_un += doacao
                if i == "extrato de tomate" and tipo_pessoa == "f":
                    extrato_de_tomate_f += doacao
                    p_fisica_un += doacao
                #condicoes pct de bolacha
                if i == "pct de bolacha":
                    pct_bolacha += doacao
                    pct_bolacha_t += doacao
                    
                    
                if i == "pct de bolacha" and tipo_pessoa == "j":
                    pct_bolacha_j += doacao
                     
                    p_juridica_pct += doacao
                if i == "pct de bolacha" and tipo_pessoa == "f":
                    pct_bolacha_f += doacao
                    
                    p_fisica_pct += doacao
                #condicoes macarrao
                if i == "macarrão":
                    macarrao += doacao
                    macarrao_t += doacao
                    
                    if tipo_pessoa == "j":
                        macarrao_j += doacao      
                        p_juridica_un += doacao

                    else:
                        macarrao_f += doacao
                        p_fisica_un += doacao


            #codicoes oleo
            elif i == "óleo":
                doacao =""
                while type(doacao) != float:
                    try:
                        doacao = float(input(f"Quantos litros de {i} você deseja doar: "))
                        while doacao < 0:
                            doacao = float(input(f"Quantos litros {i} você deseja doar(apenas numero maior que zero): "))
                    except ValueError:
                        print("ERRO!!! Por Favor Digite Apenas Numeros Validos")
                        doacao = "" 
                
                #atribuicao de valores as variaveis
                oleo += round(doacao, 3)
                oleo_t += round(doacao, 3)
                
                if tipo_pessoa == "j":
                    oleo_j += round(doacao, 3)
                    
                    p_juridica_l += round(doacao, 3)
                else:
                    oleo_f += round(doacao, 3)
                    
                    p_fisica_l += round(doacao, 3)
            
            else:    
                doacao =""
                while type(doacao) != float:
                    try:
                        doacao = float(input(f"Quantos kg de {i} você deseja doar: "))
                        while doacao < 0:
                            doacao = float(input(f"Quantos kg {i} você deseja doar(apenas numero maior que zero): "))
                    except ValueError:
                        print("ERRO!!! Por Favor Digite Apenas Numeros Validos")
                        doacao = ""           
                
                #atribuicao de valores as variaveis e condicionais por tipo de pessoas
                #acucar
                if i == "açúcar":
                    acucar += round(doacao, 3)
                    acucar_t += round(doacao, 3)
                    
                    if tipo_pessoa == "j":
                        acucar_j += round(doacao, 3)
                        p_juridica_kg += round(doacao, 3)

                    else:
                        acucar_f += round(doacao, 3)
                        p_fisica_kg += round(doacao, 3)

                #arroz
                elif i == "arroz":
                    arroz += round(doacao, 3)
                    arroz_t += round(doacao, 3)
                    
                    if tipo_pessoa == "j":
                        arroz_j += round(doacao, 3)
                        p_juridica_kg += round(doacao, 3)

                    else:
                        arroz_f += round(doacao, 3)                       
                        p_fisica_kg += round(doacao, 3)

                #café
                elif i == "café":
                    cafe += round(doacao, 3)
                    cafe_t += round(doacao, 3)
                    
                    if tipo_pessoa == "j":
                        cafe_j += round(doacao, 3)                        
                        p_juridica_kg += round(doacao, 3)

                    else:
                        cafe_f += round(doacao, 3)     
                        p_fisica_kg += round(doacao, 3)


                #farinha de trigo
                elif i == "farinha de trigo":
                    farinha_de_trigo += round(doacao, 3)
                    farinha_de_trigo_t += round(doacao, 3)
                    
                    if tipo_pessoa == "j":
                        farinha_de_trigo_j += round(doacao, 3)
                        p_juridica_kg += round(doacao, 3)

                    else:
                        farinha_de_trigo_f += round(doacao, 3)
                        p_fisica_kg += round(doacao, 3)

                #feijão
                elif i == "feijão":
                    feijao += round(doacao, 3)
                    feijao_t += round(doacao, 3)
                    
                    if tipo_pessoa == "j":
                        feijao_j += round(doacao, 3)
                        p_juridica_kg += round(doacao, 3)

                    else:
                        feijao_f += round(doacao, 3)
                        p_fisica_kg += round(doacao, 3)

                #sal
                elif i == "sal":
                    sal += round(doacao, 3)
                    sal_t += round(doacao, 3)
                    
                    if tipo_pessoa == "j":
                        sal_j += round(doacao, 3)
                        p_juridica_kg += round(doacao, 3)

                    else:
                        sal_f += round(doacao, 3)
                        p_fisica_kg += round(doacao, 3)


        print()
        print("-"*100)
        #pergunta se gostaria de doar um item extra
        #condicao para o while funcionar o valor de "off2" altera dependendo da situacao
        off2 = 0
        while off2 == 0:
            p_extra = input("\nGostaria de doar algo que não foi mecionado acima \nDigite [ S ] para sim e [ N ] para não: ").strip().lower()
            if p_extra != "s" and p_extra != "n":
                print("Digite  apenas [ S ] ou [ N ]")
                off2 = 0
    
            #pergunta a quantidade de novos produdos
            if p_extra == "s":
                print()
                print("-"*100)
                print()
                quantidade = input("Quantos produtos novos gostaria de adicionar: ").strip()
                while not quantidade.isdigit():
                    quantidade = input("Quantos produtos novos gostaria de adicionar (apenas números): ").strip()
                    off2 += 1
           
                #pergunta o nome e quanto de cada produto sera doado
                for y in range(1, int(quantidade) + 1):
                    outros = input(f"{y}ª O que deseja doar?: ").strip()
                    while not outros.replace(" ","").isalpha():
                        outros = input(f"{y}ª O que deseja doar?(Apenas letras): ").strip()
                    quant_outros = input(f"Quantos {outros} deseja doar?: ").strip()
                    while not quant_outros.isdigit():
                        quant_outros = input(f"Quantos {outros} deseja doar? (apenas números): ").strip()
                    quantidade = int(quantidade)
                    quant_outros = int(quant_outros)

                    print()
                    print("-"*100)
                    

                    #adicionar produto extra a lista
                    itens_extra.append(outros)
                    itens_extra_num.append(quant_outros)

                    #total de itens
                    total_extra += quant_outros
                    extra += quant_outros

                    if tipo_pessoa == "j":
                        p_juridica_ext += quant_outros

                    else:
                        p_fisica_ext += quant_outros

            elif p_extra == "n":
                off2 += 1

        #mensagem de agradecimento
        print()
        print("="*100)
        print('''\n"Aquela pessoa que ajuda os outros simplesmente porque deveria ou precisa ser feito,
e porque é a coisa certa a fazer, é sem dúvida, um super-herói de verdade."

-Stan Lee''')
        print(f"\nAgradecemos sua doação {nome}")
        enter = input("\nPress Enter para continuar")




    #montagem das cestas 
    #o while checa se as codicoes necessarioa para montar a cestas se sao verdadeiras e repete ate que seja falsa
    while acucar >= 1 and arroz >= 4 and cafe >= 2 and extrato_de_tomate >= 2 and macarrao >= 3 and pct_bolacha >= 1 and oleo >= 1 and farinha_de_trigo >= 1 and feijao >= 4 and sal >= 1:
        #tirando itens usados para nao fica infinito o loop do while
        acucar -= 1
        arroz -= 4
        cafe -= 2
        extrato_de_tomate -= 2
        macarrao -= 3
        pct_bolacha -= 1
        oleo -= 1
        farinha_de_trigo -= 1
        feijao -= 4
        sal -= 1
        #adicionando as cesta
        cesta_basica += 1
        cesta_basica_t += 1
    
    #cesta com extra
    while extra >= 1 and cesta_basica >= 1:
            extra -= 1
            cesta_basica -= 1
            cesta_basica_ex += 1           

#prints do relatorio parcial feito em formato de tabela 
    if menu == "2":
        print("="*100)
       
        print()
        print("="*13,"RELATÓRIO PARCIAL","="*13)
        
        #total de cada item recebidos
        print()
        print(" "*18,"TOTAL"," "*18)
        print("\nItens\t                         Arrecardado")
        print("="*45)
        #
        print(f"Açúcar\t{acucar_t:>33} kg")
        print("`"*45)
        #
        print(f"Arroz\t{arroz_t:>33} kg")
        print("`"*45)
        #
        print(f"Café\t{cafe_t:>33} kg")
        print("`"*45)
        #
        print(f"Extrato de tomate\t{extrato_de_tomate_t:>17} un")
        print("`"*45)
        #
        print(f"Macarrão\t{macarrao_t:>25} un")
        print("`"*45)
        #
        print(f"Bolacha\t{pct_bolacha_t:>33} pct")
        print("`"*45)
        #
        print(f"Óleo\t{oleo_t:>33} L")
        print("`"*45)
        #
        print(f"Farinha de trigo\t{farinha_de_trigo_t:>17} kg")
        print("`"*45)
        #
        print(f"Feijão\t{feijao_t:>33} kg")
        print("`"*45)
        #
        print(f"Sal\t{sal_t:>33} kg")
        print("`"*45)
        #
        print(f"Outros\t{total_extra:>33} ")
        print("`"*45)

        #total de cada item doado por pessoas f ou j
        print()
        print(" "*14,"TOTAL POR PESSOA"," "*14)
        
        print()
        print("="*18,"Física","="*18)

        print(f"Quilos\t{p_fisica_kg:>36}")
        print("`"*45)
        print(f"Litros\t{p_fisica_l:>36}")
        print("`"*45)
        print(f"Pacotes\t{p_fisica_pct:>36}")
        print("`"*45)
        print(f"Unidades\t{p_fisica_un:>28}")
        print("`"*45)
        print(f"Extras\t{p_fisica_ext:>36}")
        print("`"*45)
        #
        print("="*17,"Juridica","="*17)

        print(f"Quilos\t{p_juridica_kg:>36}")
        print("`"*45)
        print(f"Litros\t{p_juridica_l:>36}")
        print("`"*45)
        print(f"Pacotes\t{p_juridica_pct:>36}")
        print("`"*45)
        print(f"Unidades\t{p_juridica_un:>28}")
        print("`"*45)
        print(f"Extras\t{p_juridica_ext:>36}")
        print("`"*45)

        #cestas basicas

        print()
        print(" "*14,"CESTAS BÁSICAS"," "*14)
        print("\nCestas")
        print("="*45)
        print(f"C/extra\t{cesta_basica_ex:>36}")
        print("`"*45)
        print(f"S/extra\t{cesta_basica:>36}")
        print("`"*45)
        print(f"Total\t{cesta_basica_t:>36}")
        print("`"*45)
        
        #itens que sobraram
        print()
        print(" "*12,"ITENS QUE SOBRARAM"," "*12)
        print("\nItens")
        print("="*45)
        #
        print(f"Açúcar\t{acucar:>33} kg")
        print("`"*45)
        #
        print(f"Arroz\t{arroz:>33} kg")
        print("`"*45)
        #
        print(f"Café\t{cafe:>33} kg")
        print("`"*45)
        #
        print(f"Extrato de tomate\t{extrato_de_tomate:>17} un")
        print("`"*45)
        #
        print(f"Macarrão\t{macarrao:>25} un")
        print("`"*45)
        #
        print(f"Bolacha\t{pct_bolacha:>33} pct")
        print("`"*45)
        #
        print(f"Óleo\t{oleo:>33} L")
        print("`"*45)
        #
        print(f"Farinha de trigo\t{farinha_de_trigo:>17} kg")
        print("`"*45)
        #
        print(f"Feijão\t{feijao:>33} kg")
        print("`"*45)
        #
        print(f"Sal\t{sal:>33} kg")
        print("`"*45)
        #
        print(f"Outros\t{extra:>33} ")
        print("`"*45)
        
        enter = input("\nPress Enter para continuar")


        
 
    #condicao para desligar o programa
    if menu == "3":
        fechar = 0
        while fechar == 0:
            print("="*100)
            print("\n\tATENÇÃO")
            print("Todos os dados serão perdidos")
            escolha = input("\nDeseja continuar [S/N]: ").lower()
            if escolha != "s" and escolha != "n" and escolha != "criador":
                fechar = 0
             
            elif escolha == "n":
                on = 0
                fechar += 1
          
                   
            #Easter Egg (estou ciente que estes trechos não serão considerados para fins de avaliação)
            elif escolha == "criador":
                print("="*100)

                print("\nCriado por: Sival Leão de Jesus")
                print("Tutor: Thiago D'Martin Maia")
                print("""Colegas de sessão:
                    Samara Ferreira
                    Silvio Azevedo
                    Thiago Almeida
                    Vitor Augusto
                    Vitória Tanan
                    Yasmin Cordeiro """)
                print()
                fim = input("Press Enter para continuar ")
                fechar += 1
           

            
            #print final dos relatorios
            if escolha =="s":
                print("="*100)
                print()
                print("="*14,"RELATÓRIO FINAL","="*14)

                print()
                print(" "*18,"TOTAL"," "*18)
                print("\nItens\t                         Arrecardado")
                print("="*45)
                #
                print(f"Açúcar\t{acucar_t:>33} kg")
                print("`"*45)
                #
                print(f"Arroz\t{arroz_t:>33} kg")
                print("`"*45)
                #
                print(f"Café\t{cafe_t:>33} kg")
                print("`"*45)
                #
                print(f"Extrato de tomate\t{extrato_de_tomate_t:>17} un")
                print("`"*45)
                #
                print(f"Macarrão\t{macarrao_t:>25} un")
                print("`"*45)
                #
                print(f"Bolacha\t{pct_bolacha_t:>33} pct")
                print("`"*45)
                #
                print(f"Óleo\t{oleo_t:>33} L")
                print("`"*45)
                #
                print(f"Farinha de trigo\t{farinha_de_trigo_t:>17} kg")
                print("`"*45)
                #
                print(f"Feijão\t{feijao_t:>33} kg")
                print("`"*45)
                #
                print(f"Sal\t{sal_t:>33} kg")
                print("`"*45)
                #
                print(f"Outros\t{total_extra:>33} ")
                print("`"*45)


                #total de cada item doado por pessoas f ou j
                print()
                print(" "*14,"TOTAL POR PESSOA"," "*14)
                
                print()
                print("="*18,"Física","="*18)
                

                print(f"Quilos\t{p_fisica_kg:>36}")
                print("`"*45)
                print(f"Litros\t{p_fisica_l:>36}")
                print("`"*45)
                print(f"Pacotes\t{p_fisica_pct:>36}")
                print("`"*45)
                print(f"Unidades\t{p_fisica_un:>28}")
                print("`"*45)
                print(f"Extras\t{p_fisica_ext:>36}")
                print("`"*45)
                #
                print("="*17,"Juridica","="*17)
                

                print(f"Quilos\t{p_juridica_kg:>36}")
                print("`"*45)
                print(f"Litros\t{p_juridica_l:>36}")
                print("`"*45)
                print(f"Pacotes\t{p_juridica_pct:>36}")
                print("`"*45)
                print(f"Unidades\t{p_juridica_un:>28}")
                print("`"*45)
                print(f"Extras\t{p_juridica_ext:>36}")
                print("`"*45)

                #cestas basicas

                print()
                print(" "*14,"CESTAS BÁSICAS"," "*14)
                print("\nCestas")
                print("="*45)
                print(f"C/extra\t{cesta_basica_ex:>36}")
                print("`"*45)
                print(f"S/extra\t{cesta_basica:>36}")
                print("`"*45)
                print(f"Total\t{cesta_basica_t:>36}")
                print("`"*45)
                
                #itens que sobraram
                print()
                print(" "*12,"ITENS QUE SOBRARAM"," "*12)
                print("\nItens")
                print("="*45)
                #
                print(f"Açúcar\t{acucar:>33} kg")
                print("`"*45)
                #
                print(f"Arroz\t{arroz:>33} kg")
                print("`"*45)
                #
                print(f"Café\t{cafe:>33} kg")
                print("`"*45)
                #
                print(f"Extrato de tomate\t{extrato_de_tomate:>17} un")
                print("`"*45)
                #
                print(f"Macarrão\t{macarrao:>25} un")
                print("`"*45)
                #
                print(f"Bolacha\t{pct_bolacha:>33} pct")
                print("`"*45)
                #
                print(f"Óleo\t{oleo:>33} L")
                print("`"*45)
                #
                print(f"Farinha de trigo\t{farinha_de_trigo:>17} kg")
                print("`"*45)
                #
                print(f"Feijão\t{feijao:>33} kg")
                print("`"*45)
                #
                print(f"Sal\t{sal:>33} kg")
                print("`"*45)
                #
                print(f"Outros\t{extra:>33} ")
                print("`"*45)
                

                on += 1
                fechar += 1

