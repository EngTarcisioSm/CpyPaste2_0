from Criando_tela import tela as TL
from Arquivo_configuracao import search as SH
from Arquivo_configuracao import File 
from Verifica_File import verificaFile as VF
from VerificaDir import VerificaDir as VD

import shutil as sh

###############################################################################
def carregaTela1():
    testAcessoDir = 0
    while testAcessoDir == 0:
        tela = TL.Tela()
        retornoTela = tela.Start()
        retornoTelaArray = []
        for i in retornoTela:
            retornoTelaArray.append(retornoTela[i])
        testAcessoDir = VD.TestDir(retornoTelaArray)
    File.SaveFiles(retornoTelaArray)    

###############################################################################

def step1():
    if SH.searchFileConfig():
        #desenvolver a logica
        dictDir = VF.testFile('config.txt')
        print(dictDir)
        if VD.TestDir(dictDir) == 1:
            carregaTela1()
    else:
        #requisita os diretorios de trabalho e verifica se os mesmos são válidos
        carregaTela1()

###############################################################################

#copiar diretório da origem para o destino
def copyDirOD():
    dictDir = VF.testFile('config.txt')
    #verificar se o diretório de origem esta disponivel 
    dictDirArray = []
    for i in dictDir:
        dictDirArray.append(dictDir[i])
    while 1:
        answer = VD.TestDir([dictDirArray[0]])
        if answer == 1:
            break
    #copia diretorio de origem para destino 
    sh.copytree(dictDir[0], dictDir[1])

###############################################################################
step1()
copyDirOD()

