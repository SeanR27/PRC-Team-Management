import pandas as pd
import os

from . import globalData as gd
from .. import columns as cols

def createTable():
    colDict = cols.teams()
    df = pd.DataFrame(columns = [colDict["teamID"][1],
                                    colDict["teamName"][1]
                                    ])
    return df

def clearTable(df): gd.setMain(createTable(), "teams")

def viewTeams(): print(gd.getMain("teams"))

def addTeam(teamName):
    df = gd.getMain("teams")
    teamName = teamName.upper()

    colDict = cols.teams()
    rows = len(df)
    
    for i in range(rows):
        if df.iloc[i, colDict["teamName"][0]] == teamName:
            print("Team '" + teamName + "' found in teams list.")
            return None
        
    maxID = -1
    if not df.empty:
        maxID = int(df[colDict["teamID"][1]].max()[1:])

    df.loc[rows, colDict["teamID"][1]] = "T" + str(maxID + 1).zfill(4)
    df.loc[rows, colDict["teamName"][1]] = teamName

    print("Team '" + teamName + "' added to teams list.")

    gd.setMain(df, "teams")

def removeTeam(teamID):
    df = gd.getMain("teams")
    nrows = len(df)

    if teamID not in df[cols.teams()["teamID"][1]].values: print("Team " + str(teamID) + " not found in team list.")

    i = 0
    while i < nrows:
        if df.iloc[i, cols.teams()["teamID"][0]] == teamID:
            df.drop(df.iloc[i].name, inplace = True)
            nrows -= 1
            continue
        i += 1

    gd.setMain(df, "teams")
