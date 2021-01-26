import os

def TestDir(dictDir):
    test = 1
    for i in dictDir:
        try:
            os.listdir(dictDir[i])
        except:
            test = 0
            break
    return test