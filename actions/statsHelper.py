import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

from . import weeksTable as wt

def getWeightedScoreAvg(df, playerID, weekID):
    """
    Gets the average weighted score for a some player up to a given week.
    Avg. Weighted Score = Sum of Weighted Scores / Number of Games Played
    """
    wsSum = getWeightedScore(df, playerID, weekID)
    nGames = getNumGames(df, playerID, weekID)

    if (nGames == 0):
        print("Player " + playerID + " has no games.")
        return 0
    
    return round((wsSum/nGames, 2))

   

def getWeightedScore(df, playerID, weekID):
    """
    Gets the summed weighted score for a player up to (and including) a specified week.
    """
    wsSum = 0
    wSeries = wt.getWeeksSeries(df, weekID)

    for i in range(len(wSeries)):
        weekID_loop = wSeries.iloc[i]
        court = None
        res = None

        try:
            weekGame = fm.getDF_pkl(fm.weekGamesPath(3, weekID_loop))
        except:
            print("There probably isn't a Week Game Table for the week " + weekID_loop)
        
        for j in range(len(weekGame)):
            p1 = weekGame.iloc[j, cols.weeklyGames()["player1"][0]]
            p2 = weekGame.iloc[j, cols.weeklyGames()["player1"][0]]
            if (p1 == playerID) or (p2 == playerID):
                court = weekGame.iloc[j, cols.weeklyGames()["result"][0]]
                res = weekGame.iloc[j, cols.weeklyGames()["result"][0]]

                if (court == None): raise Exception("No court value in game table." + "\nWeek: " + weekID_loop)
                if (res == None): raise Exception("No result value in game table." + "\nWeek: " + weekID_loop)

                wsSum += calcWeightedScore(court, res)
                
    return wsSum

def calcWeightedScore(court, res):
    added = 0
    if (res == 2): added = 0        # Win Score Add
    elif (res == 1): added = 0.25   # Tie Score Add
    elif(res == 0): added = 0.5     # Loss Score Add
    else:
        raise Exception("Invalid Result Value")

    return (court + added)

def getNumGames(df, playerID, weekID):
    """
    Gets the number of games a player has played up to (and including) the given week.
    """
    nGames = 0
    wSeries = wt.getWeeksSeries(df, weekID)

    for i in range(len(wSeries)):
        weekID_loop = wSeries.iloc[i]

        try:
            weekGame = fm.getDF_pkl(fm.weekGamesPath(3, weekID_loop))
        except:
            print("There probably isn't a Week Game Table for the week " + weekID_loop)
        
        for j in range(len(weekGame)):
            p1 = weekGame.iloc[j, cols.weeklyGames()["player1"][0]]
            p2 = weekGame.iloc[j, cols.weeklyGames()["player1"][0]]
            if (p1 == playerID) or (p2 == playerID):
                nGames += 1
                
    return nGames