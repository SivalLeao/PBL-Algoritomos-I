"""/*******************************************************************
Autor: Sival Leão de Jesus
Componente Curricular: MI - Algoritmos I
Concluído em: 03/07/2022
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
**********************************************************************/"""
#import os usado como principal funcionalidade a busca de arquivos presente no computador
#codigo fonte: https://github.com/python/cpython/tree/3.10/Lib/os.py
import os


#funcoes

def checar(diretorio):
    if os.path.isdir(diretorio): #verifica se o diretorio passado pelo usuario existe
        return True
    else:
        return False

def arquivos_txt(caminho, dic, endereco_py, arquivo_caminho, dic_end_ter):
    for raiz, diretorios, arquivos in os.walk(caminho):# raiz = pasta principal,
        #diretorios= pasta secudaria, arquivos = todos os arquivos presente no diretorio e suas subpastas
        if raiz == caminho: #condicao para evitar pegar arquivo de subpastas
            for arquivo in arquivos: #percore todos arquivos 
                caminho_completo = os.path.join(raiz, arquivo) # mostra endereco completo do arquivo.
                nome_arquivo, extencao = os.path.splitext(arquivo)

                
                #buscando somente arquivo *.txt do diretorio com exceçao dos arquivos "save" ultilizado para nao perder os dados (Obs.: os arquivos so poderam ser apagado os 3
                # juntos para o funcionamento do codigo e nao poderar existir outro arquivo com estes nome "save.txt", "save2.txt" e "save3.txt")
                if extencao == ".txt" and arquivo != "save.txt" and extencao != None and arquivo != "save2.txt" and arquivo != "save3.txt":
                    #verificando se o arquivo ja foi indexado
                    if arquivo_caminho.get(arquivo) == None:
                        #se nao, registra o diretorio para na proxima vez souber se foi indexado
                        arquivo_caminho[arquivo] = raiz
                        
                        #"save2". Salvando o nome do arquivo e sua pasta. (Obs.: nao podera existir dois arquivos com o mesmo nome mesmo que em outra pasta)
                        with open(rf"{endereco_py}\save2.txt", "w",encoding="utf-8") as save2:
                            save2.write(str(arquivo_caminho))

                        #lendo os arquivos do diretorio
                        with open(caminho_completo, "r", encoding="utf-8") as ler: 
                            texto = ler.read()
                        list_texto = texto.split()

                        #contando palavras dos aquivos e colocando em um dicionario
                        termo_quant = {}
                        termo_list = []
                        for palavra in list_texto:
                            if palavra not in termo_quant.keys():
                                termo_quant[palavra] = 1
                            else:
                                termo_quant[palavra] += 1
                            if palavra not in termo_list:
                                termo_list.append(palavra)
                            
                        dic_end_ter[caminho_completo] = termo_list
                        termo_list = []
                        
                        
                        for palavra in termo_quant:
                            if palavra not in dic.keys():
                                dic[palavra] = {caminho_completo: termo_quant[palavra]}
                            else:
                                dic[palavra][caminho_completo] = termo_quant[palavra]

                    else:# se o endereco fornecido ja estiver indexado
                        Rdiretorio = caminho #passo o endereco a outra variavel
                        
                        a = dic_end_ter 
                        remover(dicionario_of,Rdiretorio,arquivo_caminho,a) #chamo a funcao remover, para que todos os dados do diretorio seja apagado do indice
                        arquivos_txt(caminho, dicionario_of, endereco_py, arquivo_caminho,a)#chamo a propria funcao de indexacao para inserir novamente os dado so que atualizados


    #"save3". Responsavel por salvar os termos de cada documento
    with open(rf"{endereco_py}\save3.txt", "w",encoding="utf-8") as save3:
        save3.write(str(dic_end_ter))
    #"save". Responsavel por salvar os indices 
    with open(rf"{endereco_py}\save.txt", "w",encoding="utf-8") as save:
        save.write(str(dic))           
    return dic

