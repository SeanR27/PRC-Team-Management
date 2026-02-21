import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

def main():
    df = fm.getDF_pkl(fm.mainDataPath(2, 0))
    df = clearTable(df)
    df = addPlayer(df, "Agota", "Roth")
    fm.export(df, fm.mainDataPath(1, 0), fm.mainDataPath(2, 0))

def clearTable(df): return df.drop(df.index, inplace = False)

def addPlayer(df, first, last):

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

    return df

def removePlayer(df, playerID):
    nrows = len(df)

    for i in range(nrows):
        if df.iloc[i, cols.players()["playerID"][0]] == playerID:
            df.drop(df.iloc[i].name, inplace = True)
    
    return df



main()