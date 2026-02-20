import pandas as pd
import os

from .. import config
from .. import fileManagement as fm
from .. import weeklyGames as wg

rootPath = config.mainPath()
dataPath = config.dataPath()
weeks_dataPath = config.weeksPath()
thisPath = os.path.dirname(__file__)

def main():
    weeksCSV_path = dataPath + "weeks.csv"
    weeksPKL_path = dataPath + "weeks.pkl"

    df = fm.getDF_pkl(weeksPKL_path)
    df = clearTable(df)
    
    fm.export(df, weeksCSV_path, weeksPKL_path)


def getColumnDict():
    """
    The Column Lable-Index dictionary for the weeks.csv table.
    This table holds each week ID.
    """
    # KeyName : [index, columnLabel]
    return {"weekID": [0, "WEEK_ID"],
            "OppID": [1, "OPP_TEAM_ID"],
            "date": [2, "DATE"]
            }

def clearTable(df):

    return df.drop(df.index, inplace = False)

def addWeek(df, teamID, date):
    colDict_weeks = getColumnDict()
    colDict_weekly = wg.getColumnDict()

    maxID = -1
    if not df.empty:
        maxID = int(df[colDict_weeks["weekID"][1]].max()[1:])

    rows = len(df)

    weekID = "W" + str(maxID + 1).zfill(4)

    df.reset_index()
    df.loc[rows, colDict_weeks["weekID"][1]] = weekID
    df.loc[rows, colDict_weeks["OppID"][1]] = teamID
    df.loc[rows, colDict_weeks["date"][1]] = str(date)

    wg.createWeek(weekID)

    return df

def removeWeek(df, weekID):
    nrows = len(df)

    for i in range(nrows):
        if df.iloc[i, getColumnDict()["weekID"][0]] == weekID:
            df.drop(df.iloc[i].name, inplace = True)
    
    return df

def getWeek():
    None

main()