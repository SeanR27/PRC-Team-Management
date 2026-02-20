import pandas as pd
import os

from .. import config
from .. import fileManagement as fm

rootPath = config.mainPath()
dataPath = config.dataPath()
thisPath = os.path.dirname(__file__)

def main():
    print(dataPath + "data.csv")


def getColumnDict():
    """
    The Column Lable-Index dictionary for a week table.
    These tables hold information about each game for some week.
    """
    return {"courtNum": [0, "COURT"],
            "player1": [1, "P1"],
            "player2": [2, "P2"],
            "pairStrength": [3, "PAIR_STRNGTH"],
            "result": [4, "RESULT"]
            }

def createWeek(weekID):
    colDict = getColumnDict()
    newDF = pd.DataFrame(columns = [colDict["courtNum"][1],
                                    colDict["player1"][1],
                                    colDict["player2"][1],
                                    colDict["pairStrength"][1],
                                    colDict["result"][1]])
    
    pathBase = rootPath + "weeks/" + weekID + "/" + weekID
    
    fm.export(newDF, pathBase + ".csv", pathBase + ".pkl")

    

main()