def adicionar_save(dic, endereco_py):
    #funcao usada para criar e abrir os arquivos txt para funcionamento do software, assim que o programa inicia
    #verificando se o arquivo existe
    if os.path.isfile(rf"{endereco_py}\save.txt"):
        #se existir, abre o arquivo
        with open(rf"{endereco_py}\save.txt", "r",encoding="utf-8") as abrir:
            dic = abrir.read()
            dic = eval(dic)
        return dic
        
    else:
        #se nao existir, cria um arquivo
        with open(rf"{endereco_py}\save.txt", "w",encoding="utf-8") as save:
            save.write(str(dic))

def adicionar_save2(dic2, endereco_py):
    #funcao usada para criar e abrir os arquivos txt para funcionamento do software, assim que o programa inicia
    #verificando se o arquivo existe
    if os.path.isfile(rf"{endereco_py}\save2.txt"):
        #se existir, abre o arquivo
        with open(rf"{endereco_py}\save2.txt", "r",encoding="utf-8") as abrir:
            dic2 = abrir.read()
            dic2 = eval(dic2)
        return dic2    
    else:
        #se nao existir, cria um arquivo
        with open(rf"{endereco_py}\save2.txt", "w",encoding="utf-8") as save2:
            save2.write(str(dic2))

def adicionar_save3(dic3, endereco_py):
    #funcao usada para criar e abrir os arquivos txt para funcionamento do software, assim que o programa inicia
    #verificando se o arquivo existe
    if os.path.isfile(rf"{endereco_py}\save3.txt"):
        #se existir, abre o arquivo
        with open(rf"{endereco_py}\save3.txt", "r",encoding="utf-8") as abrir:
            dic3 = abrir.read()
            dic3 = eval(dic3)
        return dic3    
    else:
        #se nao existir, cria um arquivo
        with open(rf"{endereco_py}\save3.txt", "w",encoding="utf-8") as save2:
            save2.write(str(dic3))

def buscar(lista, dic, termo):
    #organizar em decrescente (Obs.: nao esta funcionando)
    #metodo selection sort
    #https://youtu.be/ZT_dT8yn48s
    tamanho = len(lista)
    for i in range(1, tamanho):
        chave = dic[termo][lista[i]]
        aux = lista[i]
        j = i - 1
        while j >= 0 and dic[termo][lista[j]] < chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = aux
        
    
    #mostra resultado da busca
    nome = []
    cami = []
    num = []
    for palavra in dic:
        palavr = palavra
        if termo in palavra:
            for caminho_completo in dic[palavra]: # caminho do diretorio 
                desfragmentar = caminho_completo.split("\\")
                a = len(desfragmentar) - 1
                nome.append(desfragmentar[a])
    
    b = str(lista).replace("[","").replace("]", "").replace("{","").replace("}", "").replace("","").replace(",", "").replace("'","").replace(",", "")
    #print(b)
    c = b.split()
    for i in range(len(c)):
        if i%2 == 0:
           cami.append(c[i])
        else:
            num.append(c[i])

    for k in range(len(cami)):
        print("-"*100)
        print(f"NOME: {nome[k]} \nENDEREÇO DO ARQUIVO: {cami[k]} \nQUANTIDADE DE '{termo}' PRESENTE: {num[k]}\n")

def verificar_termo(dic,termo):
    #verifica se o termo existe em algum documento
    tem = ""
    for i in dic:
        if termo in dic[i]:
            tem = "sim"
    if tem == "sim":
        return True
    else:
        False

