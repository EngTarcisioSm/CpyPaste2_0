from Criando_tela import tela as TL
from Arquivo_configuracao import search as SH
from Arquivo_configuracao import File 
from VerificaDir import VerificaDir as VD


if SH.searchFileConfig():
    #desenvolver a logica
    print('ok')
else:
    testAcessoDir = 0
    #requisita os diretorios de trabalho e verifica se os mesmos são válidos
    while testAcessoDir == 0:
        tela = TL.Tela()
        retornoTela = tela.Start()
        testAcessoDir = VD.TestDir(retornoTela)
    File.SaveFiles(retornoTela)
