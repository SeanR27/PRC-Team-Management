import pandas as pd
import os

from .. import fileManagement as fm
from ..  import columns as cols

def main():
    weekID = "W0003"
    createWeek(weekID)
    df = fm.getDF_pkl(fm.weekGamesPath(3, weekID))
    addGame(df, 4, "P0005", "P0008")
    fm.export(df, fm.weekGamesPath(2, weekID), fm.weekGamesPath(3, weekID))

def createWeek(weekID):
    colDict = cols.weeklyGames()
    df = pd.DataFrame(columns = [colDict["weekID"][1],
                                    colDict["courtNum"][1],
                                    colDict["player1"][1],
                                    colDict["player2"][1],
                                    colDict["pairStrength"][1],
                                    colDict["result"][1]])
    
    for i in range(4):
        df.loc[len(df), colDict["weekID"][1]] = weekID
        df.loc[len(df), colDict["courtNum"][1]] = i + 1
    
    os.makedirs(fm.weekGamesPath(1, weekID), exist_ok = True)
    fm.export(df, fm.weekGamesPath(2, weekID), fm.weekGamesPath(3, weekID))

def addGame(df, courtNum, p1_id, p2_id):
    colDict = cols.weeklyGames()

    for i in range(len(df)):
        if df.iloc[i, colDict["courtNum"][0]] == courtNum:
            df.iloc[i, colDict["player1"][0]] = p1_id
            df.iloc[i, colDict["player2"][0]] = p2_id

def addResult():
    None

main()