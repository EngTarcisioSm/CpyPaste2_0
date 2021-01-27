import os

def searchFileConfig():
    listFile = os.listdir(os.getcwd())

    if "config.txt" in listFile:
        return 1
    else:
        return 0
