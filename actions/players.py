import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

def main():
    df = createTable()
    df = fillInitial(df)
    fm.export(df, fm.mainDataPath(1, 0), fm.mainDataPath(2, 0))

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

def clearTable(df): return df.drop(df.index, inplace = False)

def addPlayer(df, first, last, court):

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

    return df

def removePlayer(df, playerID):
    nrows = len(df)

    for i in range(nrows):
        if df.iloc[i, cols.players()["playerID"][0]] == playerID:
            df.drop(df.iloc[i].name, inplace = True)
    
    return df

def fillInitial(df):
    dfInit = fm.getDF_pkl(fm.mainDataPath(2, 3))
    nInit = len(dfInit)

    df = clearTable(df)

    for i in range(nInit):
        first = dfInit.iloc[i, cols.initialData()["firstName"][0]]
        last = dfInit.iloc[i, cols.initialData()["lastName"][0]]
        court = dfInit.iloc[i, cols.initialData()["court_ass"][0]]
        df = addPlayer(df, first, last, court)

    return df

main()