def remover(dic,Remov,arquivo_caminho,dic_exc):
   
    for raiz, diretorios, arquivos in os.walk(Remov):# raiz = pasta principal,
        #diretorios= pasta secudaria, arquivos=arquvivos
        if raiz == Remov:
            for arquivo in arquivos: #percore todos arquivos 
                caminho_completo = os.path.join(raiz, arquivo) # mostra 
                #endereco(raiz) e arquivo.
                nome_arquivo, extencao = os.path.splitext(arquivo)
                if  extencao == ".txt" and arquivo != "save.txt" and extencao != None and arquivo != "save2.txt" and arquivo != "save3.txt":
                    if arquivo_caminho.get(arquivo) != None: #verifica se ja foi indexado

                        #bloco responsavel por excluir
                        for i in dic_exc[caminho_completo]:
                            dic[i].pop(caminho_completo)
                            if dic[i] == {}:
                                dic.pop(i)
                        arquivo_caminho.pop(arquivo)
                        dic_exc.pop(caminho_completo)
                        
                        #atualizar todos os arquivos salvo
                        with open(rf"{endereco_py}\save.txt", "w",encoding="utf-8") as save:
                            save.write(str(dic))
                        with open(rf"{endereco_py}\save2.txt", "w",encoding="utf-8") as save2:
                            save2.write(str(arquivo_caminho))
                        with open(rf"{endereco_py}\save3.txt", "w",encoding="utf-8") as save3:
                            save3.write(str(dic_exc))  
                    
                    else:
                        print("Caminho não indexado")

def mostra(arquivo_caminho):
    #mostra todos arquivos indexado
    nome = []
    cami = []
    for palavra in arquivo_caminho:
        nome.append(palavra)
        camin = arquivo_caminho[palavra]
        cami.append(camin)
    for i in range(len(nome)):
        print("-"*100)
        print(f"NOME DO ARQUIVO: {nome[i]}\nPASTA DO ARQUIVO: {cami[i]}\n")


#------------------------------------------------------------programa principal-------------------------------------------#

#buscar endereco onde o codigo esta localizado
endereco_py = os.getcwd()
#dicionario save
dicionario_of = {}
#dicionario caminho endereco
arquivo_caminho = {}
#dicionario com endereco completo do arquivo e seus termos
dic_end_ter = {}
#
lista = []


#entrada
entrada = input("digite um comando: ").lower()
#atualizando dicionario
if adicionar_save(dicionario_of,endereco_py) != None:
    dicionario_of = adicionar_save(dicionario_of,endereco_py)
if adicionar_save2(arquivo_caminho,endereco_py) != None:
    arquivo_caminho = adicionar_save2(arquivo_caminho,endereco_py)
if adicionar_save3(dic_end_ter,endereco_py) != None:
    dic_end_ter = adicionar_save3(dic_end_ter,endereco_py)


#codicoes
#adicionar diretorio para indexar ou atualizar
if entrada == "-d":
    caminho = input("isira o caminho: ")
    if checar(caminho) == True:
        dicionario_of = arquivos_txt(caminho, dicionario_of, endereco_py, arquivo_caminho,dic_end_ter)
        adicionar_save(dicionario_of,endereco_py)
        

#busca ("Obs.: busca so por termo")
elif entrada == "-b":
    termo = input("digite o termo: ")
    if verificar_termo(dic_end_ter,termo) == True:
        lista = list([dicionario_of[termo]])
        buscar(lista, dicionario_of, termo)
    else:
        print("Termo nao encontrado")

#remocao (Obs.: so poderar remover o diretorio)
elif entrada == "-r":
    Rdiretorio = input("digite o caminho do arquivo a ser exluido: ")
    remover(dicionario_of,Rdiretorio,arquivo_caminho,dic_end_ter)

#mostrar os arquivos indexados
elif entrada == "-m":
    mostra(arquivo_caminho)

else:
    print("=-"*50)
    print("COMANDOS DO SOFTWARE".center(100))
    print("=-"*50)
    print()
    print("FUNÇÕES")
    print("-d = adicionar diretorio ou atualizar\n-b = buscar arquivo por termo\n-r = remover diretorio\n-m = mostrar arquivos indexado")
    print("-"*100) 
