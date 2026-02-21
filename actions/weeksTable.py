import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols
import weeklyGames as wg
import weeklyStats as ws

def main():
    df = fm.getDF_pkl(fm.mainDataPath(2, 1))
    df = clearTable(df)
    
    fm.export(df, fm.mainDataPath(1, 1), fm.mainDataPath(2, 1))

def createTable():
    colDict = cols.weeks()
    df = pd.DataFrame(columns = [colDict["weekID"][1],
                                    colDict["OppID"][1],
                                    colDict["homeAway"][1],
                                    colDict["date"][1],
                                    colDict["positionGames"][1]])
    return df

def clearTable(df): return df.drop(df.index, inplace = False)

def addWeek(df, teamID, ha_bin, date):
    colDict_weeks = cols.weeks()

    maxID = 0
    if not df.empty:
        maxID = int(df[colDict_weeks["weekID"][1]].max()[1:])

    rows = len(df)

    weekID = "W" + str(maxID + 1).zfill(4)

    df.reset_index()
    df.loc[rows, colDict_weeks["weekID"][1]] = weekID
    df.loc[rows, colDict_weeks["OppID"][1]] = teamID
    df.loc[rows, colDict_weeks["homeAway"][1]] = ha_bin
    df.loc[rows, colDict_weeks["date"][1]] = str(date)

    wg.createWeek(weekID)
    ws.createWeek(weekID)

    return df

def removeWeek(df, weekID):
    nrows = len(df)

    for i in range(nrows):
        if df.iloc[i, cols.weeks()["weekID"][0]] == weekID:
            df.drop(df.iloc[i].name, inplace = True)
    
    return df

def getWeek():
    None

main()