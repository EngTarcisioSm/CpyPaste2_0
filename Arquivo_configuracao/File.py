
def SaveFiles(dictDir):
    x = open('config.txt', 'w')
    for i in dictDir:
        x.write(i +'\n')
    x.close()