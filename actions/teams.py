import pandas as pd
import os

from .. import config
from .. import fileManagement as fm

rootPath = config.mainPath()
dataPath = config.dataPath()
teams_dataPath = config.teamsPath()
thisPath = os.path.dirname(__file__)

def main():
    teamsCSV_path = teams_dataPath + "teams.csv"
    teamsPKL_path = teams_dataPath + "teams.pkl"

    df = fm.getDF_pkl(teamsPKL_path)
    print(df)
    #fm.export(df, playerCSV_path, playerPKL_path)

def getColumnDict():
    # KeyName : [index, columnLabel]
    return {"teamID": [0, "TEAM_ID"],
            "teamName": [1, "TEAM_NAME"]
            }

def clearTable(df): return df.drop(df.index, inplace = False)

main()