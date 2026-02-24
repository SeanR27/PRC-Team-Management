import pandas as pd
import os

from .. import fileManagement as fm
from ..  import columns as cols

from . import globalData as gd

def createWeek(weekID):
    colDict = cols.weeklyGames()
    df = pd.DataFrame(columns = [colDict["weekID"][1],
                                    colDict["courtNum"][1],
                                    colDict["player1"][1],
                                    colDict["player2"][1],
                                    colDict["pairStrength"][1],
                                    colDict["result"][1]])
    
    weeksDF = gd.getMain("weeks")
    weekCols = cols.weeks()
    existingWeeks = weeksDF[weekCols["weekID"][1]]
    if not (weekID in existingWeeks.values):
        raise Exception("This week is not in weeks.csv.\nWeek ID: " + weekID)

    for i in range(4):
        row = len(df)
        df.loc[row, colDict["weekID"][1]] = weekID
        df.loc[row, colDict["courtNum"][1]] = i + 1

    gd.setWeeklyGames(df, weekID)
    
def addGame(weekID, courtNum, p1_id, p2_id):
    df = gd.getWeeklyGames(weekID)
    colDict = cols.weeklyGames()

    for i in range(len(df)):
        if df.iloc[i, colDict["courtNum"][0]] == courtNum:
            df.iloc[i, colDict["player1"][0]] = p1_id
            df.iloc[i, colDict["player2"][0]] = p2_id
    
    gd.setWeeklyGames(df, weekID)

def addResult():
    None