import pandas as pd
import os

from .. import columns as cols

from . import globalData as gd
from . import weeklyGames as wg
from . import weeklyStats as ws
from . import teams


def createTable():
    colDict = cols.weeks()
    df = pd.DataFrame(columns = [colDict["weekID"][1],
                                    colDict["opp"][1],
                                    colDict["homeAway"][1],
                                    colDict["date"][1]])
    return df

def clearTable(): gd.setMain(createTable(), "weeks")

def viewWeeks(): print(gd.getMain("weeks"))

def addWeek(teamName, ha_bin, date):
    df = gd.getMain("weeks")
    colDict_weeks = cols.weeks()

    teams.addTeam(teamName)

    maxID = -1
    if not df.empty:
        maxID = int(df[colDict_weeks["weekID"][1]].max()[1:])

    weekID = "W" + str(maxID + 1).zfill(4)

    rows = len(df)
    df.reset_index()
    df.loc[rows, colDict_weeks["weekID"][1]] = weekID
    df.loc[rows, colDict_weeks["opp"][1]] = teamName
    df.loc[rows, colDict_weeks["homeAway"][1]] = ha_bin
    df.loc[rows, colDict_weeks["date"][1]] = date

    wg.createWeek(weekID)
    ws.createWeek(weekID)

    gd.setMain(df, "weeks")

def removeWeek(weekID):
    df = gd.getMain("weeks")
    nrows = len(df)

    if weekID not in df[cols.weeks()["weekID"][1]].values: print("Week " + str(weekID) + " not found in player list.")

    i = 0
    while i < nrows:
        if df.iloc[i, cols.players()["weekID"][0]] == weekID:
            df.drop(df.iloc[i].name, inplace = True)
            nrows -= 1
            continue
        i += 1
    
    gd.setMain(df, "weeks")

def getMaxWeekID():
    df = gd.getMain("weeks")
    print(df)
    maxDate = df[cols.weeks()["date"][1]].max()

    for i in range(len(df)):   
        if (df.iloc[i, cols.weeks()["date"][0]] == maxDate):
            return df.iloc[i, cols.weeks()["weekID"][0]]

def getWeeksSeries(weekID):
    """
    Gets the set of weeks up to a given week, inclusive.
    Returns as a Series
    """

    df = gd.getMain("weeks")
    weeksSeries = pd.Series()

    for i in range(len(df)):
        if df.iloc[i, cols.weeks()["weekID"][0]] == weekID:
            targetDate = df.iloc[i, cols.weeks()["date"][0]]

    for i in range(len(df)):
        if df.iloc[i, cols.weeks()["date"][0]] <= targetDate:
            weeksSeries.loc[len(weeksSeries)] = df.iloc[i, cols.weeks()["weekID"][0]]

    return weeksSeries

def getPreviousWeek(weekID):
    """
    Returns the Week ID of the previous week from a given week.
    """
    weeksSeries = getWeeksSeries(weekID)
    nWeeks = len(weeksSeries)

    if nWeeks == 0:
        print("Week not found: " + weekID)
        return None
    
    if nWeeks == 1:
        print("No previous weeks: " + weekID)
        return None
    
    weeksSeries.sort_values(ascending = True, inplace = True) 
    return weeksSeries.iloc[nWeeks - 2]