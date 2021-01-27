import os

def TestDir(dictDir):
    test = 1
    for i in dictDir:
        try:
            print(i)
            x = os.listdir(i)
            print(x)
        except:
            test = 0
            break
    return test
