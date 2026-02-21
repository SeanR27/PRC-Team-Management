import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

def main():
    weekID = "W0004"
    createWeek(weekID)

def createWeek(weekID):
    colDict = cols.weeklyStats()
    df = pd.DataFrame(columns = [colDict["weekID"][1],
                                    colDict["playerID"][1],
                                    colDict["court_ass"][1],
                                    colDict["court_played"][1],
                                    colDict["result"][1],
                                    colDict["ws_before"][1],
                                    colDict["ws_after"][1],
                                    colDict["weekAvab"][1]])

    weekDF = fm.getDF_pkl(fm.mainDataPath(2, 1))
    weekCols = cols.weeks()

    existingWeeks = weekDF[weekCols["weekID"][1]]

    if not (weekID in existingWeeks.values):
        raise Exception("This week is not in weeks.csv.\nWeek ID: " + weekID)
    
    df = fillWeek(df, weekID)

    os.makedirs(fm.weekStatsPath(1, weekID), exist_ok = True)
    fm.export(df, fm.weekStatsPath(2, weekID), fm.weekStatsPath(3, weekID))

    return df

def fillWeek(df, weekID):
    if (not df.empty): raise Exception("Cannot fill this Week Stats file; file must be empty to fill.")

    # Basic Fill (playerID, weekID, assigned courts)
    colDict = cols.weeklyStats()
    playersDF = fm.getDF_pkl(fm.mainDataPath(2, 0))
    playersCols = cols.players()

    for i in range(len(playersDF)):
        df.loc[i, colDict["playerID"][1]] = playersDF.iloc[i, playersCols["playerID"][0]]
        df.loc[i, colDict["weekID"][1]] = weekID
        df.loc[i, colDict["court_ass"][1]] = playersDF.iloc[i, playersCols["court_ass"][0]]

    df = fillWeekGameData(df, weekID)
    df = fillWeightedScore(df, weekID)

    return df

def fillWeekGameData(df, weekID):
    """
    Fills data in Weekly Stats Table which must be filled from week's game data.
    """
    if (not os.path.isdir(fm.weekGamesPath(1, weekID))):
        raise Exception(weekID + " game table direcotry does not exist.\nAttempted path: " + fm.weekGamesPath(1, weekID))
    
    if (not os.path.isfile(fm.weekGamesPath(3, weekID))):
        raise Exception(weekID + " game table file does not exist.\nAttempted path: " + fm.weekGamesPath(3, weekID))
    
    colDict = cols.weeklyStats()
    gameDF = fm.getDF_pkl(fm.weekGamesPath(3, weekID))
    colDict_game = cols.weeklyGames()

    for i in range(len(gameDF)):
        court = gameDF.iloc[i, colDict_game["court"][0]]
        p1_ID = gameDF.iloc[i, colDict_game["player1"][0]]
        p2_ID = gameDF.iloc[i, colDict_game["player2"][0]]
        result = gameDF.iloc[i, colDict_game["result"][0]]

        for j in range(len(df)):
            loopPlayerID = df.iloc[j, colDict["playerID"][0]]
            if (loopPlayerID == p1_ID) or (loopPlayerID == p2_ID):
                df.iloc[j, colDict["court_played"][0]] = court
                df.iloc[j, colDict["result"][0]] = result
        
    return df

def fillWeightedScore(df, weekID):
    None

def getWeightedScoreAvg(df, weekID):
    None

def getWeightedScore(df, playerID, weekID):
    """
    Gets the weighted score for a player up to & including the specified week.
    """
    None

def getNumGames(df, playerID, weekID):
    None



main()