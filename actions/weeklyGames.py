import pandas as pd
import os

from .. import config
from .. import fileManagement as fm

rootPath = config.mainPath()
dataPath = config.dataPath()
thisPath = os.path.dirname(__file__)

def main():
    weekID = "W0003"
    createWeek(weekID)
    df = fm.getDF_pkl(config.weekGamesPath(3, weekID))
    addGame(df, 4, "P0005", "P0008")
    fm.export(df, config.weekGamesPath(2, weekID), config.weekGamesPath(3, weekID))


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
    df = pd.DataFrame(columns = [colDict["courtNum"][1],
                                    colDict["player1"][1],
                                    colDict["player2"][1],
                                    colDict["pairStrength"][1],
                                    colDict["result"][1]])
    
    for i in range(4):
        df.loc[len(df), colDict["courtNum"][1]] = i + 1
    
    os.makedirs(config.weekGamesPath(1, weekID), exist_ok = True)
    fm.export(df, config.weekGamesPath(2, weekID), config.weekGamesPath(3, weekID))

def addGame(df, courtNum, p1_id, p2_id):
    colDict = getColumnDict()
    nrows = len(df)

    for i in range(nrows):
        if df.iloc[i, colDict["courtNum"][0]] == courtNum:
            df.iloc[i, colDict["player1"][0]] = p1_id
            df.iloc[i, colDict["player2"][0]] = p2_id

def addResult():
    None

main()