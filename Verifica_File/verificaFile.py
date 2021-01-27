
def testFile(file_):
    openFile = open(file_, 'r')
    dados = openFile.readlines()
    dictDados ={}
    for i in range(len(dados)):
        dictDados[i] = dados[i].replace('\n','')
    return dictDados 


'''
print(testFile('config.txt'))
'''