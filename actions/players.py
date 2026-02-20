import pandas as pd
import os

from .. import config
from .. import fileManagement as fm

rootPath = config.mainPath()
dataPath = config.dataPath()
players_dataPath = config.playerPath()
thisPath = os.path.dirname(__file__)

def main():
    playerCSV_path = players_dataPath + "players.csv"
    playerPKL_path = players_dataPath + "players.pkl"

    df = fm.getDF_pkl(playerPKL_path)
    df = clearTable(df)
    df = addPlayer(df, "Agota", "Roth")
    print(df)
    df = removePlayer(df, "P0000")
    print(df)
    #export(df, playerCSV_path, playerPKL_path)


def getColumnDict():
    # KeyName : [index, columnLabel]
    return {"playerID": [0, "PLAYER_ID"],
            "firstName": [1, "FIRST"],
            "lastName": [2, "LAST"],
            "totalGames": [3, "TOT_GAMES"],
            "positionGames": [4, "POS_GAMES"],
            "wins": [5, "WIN"],
            "losses": [6, "LOSS"],
            "ties": [7, "TIE"],
            "performance": [8, "PERF"],
            "weightedScore": [9, "WS"]
            }

def clearTable(df): return df.drop(df.index, inplace = False)

def addPlayer(df, first, last):

    first = first.capitalize()
    last = last.capitalize()

    colDict = getColumnDict()

    rows = len(df)

    maxID = -1
    if not df.empty:
        maxID = int(df[colDict["playerID"][1]].max()[1:])

    df.iloc[rows, colDict["playerID"][0]] = "P" + str(maxID + 1).zfill(4)
    df.iloc[rows, colDict["firstName"][0]] = first
    df.iloc[rows, colDict["lastName"][0]] = last

    return df

def removePlayer(df, playerID):
    nrows = len(df)

    for i in range(nrows):
        if df.iloc[i, getColumnDict()["playerID"][0]] == playerID:
            df.drop(df.iloc[i].name, inplace = True)
    
    return df



main()