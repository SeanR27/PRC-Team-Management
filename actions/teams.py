import pandas as pd
import os

from .. import config
from .. import fileManagement as fm

rootPath = config.mainPath()
dataPath = config.dataPath()
thisPath = os.path.dirname(__file__)

def main():
    df = fm.getDF_pkl(config.mainDataPath(2, 2))
    print(df)
    #fm.export(df, config.mainDataPath(1, 2), config.mainDataPath(2, 2))

def getColumnDict():
    # KeyName : [index, columnLabel]
    return {"teamID": [0, "TEAM_ID"],
            "teamName": [1, "TEAM_NAME"]
            }

def clearTable(df): return df.drop(df.index, inplace = False)

main()