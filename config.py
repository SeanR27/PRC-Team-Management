import os

rootPath = os.path.dirname(__file__).replace('\\', '/') + "/"

def mainPath(): return rootPath
def dataPath(): return rootPath + "data/"