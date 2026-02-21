import pandas as pd
import os

from .. import fileManagement as fm
from .. import columns as cols

import players

def main():
    weekID = "W0004"
    createWeek(weekID)

def getWeekStatsID(weekID): return "WPS_" + weekID

def createWeek(weekID):
    colDict = cols.weeklyStats()
    df = pd.DataFrame(columns = [colDict["playerID"][1],
                                    colDict["court_ass"][1],
                                    colDict["court_played"][1],
                                    colDict["result"][1],
                                    colDict["ws_before"][1],
                                    colDict["ws_after"][1],
                                    colDict["weekAvab"][1]])
       
    os.makedirs(fm.weekStatsPath(1, weekID), exist_ok = True)
    fm.export(df, fm.weekStatsPath(2, weekID), fm.weekStatsPath(3, weekID))

def createBaseWeek():
    colDict = cols.weeklyStats()
    playerColDict = cols.players()
    createWeek("W0000")
    playersDF = fm.getDF_pkl(fm.mainDataPath(2, 0))

    nPlayers = len(playersDF)

    initCourt = [[None for _ in range(2)] for _ in range(nPlayers)]

    for i in range(nPlayers):
        initCourt = None


main()