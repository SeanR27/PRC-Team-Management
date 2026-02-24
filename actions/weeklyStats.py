import pandas as pd
import os

from .. import columns as cols

from . import globalData as gd
from . import statsHelper as sh
from . import weeksTable as wt

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

    weeksDF = gd.getMain("weeks")
    weekCols = cols.weeks()
    existingWeeks = weeksDF[weekCols["weekID"][1]]
    if not (weekID in existingWeeks.values):
        raise Exception("This week is not in weeks.csv.\nWeek ID: " + weekID)
    
    gd.setWeeklyStats(df, weekID)

def fillWeekStats(weekID):
    """
    Fills the weekly stats table for a given week.    
    """

    df = gd.getWeeklyStats(weekID)
    playersDF = gd.getMain("players")

    # Basic Fill (playerID, weekID, assigned courts)
    colDict = cols.weeklyStats()
    playersCols = cols.players()

    for i in range(len(playersDF)):
        df.loc[i, colDict["playerID"][1]] = playersDF.iloc[i, playersCols["playerID"][0]]
        df.loc[i, colDict["weekID"][1]] = weekID
        df.loc[i, colDict["court_ass"][1]] = playersDF.iloc[i, playersCols["court_ass"][0]]

    gd.setWeeklyStats(df, weekID)

    # Other Fill
    fillWeekGameData(weekID)
    fillWeightedScore(weekID)

def fillWeekGameData(weekID):
    """
    Fills data in Weekly Stats Table which must be filled from week's game data.
    """
    df = gd.getWeeklyStats(weekID)
    gameDF = gd.getWeeklyGames(weekID)
    colDict = cols.weeklyStats()
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

    gd.setWeeklyStats(weekID)

def fillWeightedScore(weekID):
    """
    Fills the weighted score for all playerIDs in the given Weekly Stats Table.
    """
    df = gd.getWeeklyStats(weekID)
    gameDF = gd.getWeeklyGames(weekID)

    arr_p1 = gameDF[cols.weeklyGames()["player1"][1]].values
    arr_p2 = gameDF[cols.weeklyGames()["player2"][1]].values

    prevWeekID = wt.getPreviousWeek(weekID)
    prevWeek_statsDF = gd.getWeeklyStats(prevWeekID)

    if (prevWeekID != None):
        prevWeek_playerList = prevWeek_statsDF[cols.weeklyStats["playerID"][1]].values

    for i in range(len(df)):
        playerID = df.iloc[i, cols.weeklyStats()["playerID"][0]]
        prevWeekStats_playerRow = prevWeek_statsDF[prevWeek_statsDF[cols.weeklyStats["playerID"][1]] == playerID]

        if (playerID in arr_p1) or (playerID in arr_p2):
            df.iloc[i, cols.weeklyStats()["ws_after"][0]] = sh.getWeightedScoreAvg(playerID, weekID)
        else:
            if (prevWeekID == None) or (playerID not in prevWeek_playerList):
                df.iloc[i, cols.weeklyStats()["ws_after"][0]] = 0
            else:
                df.iloc[i, cols.weeklyStats()["ws_after"][0]] = prevWeekStats_playerRow.loc[cols.weeklyStats()["ws_after"][1]]

        if (prevWeekID != None) and (playerID in prevWeek_playerList):
            df.iloc[i, cols.weeklyStats()["ws_before"][0]] = prevWeekStats_playerRow.loc[cols.weeklyStats()["ws_after"][1]]
        else:
            df.iloc[i, cols.weeklyStats()["ws_before"][0]] = 0
    
    gd.setWeeklyStats(df, weekID)