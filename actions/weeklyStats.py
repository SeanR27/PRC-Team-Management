import pandas as pd
import os

from .. import config
from .. import fileManagement as fm

rootPath = config.mainPath()
dataPath = config.dataPath()
thisPath = os.path.dirname(__file__)

def main():
    weekID = "W0004"
    createWeek(weekID)

def getWeekStatsID(weekID): return "WPS_" + weekID

def getColumnDict():
    """
    The Column Label-Index dictionary for a week table.
    These tables hold information about each game for some week.
    """
    return {"playerID": [0, "PLAYER_ID"],
            "court_ass": [1, "COURT_ASSIGNED"],
            "court_played": [2, "COURT_PLAYED"],
            "result": [3, "RESULT"],
            "ws_before": [4, "WS_BEFORE"],
            "ws_after": [4, "WS_AFTER"],
            "weekAvab": [4, "AVAB"]
            }

def createWeek(weekID):
    colDict = getColumnDict()
    df = pd.DataFrame(columns = [colDict["playerID"][1],
                                    colDict["court_ass"][1],
                                    colDict["court_played"][1],
                                    colDict["result"][1],
                                    colDict["ws_before"][1],
                                    colDict["ws_after"][1],
                                    colDict["weekAvab"][1]])
       
    os.makedirs(config.weekStatsPath(1, weekID), exist_ok = True)
    fm.export(df, config.weekStatsPath(2, weekID), config.weekStatsPath(3, weekID))

def createBaseWeek():
    colDict = getColumnDict()
    createWeek("W0000")
    playersDf = fm.getDF_pkl(config.mainDataPath(2, 0))


main()