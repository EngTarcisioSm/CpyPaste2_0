from Criando_tela import tela as TL
from Arquivo_configuracao import search as SH
from Arquivo_configuracao import File 
from Verifica_File import verificaFile as VF
from VerificaDir import VerificaDir as VD

###############################################################################
def carregaTea1():
    testAcessoDir = 0
    while testAcessoDir == 0:
        tela = TL.Tela()
        retornoTela = tela.Start()
        testAcessoDir = VD.TestDir(retornoTela)
    File.SaveFiles(retornoTela)    

###############################################################################

def step1():
    if SH.searchFileConfig():
        #desenvolver a logica
        dictDir = VF.testFile('config.txt')
        print(dictDir)
        if VD.TestDir(dictDir) == 0:
            carregaTea1()
    else:
        #requisita os diretorios de trabalho e verifica se os mesmos são válidos
        carregaTea1()

###############################################################################

step1()