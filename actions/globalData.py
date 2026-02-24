import pandas as pd
import os

from . import players
from . import weeksTable
from . import teams
from . import weeklyGames as wg
from . import weeklyStats as ws

from .. import fileManagement as fm
from .. import columns as cols

mainDataNames = ["players", "weeks", "teams"]

mainData = {}
weeklyGames = {}
weeklyStats = {}

# Data Loading
# ----------------------------------
def loadSequence():
    loadMainData()
    loadWeeklyGames()
    loadWeeklyStats()

def loadMainData():
    ind = 0
    for i in mainDataNames:
        try:
            mainData[mainDataNames[ind]] = fm.getDF_pkl(fm.mainDataPath(2, i))
        except:
            print("File for " + mainDataNames[ind] + " doesn't exist.")
            print("Creating the " + mainDataNames[ind] + " files.")

            if (i == "players"): df = players.createTable()
            elif (i == "weeks"): df = weeksTable.createTable()
            elif (i == "teams"): df = teams.createTable()

            if df != None: fm.export(df, fm.mainDataPath(1, i), fm.mainDataPath(2, i))

        ind += 1

def loadWeeklyGames():
    weeksID_Arr = mainData["weeks"][cols.weeks()["weekID"][1]].values

    for weekID in weeksID_Arr:
        if os.path.isfile(fm.weekGamesPath(3, weekID)):
            weeklyGames[weekID] = fm.getDF_pkl(fm.weekGamesPath(3, weekID))
        else:
            raise Exception("There is supposed to be a Week's Games file for Week ID " + weekID)
            
def loadWeeklyStats():
    weeksID_Arr = mainData["weeks"][cols.weeks()["weekID"][1]].values

    for weekID in weeksID_Arr:
        if os.path.isfile(fm.weekStatsPath(3, weekID)):
            weeklyStats[weekID] = fm.getDF_pkl(fm.weekStatsPath(3, weekID))
        else:
            raise Exception("There is supposed to be a Week's Player Stats file for Week ID " + weekID)


# Data Accessors & Mutators
# ----------------------------------
def missingKeyError(key, dictName):
    raise Exception("\nThe key '" + str(key) + "' is not in the dictionary '" + dictName + "'." +
                    "\nIf it should be, try loading data into program with globalData.loadSequence() at script start.")
def getMain(key):
    if not (key in mainData):
        missingKeyError(key, "mainData")
        raise Exception()
    else: return mainData[key]

def setMain(df, key):
    if not (key in mainData):
        missingKeyError(key, "mainData")
    else: mainData[key] = df

def getWeeklyGames(weekID):
    if not (weekID in weeklyGames):
        missingKeyError(weekID, "weeklyGames")
    else: return weeklyGames[weekID]

def setWeeklyGames(df, weekID):
    if not (weekID in weeklyGames):
        print("Week " + weekID + " is not in 'weeklyGames' dictionary.\nAdding entry to dictionary.")
    weeklyGames[weekID] = df

def getWeeklyStats(weekID):
    if not (weekID in weeklyStats):
        missingKeyError(weekID, "weeklyStats")
    else: return weeklyGames[weekID]

def setWeeklyStats(df, weekID):
    if not (weekID in weeklyStats):
        print("Week " + weekID + " is not in 'weeklyStats' dictionary.\nAdding entry to dictionary.")
    weeklyStats[weekID] = df

# Data On Drive Update
# ----------------------------------
def updateMainData(key):
    df = getMain(key)
    if not (key in mainDataNames):
        raise Exception("The key '" + str(key) + "' is not an expected main data name.")
    else: fm.export(df, fm.mainDataPath(1, key), fm.mainDataPath(2, key))

def updateWeeklyGames(weekID):
    df = getWeeklyGames(weekID)
    if not (weekID in weeklyGames):
        raise Exception("The key '" + str(weekID) + "' is not in the dictionary 'weeklyGames'.")
    
    if not os.path.isdir(fm.weekGamesPath(1, weekID)): os.makedirs(fm.weekGamesPath(1, weekID), exist_ok = True)
    fm.export(df, fm.weekGamesPath(2, weekID), fm.weekGamesPath(3, weekID))
            
def updateWeeklyStats(weekID):
    df = getWeeklyStats(weekID)
    if not (weekID in weeklyStats):
        raise Exception("The key '" + str(weekID) + "' is not in the dictionary 'weeklyStats'.")
    
    if not os.path.isdir(fm.weekStatsPath(1, weekID)): os.makedirs(fm.weekStatsPath(1, weekID), exist_ok = True)
    fm.export(df, fm.weekStatsPath(2, weekID), fm.weekStatsPath(3, weekID))

def updateWeeklyGames_all():
    allWeeks = weeksTable.getWeeksSeries(weeksTable.getMaxWeekID()).values
    for weekID in allWeeks:
        updateWeeklyGames(weekID)


def updateWeeklyStats_all():
    allWeeks = weeksTable.getWeeksSeries(weeksTable.getMaxWeekID()).values
    for weekID in allWeeks:
        updateWeeklyStats(weekID)