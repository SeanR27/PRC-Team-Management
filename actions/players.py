import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

from . import globalData as gd

def main():
    None

def createTable():
    colDict = cols.players()
    df = pd.DataFrame(columns = [colDict["playerID"][1],
                                    colDict["firstName"][1],
                                    colDict["lastName"][1],
                                    colDict["court_ass"][1],
                                    colDict["totalGames"][1],
                                    colDict["positionGames"][1],
                                    colDict["wins"][1],
                                    colDict["losses"][1],
                                    colDict["ties"][1],
                                    colDict["performance"][1],
                                    colDict["weightedScore"][1]
                                    ])
    return df

def clearTable(): gd.setMain(createTable(), "players")

def viewPlayers(): print(gd.getMain("players"))

def addPlayer(first, last, court):
    """
    Adds a player to the player DataFrame.
    """
    df = gd.getMain("players")

    first = first.capitalize()
    last = last.capitalize()

    colDict = cols.players()
    rows = len(df)

    maxID = -1
    if not df.empty:
        maxID = int(df[colDict["playerID"][1]].max()[1:])

    df.loc[rows, colDict["playerID"][1]] = "P" + str(maxID + 1).zfill(4)
    df.loc[rows, colDict["firstName"][1]] = first
    df.loc[rows, colDict["lastName"][1]] = last
    df.loc[rows, colDict["court_ass"][1]] = court

    gd.setMain(df, "players")

def removePlayer(playerID):
    df = gd.getMain("players")
    nrows = len(df)

    if playerID not in df[cols.players()["playerID"][1]].values: print("Player " + str(playerID) + " not found in player list.")

    i = 0
    while i < nrows:
        if df.iloc[i, cols.players()["playerID"][0]] == playerID:
            df.drop(df.iloc[i].name, inplace = True)
            nrows -= 1
            continue
        i += 1

    gd.setMain(df, "players")

def fillInitial():
    dfInit = fm.getDF_pkl(fm.mainDataPath(2, 3))
    nInit = len(dfInit)

    df = createTable()

    for i in range(nInit):
        first = dfInit.iloc[i, cols.initialData()["firstName"][0]]
        last = dfInit.iloc[i, cols.initialData()["lastName"][0]]
        court = dfInit.iloc[i, cols.initialData()["court_ass"][0]]
        df = addPlayer(df, first, last, court)

    gd.setMain(df, "players")

main()