import pandas as pd

from . import players
from . import weeksTable
from . import teams
from . import weeklyGames as wg
from . import weeklyStats as ws

from .. import fileManagement as fm

mainDataNames = ["players", "weeks", "teams"]
mainData = {}

weeklyGames = None      # To be a dictionary. Keys are weekID; values are the DFs
weeklyStats = None      # To be a dictionary. Keys are weekID; values are the DFs

def loadSequence():
    loadMainData()
    loadWeeklyGames()
    loadWeeklyStats()
    print(mainData)

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

            fm.export(df, fm.mainDataPath(1, i), fm.mainDataPath(2, i))

        ind += 1

def loadWeeklyGames():
    None

def loadWeeklyStats():
    None

loadSequence()